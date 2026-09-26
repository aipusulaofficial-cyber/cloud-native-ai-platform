# Cloud-Native AI Platform

A cloud-native AI service foundation focused on explicit service boundaries, health-aware operation, deployment safety and infrastructure portability.

## Runtime model
```text
request -> service boundary -> domain operation -> infrastructure adapter
                  |                    |
             readiness/liveness     telemetry
```

## Design goals
- Keep domain behavior independent from cloud-specific adapters.
- Make readiness and liveness separate operational contracts.
- Bound runtime resources and dependency work.
- Treat deployment configuration as part of the system contract.

## Deployment
Kubernetes/Helm and infrastructure definitions are kept alongside application code so runtime assumptions are reviewable. CI and production checks validate deployment-facing behavior.

## Reliability & security
Failure semantics are explicit, health signals are operationally meaningful, and security controls use least-privilege defaults. External dependencies remain replaceable adapters.

## Evidence
[ARCHITECTURE.md](ARCHITECTURE.md) · [docs/PRINCIPAL-ENGINEERING.md](docs/PRINCIPAL-ENGINEERING.md) · [ADRs](ADRs/)

**Engineering chain:** Code → Contract → Test → Security → Runtime → Observability → Deployment → Evidence.