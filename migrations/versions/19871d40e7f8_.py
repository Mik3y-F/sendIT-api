"""empty message

Revision ID: 19871d40e7f8
Revises: fd7a5df93220
Create Date: 2019-10-01 16:30:59.327949

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19871d40e7f8'
down_revision = 'fd7a5df93220'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order_statuses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order_statuses')
    # ### end Alembic commands ###
