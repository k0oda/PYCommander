#!/usr/bin/env python3

import os
import shutil

class Messages():
    symbol = '[PYCOMMANDER]'

    error_messages = {
    'folder_not_found': f'{symbol} - Folder not found!',
    'unknown_command': f'{symbol} - Unknown command!',
    'folder_exists': f'{symbol} - Folder already exists!',
    'src_not_found': f'{symbol} - Source not found!',
    'dest_exists': f'{symbol} - Destination name already exists!',
    'dest_not_exists': f'{symbol} - Destination file does not exists!',
    }

    system_messages = {
    'exit': f'{symbol} - Logout...'
    }


class Commander():
    messages = Messages()

    def default(self, *_args):
        print(self.messages.error_messages['unknown_command'])

    def list_files(self, *args):
        if len(args) >= 1:
            if os.path.exists(args[0]):
                target_dir = args[0]
            else:
                print(self.messages.error_messages['folder_not_found'])
                return
        else:
            target_dir = os.curdir
        last_dir = os.getcwd()
        os.chdir(target_dir)
        file_list = os.listdir(os.curdir)
        print('\n{:<20} {:<15} {:<10}'.format('Filename', 'Type', 'Size (bytes)'))
        print('-' * 50)
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
        print('-' * 50 + '\n')
        os.chdir(last_dir)

    def change_current_directory(self, *args):
        path = ' '.join(args)
        if os.path.exists(path):
            os.chdir(path)
        else:
            print(self.messages.error_messages['folder_not_found'])

    def clear(self,):
        print(chr(27) + "[2J")

    def exit(self,):
        print(self.messages.system_messages['exit'])
        exit()

    def mkdir(self, *args):
        path = ' '.join(args)
        if os.path.exists(path):
            print(self.messages.error_messages['folder_exists'])
        else:
            os.makedirs(path)
            print(f'+ [DIR] {path}')

    def rmdir(self, *args):
        path = ' '.join(args)
        if os.path.exists(path):
            shutil.rmtree(path)
            print(f'- [DIR] {path}')
        else:
            print(self.messages.error_messages['folder_not_found'])

    def rename(self, *args):
        if os.path.exists(args[0]):
            src = args[0]
        else:
            print(self.messages.error_messages['src_not_found'])
            return
        if os.path.exists(args[1]):
            print(self.messages.error_messages['dest_exists'])
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
            print(self.messages.error_messages['dest_not_exists'])
            return

    def sys(self, *args):
        command = ' '.join(args)
        os.system(command)

    def run(self, *args):
        path = ' '.join(args)
        if os.path.exists(path):
            print(f'~ {os.path.basename(path)}')
            os.startfile(path)

    def help(self,):
        print('''
Welcome to PYCommander

Available commands:
------------------------------
"ccd [path]" - Change Current Directory
"lf ([path])" - List Files
"mkdir [path]" - Make Directory
"rmdir [path]" - Remove Directory
"rename [old] [new]" - Rename file from <old> to <new>
"rm [path]" - Remove file
"sys [command]" - Command to external terminal
"run [path]" - Run application
"clear" - Clear screen
"exit" - Exit from PYCommander
------------------------------
            ''')


cmd = Commander()

command_list = {
    'ccd': cmd.change_current_directory,
    'lf': cmd.list_files,
    'exit': cmd.exit,
    'clear': cmd.clear,
    'mkdir': cmd.mkdir,
    'rmdir': cmd.rmdir,
    'rename': cmd.rename,
    'rm': cmd.rm,
    'sys': cmd.sys,
    'run': cmd.run,
    'help': cmd.help,
}

os.chdir('/')
while True:
    current_directory = os.getcwd()
    input_prefix = f'{current_directory} $> '
    try:
        command, *attrs = input(input_prefix).split()
    except ValueError:
        continue
    call_program = command_list.get(command, cmd.default)
    call_program(*attrs)
