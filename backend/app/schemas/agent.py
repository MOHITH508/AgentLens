from pydantic import BaseModel, ConfigDict


class AgentCreate(BaseModel):
    name: str
    provider: str
    model: str
    project_id: int


class AgentResponse(BaseModel):
    id: int
    name: str
    provider: str
    model: str
    project_id: int

    model_config = ConfigDict(from_attributes=True)