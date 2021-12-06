from .collection_command import CollectionCommand
from downloader.playlist_downloader import PlaylistDownloader
from meta_fetcher.playlist_meta_fetcher import PlaylistMetaFetcher
from mapper.playlist_mapper import PlaylistMapper
from mapper.track_mapper import TrackMapper


class PlaylistCommand(CollectionCommand):

    @staticmethod
    def create(ytm):
        meta_fetcher = PlaylistMetaFetcher(ytm)
        track_mapper = TrackMapper()
        mapper = PlaylistMapper(track_mapper)
        downloader = PlaylistDownloader.create()
        return PlaylistCommand(meta_fetcher, mapper, downloader)
