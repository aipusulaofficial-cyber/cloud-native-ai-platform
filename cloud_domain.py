from dataclasses import dataclass

@dataclass(frozen=True)
class ResourcePolicy:
    cpu_millicores:int; memory_mib:int; replicas:int
    def validate(self):
        if min(self.cpu_millicores,self.memory_mib,self.replicas)<=0: raise ValueError("resources must be positive")
        if self.replicas>50: raise ValueError("replica limit exceeded")

def deployment_contract(name:str,image:str,policy:ResourcePolicy)->dict:
    policy.validate()
    return {"apiVersion":"apps/v1","kind":"Deployment","metadata":{"name":name},"spec":{"replicas":policy.replicas,"template":{"spec":{"containers":[{"name":name,"image":image,"resources":{"requests":{"cpu":f"{policy.cpu_millicores}m","memory":f"{policy.memory_mib}Mi"}}}]}}}}
