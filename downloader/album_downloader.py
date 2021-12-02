import sys
import logging
from pathlib import Path

from downloader.yt_downloader import YTDownloader
from path_generator.track_path_generator import TrackPathGenerator
from tagger.mp3_tagger import MP3Tagger


class AlbumDownloader:
    def __init__(self, file_downloader, path_generator, tagger):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.file_downloader = file_downloader
        self.path_generator = path_generator
        self.tagger = tagger

    def download(self, destination_path, album):
        destination_path = Path(destination_path)
        for track in album.tracks:
            file_path = destination_path.joinpath(self.path_generator.generate_relative_path(track))
            try:
                self.file_downloader.download(file_path, track.video_id)
            except Exception as e:
                logger.error('Failed to download track %s', track.title, exc_info=sys.exc_info())
            self.tagger.tag(file_path, track)

    @staticmethod
    def create():
        file_downloader = YTDownloader()
        path_generator = TrackPathGenerator()
        tagger = MP3Tagger()
        return AlbumDownloader(file_downloader, path_generator, tagger)
