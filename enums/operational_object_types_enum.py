from enums.main_enum import MainEnum

class OperationalObjectTypesEnum(MainEnum):
    demo = '{"description": "an unfinished track, an example, a sample or a try"}'
    track = '{"description": "a finished music track"}'
    mix = '{"description": "a mix of several tracks"}'
    cover = '{"description": "an image using as a (track, album, mix) cover"}'
    album = '{"description": "a list(collection) of tracks or mixes, can be use as mix sours, or as a chart"}'