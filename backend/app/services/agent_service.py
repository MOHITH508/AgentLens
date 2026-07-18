from sqlalchemy.orm import Session

from app.database.models.agent import Agent
from app.schemas.agent import AgentCreate


def create_agent(db: Session, agent: AgentCreate):
    db_agent = Agent(
        name=agent.name,
        provider=agent.provider,
        model=agent.model,
        project_id=agent.project_id,
    )

    db.add(db_agent)
    db.commit()
    db.refresh(db_agent)

    return db_agent


def get_agents(db: Session):
    return db.query(Agent).all()


def get_agent(db: Session, agent_id: int):
    return db.query(Agent).filter(Agent.id == agent_id).first()


def delete_agent(db: Session, agent_id: int):
    agent = get_agent(db, agent_id)

    if agent is None:
        return None

    db.delete(agent)
    db.commit()

    return agent