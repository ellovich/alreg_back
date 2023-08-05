from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.database import BaseAlchemyModel


class User(BaseAlchemyModel):
    __tablename__ = "user"

    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String(10), nullable=False) # при регистрации ставить user

    doctor_id = Column(Integer, ForeignKey("doctor.id"))
    docktor = relationship("Doctor", back_populates="user")

    def __str__(self) -> str:
        return f"User #{self.id}: ({self.email})"
