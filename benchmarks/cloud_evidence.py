import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from cloud_domain import ResourcePolicy,deployment_contract
p=ResourcePolicy(500,1024,3); d=deployment_contract("evidence","registry/evidence:1.0",p)
report={"kind":d["kind"],"replicas":d["spec"]["replicas"],"image":d["spec"]["template"]["spec"]["containers"][0]["image"],"resources_present":"resources" in d["spec"]["template"]["spec"]["containers"][0]}
if report["kind"]!="Deployment" or report["replicas"]!=3 or not report["resources_present"]: raise SystemExit(report)
print(json.dumps(report,sort_keys=True))
