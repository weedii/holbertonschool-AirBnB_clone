#!/usr/bin/python3
"""
The base model for our console
"""
import cmd


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

if __name__ == '__main__':
    HBNBCommand().cmdloop()