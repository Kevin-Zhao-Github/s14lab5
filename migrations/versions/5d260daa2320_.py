"""empty message

Revision ID: 5d260daa2320
Revises: b5356773bebe
Create Date: 2020-07-26 14:07:38.473206

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d260daa2320'
down_revision = 'b5356773bebe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('created_date', sa.DateTime(), server_default='Beginning of time', nullable=False))
    op.create_unique_constraint(None, 'users', ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('posts', 'created_date')
    # ### end Alembic commands ###