from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.agent import AgentCreate, AgentResponse
from app.services.agent_service import (
    create_agent,
    delete_agent,
    get_agent,
    get_agents,
)

router = APIRouter(
    prefix="/agents",
    tags=["Agents"],
)


@router.post("/", response_model=AgentResponse)
def create(agent: AgentCreate, db: Session = Depends(get_db)):
    return create_agent(db, agent)


@router.get("/", response_model=list[AgentResponse])
def list_agents(db: Session = Depends(get_db)):
    return get_agents(db)


@router.get("/{agent_id}", response_model=AgentResponse)
def get_one(agent_id: int, db: Session = Depends(get_db)):
    agent = get_agent(db, agent_id)

    if agent is None:
        raise HTTPException(status_code=404, detail="Agent not found")

    return agent


@router.delete("/{agent_id}")
def delete(agent_id: int, db: Session = Depends(get_db)):
    agent = delete_agent(db, agent_id)

    if agent is None:
        raise HTTPException(status_code=404, detail="Agent not found")

    return {"message": "Agent deleted successfully"}