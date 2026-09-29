from dataclasses import dataclass


@dataclass(frozen=True)
class DeploymentTarget:
    name: str
    namespace: str = "default"


class DeploymentAdapter:
    """Validate essential manifest identity before dispatch to an injected client."""

    def __init__(self, client):
        if not callable(getattr(client, "apply", None)):
            raise TypeError("deployment client must implement apply(manifest)")
        self.client = client

    def apply(self, manifest: dict):
        if not isinstance(manifest, dict):
            raise ValueError("manifest must be a mapping")
        for field in ("apiVersion", "kind"):
            value = manifest.get(field)
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"manifest {field} is required")
        metadata = manifest.get("metadata")
        if not isinstance(metadata, dict):
            raise ValueError("deployment metadata is required")
        name = metadata.get("name")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("deployment name required")
        return self.client.apply(manifest)
