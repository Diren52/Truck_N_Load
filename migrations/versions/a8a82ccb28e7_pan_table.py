"""pan table

Revision ID: a8a82ccb28e7
Revises: 4d29f16f74c7
Create Date: 2018-05-13 00:05:21.438930

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a8a82ccb28e7'
down_revision = '4d29f16f74c7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pan',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Weight', sa.Numeric(), nullable=False),
    sa.Column('Height', sa.Numeric(), nullable=False),
    sa.Column('Width', sa.Numeric(), nullable=False),
    sa.Column('Length', sa.Numeric(), nullable=False),
    sa.Column('Delivery ID', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['Delivery ID'], ['delivery.id'], onupdate='CASCADE', ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pan')
    # ### end Alembic commands ###
