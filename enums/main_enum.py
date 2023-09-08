import enum
import json

class MainEnum(str, enum.Enum):
    # allows contain extra fields using json strings as a enum value
    # in this case actual enum.value returns enum.name instead of this there are json_attributes and all_attributes
    # the solution works but in current cases probably better not use it to keep a clear architecture
    # however could be useful if future
    def __getattribute__(self, name):
        if (name == "value"):
            name = "name"
        elif (name == "json_attributes"):
            return json.loads(super().__getattribute__("value"))
        elif (name == "all_attributes"):
            return {**{"name": super().__getattribute__("name")}, **json.loads(super().__getattribute__("value"))}
        return super().__getattribute__(name)
