from sqlalchemy import JSON, Column, Date, Integer, String
from sqlalchemy.orm import relationship

from src.database import BaseAlchemyModel
from src.doctor.model import doctor_patient


class Patient(BaseAlchemyModel):
    __tablename__ = "patient"

    gender = Column(String, nullable=False)
    birth = Column(Date, nullable=False)

    status = Column(String, nullable=True)
    discussion = Column(Integer, nullable=True)
    comment = Column(String, nullable=True)
    visits = Column(JSON, nullable=True)
    body_info = Column(JSON, nullable=True)

    laboratoryTests = Column(
        JSON, nullable=True
    )  # clinicalBloodTest, lipidogram, bloodChemistryTests,
    instrumentalStudies = Column(
        JSON, nullable=True
    )  # echocardiography, multisliceComputedTomography, carotidArteryDuplexScan
    surgicalTreatment = Column(
        JSON, nullable=True
    )  # typeOfStentGraft: str, sizing: number, numberOfFenestrations: number, numberOfPeripheralStentGrafts: number

    def __str__(self) -> str:
        return f"P#{self.id}"

    doctors = relationship(
        "Doctor", secondary=doctor_patient, back_populates="patients"
    )

    # medication: number,
    # adverseEvents: number,
    # followUp: number,
    # mediafiles: number,
