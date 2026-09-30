# Cloud-Native AI Platform

[![CI](https://github.com/aipusulaofficial-cyber/cloud-native-ai-platform/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/aipusulaofficial-cyber/cloud-native-ai-platform/actions/workflows/ci.yml)
[![Production Tests](https://github.com/aipusulaofficial-cyber/cloud-native-ai-platform/actions/workflows/production-tests.yml/badge.svg?branch=main)](https://github.com/aipusulaofficial-cyber/cloud-native-ai-platform/actions/workflows/production-tests.yml)
[![Security / SBOM](https://github.com/aipusulaofficial-cyber/cloud-native-ai-platform/actions/workflows/security-sbom.yml/badge.svg?branch=main)](https://github.com/aipusulaofficial-cyber/cloud-native-ai-platform/actions/workflows/security-sbom.yml)


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

## Portfolio evidence
[Portfolio evidence map](docs/PORTFOLIO_EVIDENCE.md) — executable proof, architecture mapping and reviewable CI evidence.
