from sqlalchemy import JSON, Column, Date, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from src.database import BaseAlchemyModel

doctor_patient = Table(
    "doctor_patient",
    BaseAlchemyModel.metadata,
    Column("doctor_id", ForeignKey("doctor.id"), primary_key=True),
    Column("patient_id", ForeignKey("patient.id"), primary_key=True),
)


class Doctor(BaseAlchemyModel):
    __tablename__ = "doctor"

    first_name = Column(String, nullable=False)
    middle_name = Column(String, nullable=True)
    last_name = Column(String, nullable=False)

    @property
    def full_name(self):
        return f"{self.last_name}  {self.first_name} {self.middle_name if self.middle_name else ''}"

    @property
    def short_name(self):
        return f"{self.last_name}  {self.first_name[:1]}. {(self.middle_name[:1]) + '.' if self.middle_name else ''}"

    gender = Column(String, nullable=False)
    birth = Column(Date, nullable=False)
    image_path = Column(String, nullable=True)

    medical_institution = Column(String, nullable=True)
    jobTitle = Column(String, nullable=True)
    contacts = Column(JSON, nullable=True)
    education = Column(JSON, nullable=True)
    career = Column(JSON, nullable=True)

    def __str__(self) -> str:
        return f"D#{self.id}:{self.short_name}"

    user = relationship("User", back_populates="doctor")
    patients = relationship(
        "Patient", secondary=doctor_patient, back_populates="doctors"
    )
