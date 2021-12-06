from downloader.collection_downloader import CollectionDownloader
from downloader.yt_downloader import YTDownloader
from path_generator.album_track_path_generator import AlbumTrackPathGenerator
from tagger.mp3_tagger import MP3Tagger


class AlbumDownloader(CollectionDownloader):

    @staticmethod
    def create():
        file_downloader = YTDownloader()
        path_generator = AlbumTrackPathGenerator()
        tagger = MP3Tagger()
        return AlbumDownloader(file_downloader, path_generator, tagger)
