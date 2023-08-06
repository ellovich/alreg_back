from sqladmin import ModelView
from sqlalchemy import Table

from src.doctor.model import Doctor, doctor_patient
from src.patient.model import Patient
from src.user.model import Role, User


class RoleAdmin(ModelView, model=Role):
    column_list = [c.name for c in Role.__table__.c]
    can_delete = False
    name = "Роль"
    name_plural = "Роли и права"
    icon = "fa-solid fa-key"


class UsersAdmin(ModelView, model=User):
    column_list = [c.name for c in User.__table__.c] + [User.doctor]
    column_details_exclude_list = [User.hashed_password]
    # can_delete = False
    name = "Пользователь"
    name_plural = "Пользователи"
    icon = "fa-solid fa-user"


class DoctorAdmin(ModelView, model=Doctor):
    column_list = [Doctor.user] + [c.name for c in Doctor.__table__.c]
    name = "Врач"
    name_plural = "Врачи"
    icon = "fa-solid fa-user-nurse"


class PatientAdmin(ModelView, model=Patient):
    column_list = [c.name for c in Patient.__table__.c]
    name = "Пациент"
    name_plural = "Пациенты"
    icon = "fa-solid fa-hospital-user"


# class DoctorPatientAdmin(ModelView, model=get_class_by_tablename(doctor_patient)):
#     # column_list = [c.name for c in doctor_patient.columns]
#     column_list = []
#     name = "Доктор <-> Пациент"
#     name_plural = "Доктор <-> Пациент"
#     # icon = "fa-solid fa-stethoscope"
