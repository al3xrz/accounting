from pydantic import BaseModel

class SProjectCreate(BaseModel):
    client_id : int
    agent_id : int
