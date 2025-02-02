from sqlalchemy.orm import Mapped
from api.database.models.base import Base


class User(Base):
    __tablename__ = "users"
    
    username: Mapped[str]
    password: Mapped[str]
    token: Mapped[str]