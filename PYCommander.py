#!/usr/bin/env python3

import os


class Viewer():
    def list_files(self, working_directory,):
        file_list = os.listdir(working_directory)
        for file in file_list:
            print(file)

    def change_directory(self, target_directory):
        os.chdir(target_directory)


viewer = Viewer()
while True:
    input_prefix = f'{os.path.abspath(os.curdir)} $> '
    directory = input(input_prefix)
    viewer.list_files(directory)
