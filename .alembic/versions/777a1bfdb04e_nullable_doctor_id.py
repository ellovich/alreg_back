"""Nullable doctor id

Revision ID: 777a1bfdb04e
Revises: 5f8ebdd22ecf
Create Date: 2023-08-06 12:16:37.310922

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '777a1bfdb04e'
down_revision: Union[str, None] = '5f8ebdd22ecf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###