import logging
import time
from abc import ABCMeta, abstractmethod
from pathlib import Path


class CollectionDownloader(metaclass=ABCMeta):
    def __init__(self, file_downloader, path_generator, tagger):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.file_downloader = file_downloader
        self.path_generator = path_generator
        self.tagger = tagger

    def download(self, destination_path, collection, tracks, **kwargs):
        force_redownload = kwargs.get('force_redownload', False)
        force_retagging = kwargs.get('force_retagging', True)  # TODO: change to False and pass from command line
        destination_path = Path(destination_path)
        for track in tracks:
            track_path = self.path_generator.generate_relative_path(collection, track, **kwargs)
            file_path = destination_path.joinpath(track_path)
            if file_path.exists() and not force_redownload:
                if force_retagging:
                    self.tagger.tag(file_path, track)
                continue

            for _ in range(5):
                try:
                    self.file_downloader.download(file_path, track.video_id)
                    self.tagger.tag(file_path, track)
                    time.sleep(2)
                    break
                except Exception as e:
                    self.logger.error('Failed to download track "%s": %s', track.title, str(e))
                    time.sleep(10)

    @staticmethod
    @abstractmethod
    def create():
        pass
