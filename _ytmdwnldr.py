import sys
import logging
from pathlib import Path

from ytmusicapi import YTMusic

from command.album_command import AlbumCommand


def get_ytm(use_auth, headers_path, brand_id):
    if not use_auth:
        return YTMusic()
    headers_path = str(headers_path)
    if not Path(headers_path).exists():
        YTMusic.setup(filepath=headers_path)
    if brand_id:
        return YTMusic(headers_path, brand_id)
    else:
        return YTMusic(headers_path)


class YTMDwnldr:
    def __init__(self, destination_path, use_auth, headers_path, brand_id):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.destination_path = destination_path
        self.ytm = get_ytm(use_auth, headers_path, brand_id)

    def go(self, download_type, args):
        if download_type == 'album':
            command = AlbumCommand.create(self.ytm)
            for album_id in args.album_id:
                self.logger.info('Going to download album %s', album_id)
                command.download(self.destination_path, album_id)
        else:
            print('Download type is not specified')
            sys.exit(1)
