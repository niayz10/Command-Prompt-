import os

from commands import dir_command, cd_command, mkdir_command, rd_command, mv_command, touch_command, delete_command, \
    type_command

base_path = 'C:\\'

while True:
    command = input(f'{base_path}->')
    if command == 'q':
        exit()

    elif command == 'dir':
        dir_command(path=base_path)

    elif 'cd' in command:
        command, path = command.split()
        base_path = cd_command(base_path=base_path, path=path)

    elif "mkdir" in command:
        command, name_of_dir = command.split()
        os.chdir(base_path)
        mkdir_command(name_of_dir=name_of_dir)

    elif "rd" in command:
        command, name_of_dir = command.split()
        os.chdir(base_path)
        rd_command(base_path, name_of_dir)
    elif 'mv' in command:
        command, name, new_name = command.split()
        os.chdir(base_path)
        mv_command(name=name, new_name=new_name)

    elif 'touch' in command:
        command, name_of_file = command.split()
        os.chdir(base_path)
        touch_command(name_of_file=name_of_file)

    elif 'del' in command:
        command, name_of_file = command.split()
        os.chdir(base_path)
        delete_command(name_of_file)

    elif 'type' in command:
        command, name_of_file = command.split()
        os.chdir(base_path)
        type_command(name_of_file=name_of_file)
