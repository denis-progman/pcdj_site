"""empty message

Revision ID: ced04ebcbf83
Revises: 9d3c78540317
Create Date: 2023-09-02 21:38:40.879806

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ced04ebcbf83'
down_revision = '9d3c78540317'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_type_assignations', schema=None) as batch_op:
        batch_op.drop_constraint('user_type_assignations_user_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'users', ['user_id'], ['id'], ondelete='CASCADE')

    with op.batch_alter_table('user_types', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.String(length=1024), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_types', schema=None) as batch_op:
        batch_op.drop_column('description')

    with op.batch_alter_table('user_type_assignations', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('user_type_assignations_user_id_fkey', 'users', ['user_id'], ['id'])

    # ### end Alembic commands ###
