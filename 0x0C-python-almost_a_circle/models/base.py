#!/usr/bin/python3
"""The Base of all classes for the project"""
import json
import csv


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
        """returns json"""
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """saves json to file.json"""
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
        """json.loads"""
        list_obj = []
        if json_string:
            list_obj = json.loads(json_string)
        return list_obj

    @classmethod
    def create(cls, **dictionary):
        """creates an instance from **dictionary attrs"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1, 0, 0)
        if cls.__name__ == "Square":
            dummy = cls(1, 0, 0)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Loads attrs from file"""
        filename = cls.__name__ + '.json'
        try:
            with open(filename, 'r') as f:
                data = f.read()
                instances = cls.from_json_string(data)
                return [cls.create(**instance) for instance in instances]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Defines file name"""
        filename = cls.__name__ + ".csv"
        with open(filename, mode='w', newline='') as f:
            writer = csv.writer(f)
            if list_objs is None:
                writer.writerow([])
            else:
                for obj in list_objs:
                    if cls.__name__ == 'Rectangle':
                        writer.writerow([
                            obj.id, obj.width, obj.height, obj.x, obj.y])
                    elif cls.__name__ == 'Square':
                        writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """loads file"""
        file_name = cls.__name__ + ".csv"
        objs = []
        try:
            with open(file_name, mode='r') as f:
                reader = csv.reader(f)
                for row in reader:
                    if cls.__name__ == 'Rectangle':
                        obj = cls(int(row[1]), int(row[2]),\
                                  int(row[3]), int(row[4]), int(row[0]))
                    elif cls.__name__ == 'Square':
                        obj = cls(
                            int(row[1]), int(row[2]), int(row[3]), int(row[0])
                        )
                    objs.append(obj)
            return objs
        except FileNotFoundError:
            return objs
