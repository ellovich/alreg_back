"""Datetime now

Revision ID: 98e4ff3dbb91
Revises: 3b1ce6acebbd
Create Date: 2023-08-06 14:35:36.301418

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "98e4ff3dbb91"
down_revision: Union[str, None] = "3b1ce6acebbd"
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