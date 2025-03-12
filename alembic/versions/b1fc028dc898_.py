"""empty message

Revision ID: b1fc028dc898
Revises: 41c62eaa1d5d
Create Date: 2025-03-12 13:16:26.215211

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b1fc028dc898'
down_revision: Union[str, None] = '41c62eaa1d5d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Basket', sa.Column('vent_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'Basket', 'Vents', ['vent_id'], ['id'])
    op.add_column('Orders', sa.Column('vent_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'Orders', 'Vents', ['vent_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Orders', type_='foreignkey')
    op.drop_column('Orders', 'vent_id')
    op.drop_constraint(None, 'Basket', type_='foreignkey')
    op.drop_column('Basket', 'vent_id')
    # ### end Alembic commands ###
