#!/usr/bin/python3
'''The Console a CommandLine Interpreter'''
import cmd


class HBNBCommand(cmd.Cmd):
    """ A class that inherits a cmd class from the module."""

    prompt = '(hbnb) '

    def emptyline(self):
        pass

    def do_quit(self, args):
        '''Quit command to exit the program\n'''
        return True

    def do_EOF(self, args):
        '''EOF command to exit the program\n'''
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
