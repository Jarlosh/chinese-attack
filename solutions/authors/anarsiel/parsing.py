import re
from os import listdir
from os.path import isfile, join, isdir
import os

def get_pwd():
    return os.getcwd()

def list_files(directory):
    return [f for f in listdir(directory)
            if isfile(join(directory, f))]

def list_dirs(directory):
    return [f for f in listdir(directory)
            if isdir(join(directory, f))]
def write(filename, text):
    with open(filename, 'w') as f:
        f.write(text)

def read_lines(filename):
    with open(filename, 'r') as f:
        return f.readlines()


regex = re.compile(r'(\d{1,4}).*\.(\w+)')
def parse_name(name):
    res = regex.search(name)
    if res:
        prob_id, ext = res[1], res[2]
        return prob_id, ext
    return None

_old_path_add = '/src_original'
_new_path_add = '/src'
_real_pwd = get_pwd()

_old_pwd = _real_pwd + _old_path_add
_new_pwd = _real_pwd + _new_path_add

def main():
    probs = list_dirs(_old_pwd)
    for prob in probs:
        pid = str(prob).split()[0]
        if pid[0] == '#':  # idc why it in name but gonna avoid
            continue
        old_path = f'{_old_pwd}/{prob}/main.cpp'
        new_path = f'{_new_pwd}/{pid}.cpp'

        lines = read_lines(old_path)
        write(new_path, ''.join(lines))
main()
