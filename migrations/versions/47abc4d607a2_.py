"""empty message

Revision ID: 47abc4d607a2
Revises: 
Create Date: 2023-04-15 13:45:02.397984

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '47abc4d607a2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('note', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date', sa.DateTime(timezone=True), nullable=True))
        batch_op.alter_column('data',
               existing_type=sa.DATETIME(),
               type_=sa.String(length=10000),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('note', schema=None) as batch_op:
        batch_op.alter_column('data',
               existing_type=sa.String(length=10000),
               type_=sa.DATETIME(),
               existing_nullable=True)
        batch_op.drop_column('date')

    # ### end Alembic commands ###
