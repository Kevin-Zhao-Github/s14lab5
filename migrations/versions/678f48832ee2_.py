"""empty message

Revision ID: 678f48832ee2
Revises: 7706dafd88da
Create Date: 2020-07-26 14:00:39.422499

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '678f48832ee2'
down_revision = '7706dafd88da'
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