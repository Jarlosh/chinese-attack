import re
from typing import Iterable, List

from config import ROOT_DIR
from os import listdir
from os.path import isfile, join, isdir
import os

from solutions import visualize
from tools.files import read_lines, list_files, list_dirs


class Extensions:
    Python = 'py'
    Java = 'java'
    Cpp = 'cpp'
    Ruby = 'rb'
    # Csharp = 'cs'


class ExtCodes:
    _mapping = {
        Extensions.Python: 48,
        Extensions.Cpp: 40,
        Extensions.Java: 38,
        Extensions.Ruby: 18,
    }

    @classmethod
    def ext_to_code(cls, ext):
        return cls._mapping[ext]


class SourceInfo:
    source_code: str
    lang_code: int
    prob_id: int
    space_id: int = 1
    author: str

    loaded = False
    file_path: str

    def load(self):
        assert not self.loaded, 'already loaded'
        code = ''.join(read_lines(self.file_path))
        self.loaded = True
        self.source_code = code


class Collector:
    SOL_ROOT = f'{ROOT_DIR}/solutions/authors'
    SOL_FOLDER = 'src'

    def author_sols_folder(self, author_name) -> str:
        return f'{self.SOL_ROOT}/{author_name}/{self.SOL_FOLDER}'

    def authors_sols_filenames(self, author_name) -> List[str]:
        return list_files(self.author_sols_folder(author_name))

    def _make_src_info(self, filename, author_sol_folder, author_name='') -> SourceInfo:
        info = SourceInfo()
        pid, ext = filename.split('.')

        info.file_path = f'{author_sol_folder}/{filename}'
        info.lang_code = int(ExtCodes.ext_to_code(ext))
        info.prob_id = int(pid)
        info.author = author_name
        return info

    def collect(self, author_name) -> Iterable[SourceInfo]:
        author_sol_folder = self.author_sols_folder(author_name)
        for filename in list_files(author_sol_folder):
            yield self._make_src_info(filename, author_sol_folder, author_name)

    def get_authors(self) -> Iterable[str]:
        for author_folder in list_dirs(self.SOL_ROOT):
            yield author_folder


class PidCollection:
    def __init__(self, authors=None, exclude_authors=None):
        col = Collector()
        if not authors:  # ok, take all
            authors = col.get_authors()
        if exclude_authors:
            authors = set(authors) - set(exclude_authors)
        self.pids = {solution.prob_id: solution
                     for author in authors
                     for solution in col.collect(author)}
        for sol in self.pids.values():
            sol.load()

    def visualize(self):
        visualize.visualize(self.pids)

PidCollection()