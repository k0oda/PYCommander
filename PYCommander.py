#!/usr/bin/env python3

import os


class Viewer():
    def list_files(self, *args):
        if len(args) >= 1:
            target_dir = args[0]
        else:
            target_dir = os.curdir
        last_dir = os.getcwd()
        os.chdir(target_dir)
        file_list = os.listdir(os.curdir)
        for file in file_list:
            if os.path.isdir(file):
                type = 'D'
            elif os.path.isfile(file):
                type = 'F'
            elif os.path.islink(file):
                type = 'L'
            elif os.path.ismount(file):
                type = 'M'
            print(f'{file} | {type} | {os.path.getsize(file)} bytes')
        os.chdir(last_dir)

    def change_current_directory(self, *args):
        if os.path.exists(args[0]):
            os.chdir(args[0])
        else:
            print(f'[PYCOMMANDER] - Folder not found!')

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
    try:
        command, *attrs = input(input_prefix).split()
    except ValueError:
        continue
    call_program = command_list.get(command, viewer.default)
    call_program(*attrs)
