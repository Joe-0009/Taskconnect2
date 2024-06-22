"""Initial migration

Revision ID: 6c62ca5ebbfc
Revises: 
Create Date: 2024-06-20 21:23:07.467095

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6c62ca5ebbfc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('last_name', sa.String(length=150), nullable=True))
        batch_op.add_column(sa.Column('location', sa.String(length=100), nullable=True))
        batch_op.add_column(sa.Column('about_me', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('profile_picture', sa.String(length=200), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('profile_picture')
        batch_op.drop_column('about_me')
        batch_op.drop_column('location')
        batch_op.drop_column('last_name')

    # ### end Alembic commands ###