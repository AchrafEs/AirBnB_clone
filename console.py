#!/usr/bin/python3
'''the Console a CommandLine Interpreter'''
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    __classes = [
        "BaseModel",
    ]

    def do_quit(self, args):
        '''A command to exit the program'''
        return true
    def do_EOF(self, args):
        '''A command that handles the end of the file'''
        return true
if __name__ == '__main__':
    HBNBCommand().cmdloop()
