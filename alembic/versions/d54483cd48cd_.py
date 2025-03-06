"""empty message

Revision ID: d54483cd48cd
Revises: e8f708d11cff
Create Date: 2025-03-06 20:03:29.027744

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd54483cd48cd'
down_revision: Union[str, None] = 'e8f708d11cff'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Coolers_Specs', sa.Column('min_frequency', sa.Integer(), nullable=False))
    op.add_column('Coolers_Specs', sa.Column('max_frequency', sa.Integer(), nullable=False))
    op.add_column('Coolers_Specs', sa.Column('dispassion', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Coolers_Specs', 'dispassion')
    op.drop_column('Coolers_Specs', 'max_frequency')
    op.drop_column('Coolers_Specs', 'min_frequency')
    # ### end Alembic commands ###
