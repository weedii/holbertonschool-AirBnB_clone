#!/usr/bin/python3

"""
The Console
"""

import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models
from models.user import User
from models.state import State
from models.place import Place
from models.review import Review
from models.city import City
from models.amenity import Amenity


l = ["User", "BaseModel", "State", "Place", "Review", "City", "Amenity"]
class HBNBCommand(cmd.Cmd):
    """Class of HBNBCommand"""

    prompt = "(hbnb) "

    # quit method
    def do_quit(self, arg):
        """This command quits the console"""
        print("Exiting ...")
        return True

    # EOF method
    def do_EOF(self, arg):
        """
        This command quits the console
        """
        print("Exiting ...")
        return True

    # emptyline method
    def emptyline(self):
        """if line is empty do nothing"""
        pass

    # do_create method
    def do_create(self, arg):
        """method that Creates a new instance of BaseModel,
                    saves it (to the JSON file) and prints the id"""
        if len(arg) == 0:
            print("** class name missing **")
            return
        if arg not in l:
            print("** class doesn't exist **")
            return
        if arg == "BaseModel":
            x = BaseModel()
        elif arg == "User":
            x = User()
        elif arg == "State":
            x = State()
        elif arg == "Place":
            x = Place()
        elif arg == "City":
            x = City()
        elif arg == "Amenity":
            x = Amenity()
        elif arg == "Review":
            x = Review()
        x.save()
        print(x.id)
        return

    # do_show method
    def do_show(self, arg):
        """method that Prints the string representation of
                    an instance based on the class name and id"""
        if len(arg) == 0:
            print("** class name missing **")
            return
        args = arg.split(" ")
        if args[0] not in l:
            print("** class doesn't exist **")
            return
        if len(args) != 2:
            print("** instance id missing **")
            return
        x = models.storage.all()
        for i in x.keys():
            f = i.split(".")
            if f[1] == args[1]:
                print(x[i])
                return
        print("** no instance found **")
        return

    # do_destroy method
    def do_destroy(self, arg):
        """method that Deletes an instance based on the class name and id"""
        if len(arg) == 0:
            print("** class name missing **")
            return
        args = arg.split(" ")
        if args[0] not in l:
            print("** class doesn't exist **")
            return
        if len(args) != 2:
            print("** instance id missing **")
            return
        args = arg.split(" ")
        x = models.storage.all()
        for i in x.keys():
            f = i.split(".")
            if f[1] == args[1]:
                x.pop(i)
                models.storage.save()
                return
        print("** no instance found **")

    # do_all method
    def do_all(self, arg):
        """method that Prints all string representation of
                    all instances based or not on the class name"""
        lis = []
        x = models.storage.all()
        args = arg.split(" ")
        if args[0] in l or len(arg) == 0:
            for i in x.keys():
                f = i.split(".")
                if f == "BaseModel" and arg == "BaseModel":
                    lis.append(x[i].__str__())
                elif f == "User" and arg == "User":
                    lis.append(x[i].__str__())
                else:
                    lis.append(x[i].__str__())
            print(lis)
        else:
            print("** class doesn't exist **")
            return

    # do_update method
    def do_update(self, arg):
        """method that Updates an instance based on the
                    class name and id by adding or updating attribute
                                (save the change into the JSON file)"""
        args = arg.split(" ")
        if len(arg) == 0:
            print("** class name missing **")
            return
        if args[0] not in l:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        x = models.storage.all()
        to_upd = 0
        for i in x.keys():
            k = i.split(".")
            if k[1] == args[1]:
                to_upd = 1
                f = i
        if to_upd == 0:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        args = args[0] + " " + args[1]+" "+args[2]+" " + args[3]
        args = args.split(" ")
        k = x[f].__dict__
        p = args[3].split("\"")
        k[args[2]] = p[1]
        x[f].save


if __name__ == '__main__':
    HBNBCommand().cmdloop()
