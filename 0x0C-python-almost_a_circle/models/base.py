#!/usr/bin/python3
"""
    this base class manages the id attribute in my future classes
    and to avoind duplicating the same code and some bugs by extension
"""

import json
import csv
import turtle


class Base:
    """
    here we define the class. It worksa s the main file i think
    """
    __nb_objects = 0
    """
        this is a provateclass attribute method
        this keeps track of the number of objectc created from this class
    """
    def __init__(self, id=None):
        """we initialize method with init, and set id to None as default"""
        if id is not None:
            """
                assigns the value of id to a public instance attribute self.id
                otherwise, it increments it, iterating through the values
            """
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns a JSON string representation of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        this saves the csv file with json
        """
        my_file = cls.__name__ + ".json"
        content = []
        if list_objs is not None:
            content = [obj.to_dictionary() for obj in list_objs]
        with open(my_file, "w") as fl:
            fl.write(cls.to_json_string(content))

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create a dummy instance with mandatory attributes
        Call update method to apply real values
        """
        if cls.__name__ == "Rectangle":
            new_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            new_instance = cls(1)
        else:
            new_instance = None

        if new_instance is not None:
            new_instance.update(**dictionary)
        return new_instance
        # new_instance is the dummy instance createid

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances:
        """
        my_file = cls.__name__ + ".json"
        try:
            with open(my_file, 'r') as fl:
                json_info = fl.read()
                instance_info = cls.from_json_string(json_info)
                no_of_instances = [Base.create(**data) for data in instance_info]

                return no_of_instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        this serealizes in csv
        """
        my_file = cls.__name__ + ".csv"
        with open(my_file, mode='w', newline='') as fl:
            edittor = csv.writer(fl)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    row = [obj.id, obj.width, obj.height, obj.x, obj.y]
                elif cls.__name__ == "Square":
                    row = [obj.id, obj.size, obj.x, obj.y]
                edittor.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        """
        this deseralises in csv
        """
        my_file = cls.__name__ + ".csv"
        try:
            with open(my_file, mode='r') as fl:
                reader = csv.reader(fl)
                if cls.__name__ == "Rectangle":
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == "Square":
                    fields = ['id', 'size', 'x', 'y']
                on_inst = []
                for row in reader:
                    info = {field: int(row[i]) for i, field in enumerate(fields)}
                    _inst = cls.create(**info)
                    on_inst.append(_inst)
                return on_inst
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        win_dow = turtle.Screen()
        win_dow.setup(800, 600)
        # win_dow.title("Rectangles & Squares")
        turtle.speed(1)

        for shape in list_rectangles:
            turtle.penup()
            turtle.goto(shape.x, shape.y)
            turtle.pendown()
            for _ in range(2):
                turtle.forward(shape.width)
                turtle.right(90)
                turtle.forward(shape.height)
                turtle.right(90)

        for shape2 in list_squares:
            turtle.penup()
            turtle.goto(shape2.x, shape2.y)
            turtle.pendown()
            for _ in range(4):
                turtle.forward(shape2.size)
                turtle.right(90)

        turtle.done()
