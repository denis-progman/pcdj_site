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
    "listener",
    "dancer",
    "model",
    "dj",
    "sound_producer",
    "vip",
]

def upgrade():
    connection = op.get_bind()
    check_types = [type_row.type_name for type_row in connection.execute(text(f'SELECT "type_name" FROM {table}'))]
    filtered_dict = [{"type_name": type_row} for type_row in userTypes if not type_row in check_types]
    
    if  len(filtered_dict) > 0:
        connection.execute(Table(table, MetaData(), autoload_with=connection).insert().values(filtered_dict))
        print("INFO [user_types migration] executed - added types: ", end="")
        print(filtered_dict)
    else:
        print("INFO [user_types migration] Skipped - all types are already existed")
        
    connection.commit()

def downgrade():
    connection = op.get_bind()
    connection.execute(text(f'TRUNCATE TABLE {table};'))
    connection.commit()
