from sqlalchemy import JSON, Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.database import BaseAlchemyModel


class Role(BaseAlchemyModel):
    __tablename__ = "role"
    name = Column(String, nullable=False)
    permissions = Column(JSON, nullable=True)

    user = relationship("User", back_populates="role")

    def __str__(self) -> str:
        return f"R#{self.id}: ({self.name})"


class User(BaseAlchemyModel):
    __tablename__ = "user"

    email = Column(String(length=100), unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)

    doctor_id = Column(Integer, ForeignKey("doctor.id"), nullable=True)
    doctor = relationship("Doctor", back_populates="user")

    role_id = Column(Integer, ForeignKey("role.id"), nullable=True)
    role = relationship("Role", back_populates="user")

    def __str__(self) -> str:
        return f"U#{self.id}:{self.email}"
