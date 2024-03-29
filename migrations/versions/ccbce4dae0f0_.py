"""empty message

Revision ID: ccbce4dae0f0
Revises: 19871d40e7f8
Create Date: 2019-10-01 23:36:29.854531

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ccbce4dae0f0'
down_revision = '19871d40e7f8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('parcel_statuses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('order_statuses')
    op.add_column('parcels', sa.Column('dateSent', sa.DateTime(), nullable=True))
    op.add_column('parcels', sa.Column('destination', sa.String(length=255), nullable=True))
    op.add_column('parcels', sa.Column('name', sa.String(length=255), nullable=True))
    op.add_column('parcels', sa.Column('parcelWeight', sa.String(length=255), nullable=True))
    op.add_column('parcels', sa.Column('senderId', sa.Integer(), nullable=True))
    op.drop_constraint('parcels_ibfk_1', 'parcels', type_='foreignkey')
    op.create_foreign_key(None, 'parcels', 'users', ['senderId'], ['id'])
    op.drop_column('parcels', 'orderDate')
    op.drop_column('parcels', 'userID')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('parcels', sa.Column('userID', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.add_column('parcels', sa.Column('orderDate', mysql.DATETIME(), nullable=True))
    op.drop_constraint(None, 'parcels', type_='foreignkey')
    op.create_foreign_key('parcels_ibfk_1', 'parcels', 'users', ['userID'], ['id'])
    op.drop_column('parcels', 'senderId')
    op.drop_column('parcels', 'parcelWeight')
    op.drop_column('parcels', 'name')
    op.drop_column('parcels', 'destination')
    op.drop_column('parcels', 'dateSent')
    op.create_table('order_statuses',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('status', mysql.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.drop_table('parcel_statuses')
    # ### end Alembic commands ###
