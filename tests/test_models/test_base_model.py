#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class test_BaseModel(unittest.TestCase):

    def test_save(self):
        my_model = BaseModel()
        self.aassertEqual(my_model.save(), None)

    def test_to_dict(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        self.assertEqual(print(
            my_model_json), "{'id': 'e048bb45-4659-4e9a-bfd9-77c0f1839a1e', 'created_at': '2023-02-20T13:45:08.313419', 'updated_at': '2023-02-20T13:45:08.313477', 'name': 'My First Model', 'my_number': 89, '__class__': 'BaseModel'}")
