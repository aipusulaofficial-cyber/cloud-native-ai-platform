"""Cloud-native AI deployment contract and resource policy validator."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Deployment:
    name: str
    image: str
    cpu: int
    memory_mb: int
    replicas: int


class ResourcePolicyError(Exception):
    pass


class DeploymentValidator:
    def __init__(self, min_cpu=1, max_cpu=16, min_mem=256, max_replicas=100):
        self.limits = (min_cpu, max_cpu, min_mem, max_replicas)

    def validate(self, d):
        a, b, c, e = self.limits
        if not d.name or not d.image:
            raise ResourcePolicyError("name and image required")
        if not a <= d.cpu <= b or d.memory_mb < c or not 1 <= d.replicas <= e:
            raise ResourcePolicyError("resource policy violation")
        return {
            "name": d.name,
            "image": d.image,
            "replicas": d.replicas,
            "readiness": "/health/ready",
        }
