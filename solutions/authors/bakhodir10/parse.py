import re
from os import listdir
from os.path import isfile, join
import os


def get_pwd():
    return os.getcwd()

def list_files(directory):
    return [f for f in listdir(directory)
            if isfile(join(directory, f))]

def write(filename, text):
    with open(filename, 'w') as f:
        f.write(text)

def read_lines(filename):
    with open(filename, 'r') as f:
        return f.readlines()


regex = re.compile(r'(\d{1,4})\.(\w+)')
def parse_name(name):
    res = regex.search(name)
    if res:
        prob_id, ext = res[1], res[2]
        return prob_id, ext
    return None


def parse_names(filenames):
    result = []
    for filename in filenames:
        res = parse_name(filename)
        assert res
        new_name = '.'.join(res)
        tup = filename, new_name
        result.append(tup)
    return result

def honk(rere, old_pwd, new_pwd):
    for old_name, new_name in rere:
        _in = f'{old_pwd}/{old_name}'
        _out = f'{new_pwd}/{new_name}'
        lines = read_lines(_in)
        write(_out, ''.join(lines))

_old_path_add = '/src_original'
_new_path_add = '/src'
_real_pwd = get_pwd()

_old_pwd = _real_pwd + _old_path_add
_new_pwd = _real_pwd + _new_path_add
_filenames = list_files(_old_pwd)
_rr = parse_names(_filenames)
print(_rr)

honk(_rr, _old_pwd, _new_pwd)

