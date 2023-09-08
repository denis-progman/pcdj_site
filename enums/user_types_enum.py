from enums.main_enum import MainEnum

class UserTypesEnum(MainEnum):
    listener = '{"description": "a minimal role of the registered users, also aloud to post demos, and to make albums"}'
    sound_producer = '{"description": "a track maker, aloud to post tracks"}'
    dj = '{"description": "a mix maker, aloud to post mix"}'
    model = '{"description": "a cover maker, aloud to post pictures for track, mixes and albums"}'
