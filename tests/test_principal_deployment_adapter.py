import pytest

from runtime_adapter import DeploymentAdapter


class RecordingClient:
    def __init__(self):
        self.applied = []

    def apply(self, manifest):
        self.applied.append(manifest)
        return {"accepted": True}


@pytest.mark.parametrize(
    "manifest",
    [
        None,
        {},
        {"metadata": {"name": "api"}},
        {"apiVersion": "apps/v1", "kind": "Deployment", "metadata": {}},
        {"apiVersion": "apps/v1", "kind": "Deployment", "metadata": {"name": "  "}},
        {"apiVersion": "apps/v1", "kind": "Deployment", "metadata": "wrong"},
    ],
)
def test_incomplete_manifest_is_rejected_before_client_call(manifest):
    client = RecordingClient()
    with pytest.raises(ValueError):
        DeploymentAdapter(client).apply(manifest)
    assert client.applied == []


def test_valid_manifest_is_forwarded_without_mutation():
    client = RecordingClient()
    manifest = {
        "apiVersion": "apps/v1",
        "kind": "Deployment",
        "metadata": {"name": "service"},
    }
    assert DeploymentAdapter(client).apply(manifest) == {"accepted": True}
    assert client.applied == [manifest]


def test_invalid_client_rejected_at_construction():
    with pytest.raises(TypeError):
        DeploymentAdapter(object())
