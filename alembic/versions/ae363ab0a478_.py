"""empty message

Revision ID: ae363ab0a478
Revises: e0395abcb5ea
Create Date: 2025-03-02 16:23:11.109368

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ae363ab0a478'
down_revision: Union[str, None] = 'e0395abcb5ea'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Power_Units', sa.Column('cost', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Power_Units', 'cost')
    # ### end Alembic commands ###
