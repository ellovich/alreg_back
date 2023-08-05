from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.database import BaseAlchemyModel


class User(BaseAlchemyModel):
    __tablename__ = "users"

    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    doctor_id = Column(Integer, ForeignKey("doctors.id"))
    docktor = relationship("Doctor", back_populates="users")

    def __str__(self) -> str:
        return f"User #{self.id}: ({self.email})"
