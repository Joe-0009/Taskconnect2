"""Add rating to job

Revision ID: 482bb457adbc
Revises: 0e2f40866cc0
Create Date: 2024-06-25 10:45:04.414101

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '482bb457adbc'
down_revision = '0e2f40866cc0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('job', schema=None) as batch_op:
        batch_op.add_column(sa.Column('rating', sa.Integer(), nullable=True))
        batch_op.alter_column('date_posted',
               existing_type=sa.DATE(),
               type_=sa.DateTime(timezone=True),
               existing_nullable=True)

    with op.batch_alter_table('review', schema=None) as batch_op:
        batch_op.alter_column('date',
               existing_type=sa.DATE(),
               type_=sa.DateTime(timezone=True),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('review', schema=None) as batch_op:
        batch_op.alter_column('date',
               existing_type=sa.DateTime(timezone=True),
               type_=sa.DATE(),
               existing_nullable=True)

    with op.batch_alter_table('job', schema=None) as batch_op:
        batch_op.alter_column('date_posted',
               existing_type=sa.DateTime(timezone=True),
               type_=sa.DATE(),
               existing_nullable=True)
        batch_op.drop_column('rating')

    # ### end Alembic commands ###
