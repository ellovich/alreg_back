from datetime import date

from sqlalchemy import and_, func, or_, select

from src.dao.base import BaseDAO
from src.database import async_session_maker, engine
from src.doctor.model import Doctor, doctor_patient
from src.logger import logger
from src.patient.model import Patient


class DoctorDAO(BaseDAO):
    model = Doctor

    @classmethod
    async def find_all_patients(cls, doctor_id: int) -> list[Patient]:
        q_patients = (
            select(Patient)
            .join(doctor_patient)
            .join(Doctor)
            .where(Doctor.id == doctor_id)
        )

        async with async_session_maker() as session:
            logger.debug(
                q_patients.compile(engine, compile_kwargs={"literal_binds": True})
            )
            patients = await session.execute(q_patients)
            return patients.scalars().all()
