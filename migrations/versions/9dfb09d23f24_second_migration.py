"""Second migration

Revision ID: 9dfb09d23f24
Revises: e25b2affaa6c
Create Date: 2020-07-26 13:52:29.828595

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9dfb09d23f24'
down_revision = 'e25b2affaa6c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('created_date', sa.DateTime(), nullable=True))
    op.create_unique_constraint(None, 'users', ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('posts', 'created_date')
    # ### end Alembic commands ###
