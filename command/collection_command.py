import sys
from abc import ABC

from .command import Command


class CollectionCommand(Command, ABC):
    def download(self, destination_path, id_):
        try:
            collection_meta = self.meta_fetcher.fetch(id_)
        except Exception as e:
            self.logger.error('Failed to get metadata for %s', id_, exc_info=sys.exc_info())
            return
        collection = self.mapper.map(collection_meta)
        tracks = collection.tracks
        try:
            self.downloader.download(destination_path, collection, tracks)
        except Exception as e:
            self.logger.error('Failed to download %s', collection.title, exc_info=sys.exc_info())
