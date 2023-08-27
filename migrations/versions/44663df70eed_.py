"""empty message

Revision ID: 44663df70eed
Revises: 43bebd7a51c5
Create Date: 2023-08-27 06:02:27.517332

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44663df70eed'
down_revision = '43bebd7a51c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('avatar',
               existing_type=sa.VARCHAR(length=256),
               nullable=True)
        batch_op.alter_column('wallpaper',
               existing_type=sa.VARCHAR(length=256),
               nullable=True)
        batch_op.alter_column('external_link',
               existing_type=sa.VARCHAR(length=256),
               nullable=True)
        batch_op.drop_constraint('user_avatar_key', type_='unique')
        batch_op.drop_constraint('user_wallpaper_key', type_='unique')
        batch_op.create_unique_constraint(None, ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.create_unique_constraint('user_wallpaper_key', ['wallpaper'])
        batch_op.create_unique_constraint('user_avatar_key', ['avatar'])
        batch_op.alter_column('external_link',
               existing_type=sa.VARCHAR(length=256),
               nullable=False)
        batch_op.alter_column('wallpaper',
               existing_type=sa.VARCHAR(length=256),
               nullable=False)
        batch_op.alter_column('avatar',
               existing_type=sa.VARCHAR(length=256),
               nullable=False)

    # ### end Alembic commands ###
