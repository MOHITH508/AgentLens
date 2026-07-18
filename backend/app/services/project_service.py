from sqlalchemy.orm import Session

from app.database.models.project import Project
from app.schemas.project import ProjectCreate


def create_project(db: Session, project: ProjectCreate):
    db_project = Project(
        name=project.name,
        description=project.description,
    )
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project


def get_projects(db: Session):
    return db.query(Project).all()


def get_project(db: Session, project_id: int):
    return db.query(Project).filter(Project.id == project_id).first()


def delete_project(db: Session, project_id: int):
    project = get_project(db, project_id)

    if not project:
        return None

    db.delete(project)
    db.commit()

    return project