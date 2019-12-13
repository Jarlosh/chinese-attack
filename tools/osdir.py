import os
from os.path import isfile, join, isdir


def get_pwd():
    return os.getcwd()


def list_files(directory):
    return [f for f in os.listdir(directory)
            if isfile(join(directory, f))]


def list_dirs(directory):
    return [f for f in os.listdir(directory)
            if isdir(join(directory, f))]


def write(filename, text):
    with open(filename, 'w') as f:
        f.write(text)


def read_lines(filename):
    with open(filename, 'r') as f:
        return f.readlines()