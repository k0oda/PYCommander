#!/usr/bin/env python3

import os


class Viewer():
    def list_files(self,):
        file_list = os.listdir(os.curdir)
        for file in file_list:
            print(file)

    def change_current_directory(self, *args):
        os.chdir(args[0])

    def clear(self,):
        print(chr(27) + "[2J")

    def exit(self,):
        print('Logout...')
        exit()

    def default(self, *_args):
        print(f'[PYCOMMANDER] - Unknown command!')


viewer = Viewer()

command_list = {
    'ccd': viewer.change_current_directory,
    'lf': viewer.list_files,
    'exit': viewer.exit,
    'clear': viewer.clear,
}

while True:
    current_directory = os.getcwd()
    input_prefix = f'{current_directory} $> '
    command, *attrs = input(input_prefix).split()
    if command != '':
        call_program = command_list.get(command, viewer.default)
        call_program(*attrs)
