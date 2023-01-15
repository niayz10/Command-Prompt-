import os
import shutil


def dir_command(path):
    with os.scandir(path) as entries:
        for entry in entries:
            print(4 * " " + entry.name)


def cd_command(base_path, path):
    if '..' in path:
        cnt = path.count('..')
        for _ in range(cnt):
            index = base_path.rfind('\\')
            base_path = base_path[:index]

    else:
        with os.scandir(base_path) as entries:
            for entry in entries:
                if path == entry.name:
                    break
            else:
                raise FileNotFoundError
        if base_path == 'C:\\':
            base_path += path
        else:
            base_path += "\\" + path
    return base_path


def mkdir_command(name_of_dir):
    if not os.path.isdir(name_of_dir):
        os.makedirs(name_of_dir)


def rd_command(base_path, name_of_dir):
    if os.path.isdir(name_of_dir):
        if os.listdir(base_path + "\\" + name_of_dir):
            print(f'The {name_of_dir} has this files: ')
            with os.scandir(base_path + "\\" + name_of_dir) as entries:
                for entry in entries:
                    print(4 * " " + entry.name)
            command = input("Do you really want to delete this dir? Please put you answer: y(Yes) or n(No) ")
            if command == "y":
                shutil.rmtree(name_of_dir)

        else:
            os.rmdir(name_of_dir)
    else:
        print("    Not found directory with this name!!!")


def mv_command(name, new_name):
    if os.path.isdir(name):
        os.rename(name, new_name)
    elif os.path.isfile(name):
        os.rename(name, new_name)


def touch_command(name_of_file):
    if not os.path.isfile(name_of_file):
        with open(name_of_file, mode='w') as file:
            print("Success")
    else:
        print("File with this name already created!!!")


def delete_command(name_of_file):
    if os.path.isfile(name_of_file):
        os.remove(name_of_file)
        print("Success")
    else:
        print("Not found file with this name !!!")


def type_command(name_of_file):
    if os.path.isfile(name_of_file):
        with open(name_of_file, mode='r') as file:
            for row in file.readlines():
                print(4 * " " + row)
    else:
        print("Not found file with this name!!!")
