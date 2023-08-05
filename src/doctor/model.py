from sqlalchemy import JSON, Column, Date, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from src.database import BaseAlchemyModel


class Doctor(BaseAlchemyModel):
    __tablename__ = "doctor"

    first_name = Column(String, nullable=False)
    middle_name = Column(String, nullable=True)
    last_name = Column(String, nullable=False)

    @property
    def fullName(self):
        return f"{self.last_name} {self.middle_name if self.middle_name else ''} {self.first_name}"

    gender = Column(String, nullable=False)
    birth = Column(Date, nullable=False)

    medical_institution = Column(String, nullable=True)
    jobTitle = Column(String, nullable=True)
    contacts = Column(JSON, nullable=True)
    education = Column(JSON, nullable=True)
    career = Column(JSON, nullable=True)

    def __str__(self) -> str:
        return f"Doctor #{self.id}: ({self.fullName})"

    user = relationship("User", back_populates="doctor")
    patient = relationship("Patient", secondary="doctor_patient")


doctor_patient = Table("doctor_patient", BaseAlchemyModel.metadata,
    Column("doctor_id", ForeignKey("doctor.id"), primary_key=True),
    Column("patient_id", ForeignKey("patient.id"), primary_key=True),
)