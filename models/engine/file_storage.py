#!/usr/bin/python3
"""

"""
import json
import os.path
from .. import base_model


class BaseModelEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, base_model.BaseModel):
            return obj.to_dict()
        return super().default(obj)

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        #A public instance method to return the dictionary of our objects
        return(self.__objects)

    def new(self, obj):
        #gives the right representation of our obj in the dictionary objects
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj
    
    def save(self):
        #add our objects dictionary to the needed json file
        with open(self.__file_path, "a+", encoding="utf-8") as f:
            j = json.dumps(self.__objects, cls=BaseModelEncoder)
            f.write(j)

    def reload(self):
        if os.path.isfile(self.__file_path) == False:
            return
        f = open(self.__file_path, "r", encoding="utf-8")
        read = f.read()
        if read:
            lst = json.loads(read)
            self.__objects = dict(lst)
