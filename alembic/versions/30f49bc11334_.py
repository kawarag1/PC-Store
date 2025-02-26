"""empty message

Revision ID: 30f49bc11334
Revises: aa0450cdf281
Create Date: 2025-01-15 00:46:15.359187

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '30f49bc11334'
down_revision: Union[str, None] = 'aa0450cdf281'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Orders', sa.Column('products_id', sa.Integer(), nullable=True))
    op.add_column('Orders', sa.Column('cpu_id', sa.Integer(), nullable=True))
    op.add_column('Orders', sa.Column('gpu_id', sa.Integer(), nullable=True))
    op.add_column('Orders', sa.Column('ram_id', sa.Integer(), nullable=True))
    op.add_column('Orders', sa.Column('motherboard_id', sa.Integer(), nullable=True))
    op.add_column('Orders', sa.Column('m2_id', sa.Integer(), nullable=True))
    op.add_column('Orders', sa.Column('ssd_id', sa.Integer(), nullable=True))
    op.add_column('Orders', sa.Column('hdd_id', sa.Integer(), nullable=True))
    op.add_column('Orders', sa.Column('case_id', sa.Integer(), nullable=True))
    op.add_column('Orders', sa.Column('cooler_id', sa.Integer(), nullable=True))
    op.add_column('Orders', sa.Column('pu_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'Orders', 'Coolers', ['cooler_id'], ['id'])
    op.create_foreign_key(None, 'Orders', 'Power_Units', ['pu_id'], ['id'])
    op.create_foreign_key(None, 'Orders', 'CPU', ['cpu_id'], ['id'])
    op.create_foreign_key(None, 'Orders', 'GPU', ['gpu_id'], ['id'])
    op.create_foreign_key(None, 'Orders', 'HDDs', ['hdd_id'], ['id'])
    op.create_foreign_key(None, 'Orders', 'SSDs', ['ssd_id'], ['id'])
    op.create_foreign_key(None, 'Orders', 'M2_SSDs', ['m2_id'], ['id'])
    op.create_foreign_key(None, 'Orders', 'RAM', ['ram_id'], ['id'])
    op.create_foreign_key(None, 'Orders', 'Products', ['products_id'], ['id'])
    op.create_foreign_key(None, 'Orders', 'PC_Cases', ['case_id'], ['id'])
    op.create_foreign_key(None, 'Orders', 'Motherboards', ['motherboard_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Orders', type_='foreignkey')
    op.drop_constraint(None, 'Orders', type_='foreignkey')
    op.drop_constraint(None, 'Orders', type_='foreignkey')
    op.drop_constraint(None, 'Orders', type_='foreignkey')
    op.drop_constraint(None, 'Orders', type_='foreignkey')
    op.drop_constraint(None, 'Orders', type_='foreignkey')
    op.drop_constraint(None, 'Orders', type_='foreignkey')
    op.drop_constraint(None, 'Orders', type_='foreignkey')
    op.drop_constraint(None, 'Orders', type_='foreignkey')
    op.drop_constraint(None, 'Orders', type_='foreignkey')
    op.drop_constraint(None, 'Orders', type_='foreignkey')
    op.drop_column('Orders', 'pu_id')
    op.drop_column('Orders', 'cooler_id')
    op.drop_column('Orders', 'case_id')
    op.drop_column('Orders', 'hdd_id')
    op.drop_column('Orders', 'ssd_id')
    op.drop_column('Orders', 'm2_id')
    op.drop_column('Orders', 'motherboard_id')
    op.drop_column('Orders', 'ram_id')
    op.drop_column('Orders', 'gpu_id')
    op.drop_column('Orders', 'cpu_id')
    op.drop_column('Orders', 'products_id')
    # ### end Alembic commands ###
