from cloud_domain import ResourcePolicy, deployment_contract


def test_deployment_contract_contains_resource_policy():
    deployment = deployment_contract("api", "example/api:1", ResourcePolicy(250, 512, 3))
    assert deployment["apiVersion"] == "apps/v1"
    assert deployment["spec"]["replicas"] == 3
    container = deployment["spec"]["template"]["spec"]["containers"][0]
    assert container["image"] == "example/api:1"
    assert container["resources"]["requests"] == {"cpu": "250m", "memory": "512Mi"}
