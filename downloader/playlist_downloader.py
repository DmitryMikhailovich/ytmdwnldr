from path_generator.playlist_track_path_generator import PlaylistTrackPathGenerator
from tagger.mp3_tagger import MP3Tagger
from .collection_downloader import CollectionDownloader
from .yt_downloader import YTDownloader


class PlaylistDownloader(CollectionDownloader):

    @staticmethod
    def create():
        file_downloader = YTDownloader()
        path_generator = PlaylistTrackPathGenerator()
        tagger = MP3Tagger()
        return PlaylistDownloader(file_downloader, path_generator, tagger)
