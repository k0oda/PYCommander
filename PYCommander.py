#!/usr/bin/env python3

import os

class Viewer():
    def list_files(self, working_directory,):
        file_list = os.listdir(working_directory)
        for file in file_list:
            print(file)

viewer = Viewer()
while True:
    print(f'\nCurrent directory : {os.path.abspath(os.curdir)}')
    directory = input('Enter a directory for view > ')
    viewer.list_files(directory)
