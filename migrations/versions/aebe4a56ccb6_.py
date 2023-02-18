"""empty message

Revision ID: aebe4a56ccb6
Revises: 
Create Date: 2023-02-15 22:56:56.862985

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aebe4a56ccb6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('carbon_session', schema=None) as batch_op:
        batch_op.add_column(sa.Column('amount_resin', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('amount_hardner', sa.Float(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('carbon_session', schema=None) as batch_op:
        batch_op.drop_column('amount_hardner')
        batch_op.drop_column('amount_resin')

    # ### end Alembic commands ###
