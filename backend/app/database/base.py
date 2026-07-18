from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


# Import all models so Alembic can discover them
from app.database.models import *  # noqa: F401,F403

from app.database.models.agent import Agent

from app.database.models.prompt import Prompt