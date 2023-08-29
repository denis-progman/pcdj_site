"""filling user_types table

Revision ID: 7769c8cd7b0c
Revises: 932ac1f731be
Create Date: 2023-08-28 04:57:54.227744

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import text
from sqlalchemy.schema import Table, MetaData

# revision identifiers, used by Alembic.
revision = '7769c8cd7b0c'
down_revision = '932ac1f731be'
branch_labels = None
depends_on = None

table = "user_types"
userTypes = [
    {"type_name": "listener"},
    {"type_name": "dancer"},
    {"type_name": "model"},
    {"type_name": "dj"},
    {"type_name": "sound_producer"},
    {"type_name": "vip"},
]

def upgrade():
    connection = op.get_bind()
    connection.execute(Table(table, MetaData(), autoload_with=connection).insert().values(userTypes))
    connection.commit()

def downgrade():
    connection = op.get_bind()
    connection.execute(text(f'TRUNCATE TABLE {table};'))
    connection.commit()
