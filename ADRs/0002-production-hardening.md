# ADR-0002: Production hardening
FastAPI and OpenTelemetry form the service boundary. Kubernetes probes/resources define runtime safety; Helm packages releases; Terraform owns infrastructure inputs. Trivy/CycloneDX gate security and SBOM; contract/property tests protect APIs; Locust provides load checks.
Production externalizes state, secrets, telemetry and autoscaling.
