from fastapi import APIRouter, Depends

from src.auth.auth import current_active_user
from src.doctor.dao import DoctorDAO
from src.patient.schemas import SPatient
from src.user.model import User

router = APIRouter(prefix="/doctor", tags=["Patients"])


@router.get("/{doctor_id}/patients")
async def get_patients_by_doctor_id(
    doctor_id: int,
    user: User = Depends(current_active_user),
):  # -> list[SPatient]:
    patients = await DoctorDAO.find_all_patients(doctor_id=doctor_id)
    return patients
