#!/usr/bin/python3
"""
Base

"""
import turtle
import csv
from turtle import *



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
       len = []
       try:
          with open(filename, 'r') as f:
            len = cls.from_json_string(f.read())
          for i, e in enumerate(len):
            len[i] = cls.create(**l[i])
       except:
            pass
       return len

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saving file of csv"""

        b = [listToDictionary()]
        if list_objs != None:
            list_objs = []
        for items in list_objs:
            listToDictionary.append(items.to_dictionary())

        with open('{}.csv'.format(cls.__name__), 'w', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(list_obj)
    @classmethod
    def load_from_file_csv(cls):
        """Loads from csv file
        """

        len = []
        len_dict = {}
        with open(cls.__name__ + ".csv", mode="r") as read_file:
            read_from = csv.DictReader(read_file)
            for item in read_from:
                for a, b in dict(item).items():
                    len_dict[k] = int(v)
                # formatting with create()
                len.append(cls.create(**len_dict))
        return len

    def draw(list_rectangles, list_squares):
        """Update the class Base"""

        color('list_rectangles', 'list_square')
        begin_fill()
        while True:
            forward(200)
            left(170)
            if abs(pos()) < 1:
                break
        end_fill()
        done()

