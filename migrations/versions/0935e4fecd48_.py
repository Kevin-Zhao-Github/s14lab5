"""empty message

Revision ID: 0935e4fecd48
Revises: 075a676b6d1a
Create Date: 2020-07-27 15:53:23.345675

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0935e4fecd48'
down_revision = '075a676b6d1a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('created_date', sa.DateTime(), server_default='1900-01-01 00:00:00', nullable=False))
    op.create_unique_constraint(None, 'users', ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('posts', 'created_date')
    # ### end Alembic commands ###