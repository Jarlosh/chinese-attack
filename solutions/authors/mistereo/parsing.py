import re
from os import listdir
from os.path import isfile, join, isdir
import os


def get_pwd():
    return os.getcwd()

def list_dirs(directory):
    return [f for f in listdir(directory)
            if isdir(join(directory, f))]

def list_files(directory):
    return [f for f in listdir(directory)
            if isfile(join(directory, f))]

def write(filename, text):
    with open(filename, 'w') as f:
        f.write(text)

def read_lines(filename):
    with open(filename, 'r') as f:
        return f.readlines()



def search(directory, ext):
    for file in list_files(directory):
        filename, extension = os.path.splitext(file)
        dot_index = extension.rfind('.')
        extension = extension[dot_index + 1:]
        if extension == ext:
            return filename, extension
    return None


def findall():
    real_pwd = get_pwd()
    old_ending = '/src_original'
    new_ending = '/src'

    _old_pwd = real_pwd + old_ending
    _new_pwd = real_pwd + new_ending

    dirs = sorted(list_dirs(_old_pwd))

    result = []
    order = ['cpp', 'py', 'java', 'scala']
    for directory in dirs:
        full_old_pwd = f'{_old_pwd}/{directory}'
        found = False
        for ext in order:
            res = search(full_old_pwd, ext)
            if res:
                # print(res)
                old_name, _ = res
                old_path = f'{full_old_pwd}/{old_name}.{ext}'
                new_path = f'{_new_pwd}/{directory}.{ext}'
                result.append((old_path, new_path))
                found = True
                break
        assert found, f'{directory}'
    return result

def honk():
    for old_path, new_path in findall():
        lines = read_lines(old_path)
        write(new_path, ''.join(lines))


honk()





