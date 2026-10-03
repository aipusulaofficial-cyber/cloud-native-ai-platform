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
        if not isinstance(manifest, dict):
            raise ValueError("manifest must be a mapping")
        metadata = manifest.get("metadata")
        if not isinstance(metadata, dict):
            raise ValueError("deployment metadata required")
        name = metadata.get("name")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("deployment name required")
        return self.client.apply(manifest)
