#!/usr/bin/python3
"""
The base model for our console
"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models
import json


class HBNBCommand(cmd.Cmd):
    intro = "This is the console for our AirBnb clone project , you can get documentation by typing the help command"
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """This command quits the console"""
        print("Exiting ...")
        return True
    
    def do_EOF(self, arg):
        """
        This command quits the console
        """
        print("Exiting ...")
        return True
    def do_create(self, arg):
        if len(arg) == 0:
            print("** class name missing **")
            return
        if arg != "BaseModel":
            print("** class doesn't exist ** ")
            return
        x = BaseModel()
        x.save()
        print(x.id)
        return
    def do_show(self, arg):
        if len(arg) == 0:
            print("** class name missing *")
            return
        if arg[0:9] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(arg[10:]) == 0:
            print("** instance id missing **")
            return
        x = models.storage.all()
        for i in x.keys():
            if i[10:] == arg[10:]:
                print(x[i])
                return
        print("** no instance found **")
    def do_destroy(self, arg):
        if len(arg) == 0:
            print("** class name missing **")
            return
        if arg[:9] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(arg[9:]) == 0:
            print("** instance id missing **")
            return
        x = models.storage.all()
        for i in x.keys():
            if i[10:] == arg[10:]:
                x.pop("BaseModel." + i[10:])
                models.storage.save()
                return
        print("** no instance found **")
    def do_all(self, arg):
        x = models.storage.all()
        l = []
        for i in x.keys():
            l.append(x[i].__str__())
        print(l)
    def do_update(self, arg):
        
if __name__ == '__main__':
    HBNBCommand().cmdloop()