from cloud_domain import *
def test_contract():
 d=deployment_contract("api","example:1",ResourcePolicy(250,256,2));assert d["spec"]["replicas"]==2