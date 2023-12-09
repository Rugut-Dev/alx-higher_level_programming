#!/usr/bin/python3
"""The Base of all classes for the project"""
import json


class Base:
    """Manages id attribute in all future classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        lst = []
        for obj in list_objs:
            lst.append(obj.to_dictionary())
        json_str = cls.to_json_string(lst)
        file_name = cls.__name__ + ".json"

        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        list_obj = []
        if json_string:
            list_obj = json.loads(json_string)
        return list_obj
