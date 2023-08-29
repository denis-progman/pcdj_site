"""empty message

Revision ID: 932ac1f731be
Revises: fae9f122e585
Create Date: 2023-08-28 04:39:54.817628

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '932ac1f731be'
down_revision = 'fae9f122e585'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_type_assignations', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['id'])

    with op.batch_alter_table('user_types', schema=None) as batch_op:
        batch_op.add_column(sa.Column('type_name', sa.String(length=32), nullable=False))
        batch_op.drop_constraint('user_types_type_key', type_='unique')
        batch_op.create_unique_constraint(None, ['type_name'])
        batch_op.create_unique_constraint(None, ['id'])
        batch_op.drop_column('type')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_types', schema=None) as batch_op:
        batch_op.add_column(sa.Column('type', sa.VARCHAR(length=32), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.create_unique_constraint('user_types_type_key', ['type'])
        batch_op.drop_column('type_name')

    with op.batch_alter_table('user_type_assignations', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    # ### end Alembic commands ###
