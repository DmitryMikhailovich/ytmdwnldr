import os
import re
from abc import ABCMeta, abstractmethod


class TrackPathGenerator(metaclass=ABCMeta):
    RE_WIN_REPLACE_WITH_DASH = re.compile(r'[:\\/|]')
    RE_WIN_REPLACE_WITH_SPACE = re.compile(r'[?*]')

    def escape_path_part(self, path_part: str):
        if os.name == 'nt':
            path_part = path_part.replace('<', '(')
            path_part = path_part.replace('>', ')')
            path_part = path_part.replace('"', '\'')
            path_part = self.RE_WIN_REPLACE_WITH_DASH.sub('-', path_part)
            return self.RE_WIN_REPLACE_WITH_SPACE.sub(' ', path_part)
        else:
            return path_part.replace('/', '-')

    @abstractmethod
    def generate_relative_path(self, collection, track, **kwargs):
        pass
