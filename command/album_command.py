from command.collection_command import CollectionCommand
from downloader.album_downloader import AlbumDownloader
from mapper.album_mapper import AlbumMapper
from mapper.track_mapper import TrackMapper
from meta_fetcher.album_meta_fetcher import AlbumMetaFetcher


class AlbumCommand(CollectionCommand):

    @staticmethod
    def create(ytm):
        meta_fetcher = AlbumMetaFetcher(ytm)
        track_mapper = TrackMapper()
        album_mapper = AlbumMapper(track_mapper)
        album_downloader = AlbumDownloader.create()
        return AlbumCommand(meta_fetcher, album_mapper, album_downloader)
