import logging
from abc import ABCMeta, abstractmethod

import requests


class Mapper(metaclass=ABCMeta):
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)

    def get_thumbnail(self, meta):
        empty = b''
        thumbnails = meta.get('thumbnails')
        if thumbnails and len(thumbnails) > 1:
            thumbnails = filter(lambda x: x['width'] <= 500, thumbnails)
            if not thumbnails:
                return empty
            thumbnails = sorted(thumbnails, key=lambda x: x['width'])
            thumbnail_meta = thumbnails[-1]
            url = thumbnail_meta['url']
            try:
                return requests.get(url).content
            except requests.HTTPError as e:
                self.logger.warning('Failed to get thumbnail for %s', meta.get('title', 'UNKNOWN TITLE'))
        return empty

    @abstractmethod
    def map(self, track_meta):
        pass
