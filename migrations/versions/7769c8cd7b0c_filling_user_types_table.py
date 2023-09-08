"""filling user_types table

Revision ID: 7769c8cd7b0c
Revises: 932ac1f731be
Create Date: 2023-08-28 04:57:54.227744

"""
from alembic import op
from sqlalchemy.sql import text
from models.user_type import UserType
from enums.user_types_enum import UserTypesEnum

# revision identifiers, used by Alembic.
revision = '7769c8cd7b0c'
down_revision = '932ac1f731be'
branch_labels = None
depends_on = None

def upgrade():
    check_types = [type_row.get("type_name") for type_row in UserType.query.all()]
    insert_types = []
    update_types = []
    for type_enum in UserTypesEnum:
        print()
        if type_enum.name in check_types:
            update_types.append(type_enum.name)
            UserType.update().values(type_enum.value).where(UserType.type_name == type_enum.name)
        else:
            insert_types.append({**{"type_name": type_enum.name}, **type_enum.value})

    if  len(update_types) > 0:
        print(f"INFO [user_types migration] {len(update_types)} - updated types: ", end="")
        print(update_types)
    else:
        print("INFO [user_types migration] NO updated - all existed types are already updated")

    print(insert_types)
    if  len(insert_types) > 0:
        UserType.insert().values(insert_types)
        print(f"INFO [user_types migration] INSERTED {len(insert_types)} - inserted types: ", end="")
        print(insert_types)
    else:
        print("INFO [user_types migration] NO inserted - all types are already existed")
        
def downgrade():
    connection = op.get_bind()
    connection.execute(text(f'TRUNCATE TABLE {UserType.__tablename__};'))
    connection.commit()
