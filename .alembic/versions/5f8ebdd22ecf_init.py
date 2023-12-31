"""Init

Revision ID: 5f8ebdd22ecf
Revises: 
Create Date: 2023-08-06 01:42:26.129799

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "5f8ebdd22ecf"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "doctor",
        sa.Column("first_name", sa.String(), nullable=False),
        sa.Column("middle_name", sa.String(), nullable=True),
        sa.Column("last_name", sa.String(), nullable=False),
        sa.Column("gender", sa.String(), nullable=False),
        sa.Column("birth", sa.Date(), nullable=False),
        sa.Column("medical_institution", sa.String(), nullable=True),
        sa.Column("jobTitle", sa.String(), nullable=True),
        sa.Column("contacts", sa.JSON(), nullable=True),
        sa.Column("education", sa.JSON(), nullable=True),
        sa.Column("career", sa.JSON(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("created_on", sa.DateTime(), nullable=True),
        sa.Column("updated_on", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_doctor_id"), "doctor", ["id"], unique=True)
    op.create_table(
        "patient",
        sa.Column("gender", sa.String(), nullable=False),
        sa.Column("birth", sa.Date(), nullable=False),
        sa.Column("status", sa.String(), nullable=True),
        sa.Column("discussion", sa.Integer(), nullable=True),
        sa.Column("comment", sa.String(), nullable=True),
        sa.Column("visits", sa.JSON(), nullable=True),
        sa.Column("body_info", sa.JSON(), nullable=True),
        sa.Column("laboratoryTests", sa.JSON(), nullable=True),
        sa.Column("instrumentalStudies", sa.JSON(), nullable=True),
        sa.Column("surgicalTreatment", sa.JSON(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("created_on", sa.DateTime(), nullable=True),
        sa.Column("updated_on", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_patient_id"), "patient", ["id"], unique=True)
    op.create_table(
        "role",
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("permissions", sa.JSON(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("created_on", sa.DateTime(), nullable=True),
        sa.Column("updated_on", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_role_id"), "role", ["id"], unique=True)
    op.create_table(
        "doctor_patient",
        sa.Column("doctor_id", sa.Integer(), nullable=False),
        sa.Column("patient_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["doctor_id"],
            ["doctor.id"],
        ),
        sa.ForeignKeyConstraint(
            ["patient_id"],
            ["patient.id"],
        ),
        sa.PrimaryKeyConstraint("doctor_id", "patient_id"),
    )
    op.create_table(
        "user",
        sa.Column("email", sa.String(length=100), nullable=False),
        sa.Column("hashed_password", sa.String(), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("is_superuser", sa.Boolean(), nullable=False),
        sa.Column("is_verified", sa.Boolean(), nullable=False),
        sa.Column("doctor_id", sa.Integer(), nullable=True),
        sa.Column("role_id", sa.Integer(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("created_on", sa.DateTime(), nullable=True),
        sa.Column("updated_on", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["doctor_id"],
            ["doctor.id"],
        ),
        sa.ForeignKeyConstraint(
            ["role_id"],
            ["role.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_user_email"), "user", ["email"], unique=True)
    op.create_index(op.f("ix_user_id"), "user", ["id"], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_user_id"), table_name="user")
    op.drop_index(op.f("ix_user_email"), table_name="user")
    op.drop_table("user")
    op.drop_table("doctor_patient")
    op.drop_index(op.f("ix_role_id"), table_name="role")
    op.drop_table("role")
    op.drop_index(op.f("ix_patient_id"), table_name="patient")
    op.drop_table("patient")
    op.drop_index(op.f("ix_doctor_id"), table_name="doctor")
    op.drop_table("doctor")
    # ### end Alembic commands ###
