from sqladmin import ModelView
from sqlalchemy import Table

from src.doctor.model import Doctor, doctor_patient
from src.patient.model import Patient
from src.user.model import Role, User


class RoleAdmin(ModelView, model=Role):
    name = "Роль"
    name_plural = "Роли и права"
    icon = "fa-solid fa-key"
    column_list = [c.name for c in Role.__table__.c] + [Role.user]
    # column_details_exclude_list = [Role.]
    # column_exclude_list = [Role.updated_on, Role.created_on]
    # can_delete = False


class UsersAdmin(ModelView, model=User):
    name = "Пользователь"
    name_plural = "Пользователи"
    icon = "fa-solid fa-user"
    column_list = [c.name for c in User.__table__.c] + [User.doctor, User.role]
    column_details_exclude_list = [User.hashed_password]


class DoctorAdmin(ModelView, model=Doctor):
    name = "Врач"
    name_plural = "Врачи"
    icon = "fa-solid fa-user-nurse"
    column_list = (
        [Doctor.user] + [c.name for c in Doctor.__table__.c] + [Doctor.patients]
    )

    # form_ajax_refs = {
    #     "patient": {
    #         "fields": ("id",),
    #         "order_by": ("id",),
    #     }
    # }


class PatientAdmin(ModelView, model=Patient):
    name = "Пациент"
    name_plural = "Пациенты"
    icon = "fa-solid fa-hospital-user"
    column_list = [c.name for c in Patient.__table__.c] + [Patient.doctors]

    # form_ajax_refs = {
    #     "doctor": {
    #         "fields": ("id","last_name"),
    #         "order_by": ("id",),
    #     }
    # }


# class DoctorPatientAdmin(ModelView, model=get_class_by_tablename(doctor_patient)):
#     # column_list = [c.name for c in doctor_patient.columns]
#     column_list = []
#     name = "Доктор <-> Пациент"
#     name_plural = "Доктор <-> Пациент"
#     # icon = "fa-solid fa-stethoscope"


# class ChatsAdmin(ModelView, model=Chat):
#     # icon = "fa-solid fa-comments"
