#!/usr/bin/python3
"""
Base

"""


class Base:
    """Define Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialise base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Define string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save file"""
        filename = cls.__name__ + ".json"
        lo = []
        if list_objs is not None:
            for i in list_objs:
                lo.append(cls.to_dictionary(i))
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(lo))

    @staticmethod
    def from_json_string(json_string):
       """Json string to dictionary"""
       if json_string is None or len(json_string) == 0:
            return []
       return json.loads(json_string)

    @classmethod
    def load_from_file(cls):
       """file to instance"""
       filename = cls.__name__ + ".json"
       b = []
       try:
          with open(filename, 'r') as f:
            b = cls.from_json_string(f.read())
          for i, e in enumerate(b):
            b[i] = cls.create(**l[i])
       except:
            pass
       return b
