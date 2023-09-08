from enums.main_enum import MainEnum

class VisibilityEnum(MainEnum):
    all = '{"description": "objects are available for unregistered and registered users"}'
    registered = '{"description": "objects are available for registered users only"}'
    nobody = '{"description": "objects are not available for nobody"}'