import logging
import time
import uuid

from fastapi import FastAPI, HTTPException
from fastapi import Request as FastAPIRequest
from opentelemetry import trace
from pydantic import BaseModel

from cloud_domain import ResourcePolicy, deployment_contract

try:
    from opentelemetry.sdk.resources import Resource
    from opentelemetry.sdk.trace import TracerProvider
    from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter

    p = TracerProvider(resource=Resource.create({"service.name": "cloud-native-ai-platform"}))
    p.add_span_processor(BatchSpanProcessor(ConsoleSpanExporter()))
    trace.set_tracer_provider(p)
except (ImportError, RuntimeError) as exc:
    logging.getLogger(__name__).warning("OpenTelemetry setup unavailable: %s", exc)

app = FastAPI(title="cloud-native-ai-platform", version="1.0.0")
tracer = trace.get_tracer("cloud-native-ai-platform")


class Request(BaseModel):
    key: str
    payload: dict = {}


@app.middleware("http")
async def observability_headers(request: FastAPIRequest, call_next):
    started = time.perf_counter()
    request_id = request.headers.get("x-request-id") or str(uuid.uuid4())
    correlation_id = request.headers.get("x-correlation-id") or request_id
    response = await call_next(request)
    response.headers["x-request-id"] = request_id
    response.headers["x-correlation-id"] = correlation_id
    response.headers["x-latency-ms"] = f"{(time.perf_counter() - started) * 1000:.3f}"
    return response


@app.get("/health/live")
def live():
    return {"status": "ok"}


@app.get("/health/ready")
def ready():
    return {"status": "ready"}


@app.post("/v1/deployments")
def handle(r: Request):
    with tracer.start_as_current_span("cloud-native-ai-platform.domain"):
        try:
            p = ResourcePolicy(
                int(r.payload.get("cpu_millicores", 250)),
                int(r.payload.get("memory_mib", 256)),
                int(r.payload.get("replicas", 2)),
            )
            return deployment_contract(r.key, r.payload.get("image", "example:latest"), p)
        except (ValueError, KeyError, RuntimeError) as e:
            raise HTTPException(status_code=400, detail=str(e)) from e
