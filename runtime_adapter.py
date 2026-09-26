from dataclasses import dataclass


@dataclass(frozen=True)
class DeploymentTarget:
    name: str
    namespace: str = "default"


class DeploymentAdapter:
    """Runtime boundary: validates and submits manifests to an injected client."""

    def __init__(self, client):
        self.client = client

    def apply(self, manifest: dict):
        if not manifest.get("metadata", {}).get("name"):
            raise ValueError("deployment name required")
        return self.client.apply(manifest)
