import pytest

from cloud_platform import *


def test_manifest_contract():
    assert (
        DeploymentValidator().validate(Deployment("api", "img", 2, 512, 3))["readiness"]
        == "/health/ready"
    )


def test_resource_limits():
    with pytest.raises(ResourcePolicyError):
        DeploymentValidator().validate(Deployment("api", "img", 99, 512, 1))


def test_required_identity():
    with pytest.raises(ResourcePolicyError):
        DeploymentValidator().validate(Deployment("", "", 1, 512, 1))
