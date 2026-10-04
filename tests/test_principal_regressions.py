import pytest

from runtime_adapter import DeploymentAdapter


class StubClient:
    def __init__(self):
        self.calls = []

    def apply(self, manifest):
        self.calls.append(manifest)
        return "accepted"


@pytest.mark.parametrize(
    "manifest",
    [
        None,
        {},
        {"metadata": None},
        {"metadata": {"name": " "}},
        {"metadata": {"name": "api"}},
        {"apiVersion": "apps/v1", "metadata": {"name": "api"}},
        {"kind": "Deployment", "metadata": {"name": "api"}},
    ],
)
def test_invalid_manifest_not_submitted(manifest):
    client = StubClient()
    with pytest.raises(ValueError):
        DeploymentAdapter(client).apply(manifest)
    assert client.calls == []


def test_valid_manifest_submitted():
    client = StubClient()
    manifest = {
        "apiVersion": "apps/v1",
        "kind": "Deployment",
        "metadata": {"name": "api"},
    }
    assert DeploymentAdapter(client).apply(manifest) == "accepted"
    assert client.calls == [manifest]
