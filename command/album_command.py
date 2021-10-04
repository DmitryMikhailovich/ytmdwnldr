import sys
import logging

from downloader.album_downloader import AlbumDownloader
from mapper.album_mapper import AlbumMapper
from mapper.track_mapper import TrackMapper
from meta_fetcher.album_meta_fetcher import AlbumMetaFetcher


class AlbumCommand:
    def __init__(self, meta_fetcher, album_mapper, album_downloader):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.meta_fetcher = meta_fetcher
        self.album_mapper = album_mapper
        self.album_downloader = album_downloader

    def download(self, destination_path, album_id):
        try:
            album_meta = self.meta_fetcher.fetch(album_id)
        except Exception as e:
            self.logger.error('Failed to get album metadata for %s', album_id, exc_info=sys.exc_info())
            return
        album = self.album_mapper.map(album_meta)
        try:
            self.album_downloader.download(destination_path, album)
        except Exception as e:
            self.logger.error('Failed to download album %s', album.title, exc_info=sys.exc_info())

    @staticmethod
    def create(ytm):
        meta_fetcher = AlbumMetaFetcher(ytm)
        track_mapper = TrackMapper()
        album_mapper = AlbumMapper(track_mapper)
        album_downloader = AlbumDownloader.create()
        return AlbumCommand(meta_fetcher, album_mapper, album_downloader)
