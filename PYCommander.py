#!/usr/bin/env python3

import os


class Viewer():
    def list_files(self, working_directory,):
        file_list = os.listdir(working_directory)
        for file in file_list:
            print(file)

    def change_current_directory(self, target_directory):
        os.chdir(target_directory)


system_errors_logo = '[PYCOMMANDER] -'
viewer = Viewer()
while True:
    current_directory = os.path.abspath(os.curdir)
    input_prefix = f'{current_directory} $> '
    command = input(input_prefix).split()
    if command[0] == 'lf':
        viewer.list_files(current_directory)
    elif command[0] == 'ccd':
        viewer.change_current_directory(command[1])
    elif command[0] == 'exit':
        print('\nBye!')
        exit()
    else:
        print(f'{system_errors_logo} Unknown command!')
