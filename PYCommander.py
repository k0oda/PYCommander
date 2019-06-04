#!/usr/bin/env python3

import os
import shutil


class Viewer():
    def list_files(self, *args):
        if len(args) >= 1:
            if os.path.exists(args[0]):
                target_dir = args[0]
            else:
                print(f'[PYCOMMANDER] - Folder not found!')
                return
        else:
            target_dir = os.curdir
        last_dir = os.getcwd()
        os.chdir(target_dir)
        file_list = os.listdir(os.curdir)
        print('{:<20} {:<15} {:<10}'.format('Filename', 'Type', 'Size (bytes)'))
        for file in file_list:
            if os.path.isdir(file):
                type = 'D'
            elif os.path.isfile(file):
                type = 'F'
            elif os.path.islink(file):
                type = 'L'
            elif os.path.ismount(file):
                type = 'M'
            print('{:<20} |{:<15} |{:<10}'.format(
                file, type, os.path.getsize(file)))
        os.chdir(last_dir)

    def change_current_directory(self, *args):
        path = ' '.join(args)
        if os.path.exists(path):
            os.chdir(path)
        else:
            print(f'[PYCOMMANDER] - Folder not found!')

    def clear(self,):
        print(chr(27) + "[2J")

    def exit(self,):
        print('Logout...')
        exit()

    def default(self, *_args):
        print(f'[PYCOMMANDER] - Unknown command!')


class Editor():
    def mkdir(self, *args):
        path = ' '.join(args)
        if os.path.exists(path):
            print('[PYCOMMANDER] - Folder already exists!')
        else:
            os.makedirs(path)
            print(f'+ [DIR] {path}')

    def rmdir(self, *args):
        path = ' '.join(args)
        if os.path.exists(path):
            shutil.rmtree(path)
            print(f'- [DIR] {path}')
        else:
            print('[PYCOMMANDER] - Folder does not exists!')

    def rename(self, *args):
        if os.path.exists(args[0]):
            src = args[0]
        else:
            print('[PYCOMMANDER] - Source does not exists!')
            return
        if os.path.exists(args[1]):
            print('[PYCOMMANDER] - Destination name already exists!')
            return
        else:
            dst = args[1]
        os.rename(src, dst)
        print(f'{src} -> {dst}')

    def rm(self, *args):
        path = ' '.join(args)
        if os.path.exists(path):
            os.remove(path)
            print(f'- [FILE] {os.path.basename(path)}')
        else:
            print('[PYCOMMANDER] - Destination file does not exists!')
            return


viewer = Viewer()
editor = Editor()

command_list = {
    'ccd': viewer.change_current_directory,
    'lf': viewer.list_files,
    'exit': viewer.exit,
    'clear': viewer.clear,
    'mkdir': editor.mkdir,
    'rmdir': editor.rmdir,
    'rename': editor.rename,
    'rm': editor.rm,
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
