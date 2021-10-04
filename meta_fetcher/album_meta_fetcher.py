import re
import logging

RE_URL_PLAYLIST = re.compile(r'https://.+/playlist\?list=(?P<playlist_id>.+)&?')
RE_URL_BROWSE = re.compile(r'https://.+/browse/(?P<browse_id>.+)\??')


class AlbumMetaFetcher:
    def __init__(self, ytm):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.ytm = ytm

    def fetch(self, album_id):
        album_id = album_id.strip()
        browse_id = None
        if album_id.startswith('https'):
            playlist_url_match = RE_URL_PLAYLIST.match(album_id)
            if playlist_url_match:
                playlist_id = playlist_url_match.group('playlist_id')
                try:
                    browse_id = self.ytm.get_album_browse_id(playlist_id)
                except Exception as e:
                    self.logger.error('Failed to fetch album browse ID for album ID %s', album_id)
                    return
            else:
                browse_url_match = RE_URL_BROWSE.match(album_id)
                if browse_url_match:
                    browse_id = browse_url_match.group('browse_id')
        else:
            try:
                browse_id = self.ytm.get_album_browse_id(album_id)
            except Exception as e:
                self.logger.warning('Failed to get album browse ID for %s', album_id)
                browse_id = album_id
        return self.ytm.get_album(browse_id)
