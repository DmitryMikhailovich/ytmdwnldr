from typing import TYPE_CHECKING, Union
import logging
from abc import ABCMeta, abstractmethod

if TYPE_CHECKING:
    from meta_fetcher.meta_fetcher import MetaFetcher
    from mapper.mapper import Mapper
    from ytmusicapi import YTMusic
    from pathlib import Path


class Command(metaclass=ABCMeta):
    def __init__(self, meta_fetcher: 'MetaFetcher', mapper: 'Mapper', downloader):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.meta_fetcher = meta_fetcher
        self.mapper = mapper
        self.downloader = downloader

    @abstractmethod
    def download(self, destination_path: Union['Path', str], id_: str):
        pass

    @staticmethod
    @abstractmethod
    def create(ytm: 'YTMusic'):
        pass
