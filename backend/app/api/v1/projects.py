from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from app.database.session import get_db
from app.schemas.project import (
    ProjectCreate,
    ProjectResponse,
    ProjectUpdate,
)
from app.services.project_service import (
    create_project,
    get_projects,
    get_project,
    delete_project,
    update_project,
)

router = APIRouter(
    prefix="/projects",
    tags=["Projects"],
)


@router.post("/", response_model=ProjectResponse)
def create(project: ProjectCreate, db: Session = Depends(get_db)):
    return create_project(db, project)


@router.get("/", response_model=list[ProjectResponse])
def list_projects(db: Session = Depends(get_db)):
    return get_projects(db)

@router.get("/{project_id}", response_model=ProjectResponse)
def get_one(project_id: int, db: Session = Depends(get_db)):
    project = get_project(db, project_id)

    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")

    return project


@router.delete("/{project_id}")
def delete(project_id: int, db: Session = Depends(get_db)):
    project = delete_project(db, project_id)

    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")

    return {"message": "Project deleted successfully"}

@router.put("/{project_id}", response_model=ProjectResponse)
def update(
    project_id: int,
    project: ProjectUpdate,
    db: Session = Depends(get_db),
):
    updated = update_project(db, project_id, project)

    if updated is None:
        raise HTTPException(
            status_code=404,
            detail="Project not found",
        )

    return updated