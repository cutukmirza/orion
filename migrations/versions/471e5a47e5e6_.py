"""empty message

Revision ID: 471e5a47e5e6
Revises: 0cf0c4589cae
Create Date: 2022-07-01 18:06:30.760377

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '471e5a47e5e6'
down_revision = '0cf0c4589cae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('phone', sa.String(), nullable=False),
    sa.Column('committee', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
