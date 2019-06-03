from os import name as os_name, system, listdir, curdir, path

while True:
    print(f'\nCurrent directory : {path.abspath(curdir)}')
    directory = input('Enter a directory for view > ')
    system('cls' if os_name == 'nt' else 'clear')
    try:
        file_list = listdir(directory)
    except FileNotFoundError:
        print('Unknown directory!')
        continue
    print('.\n..')
    for file in file_list:
        print(file)
