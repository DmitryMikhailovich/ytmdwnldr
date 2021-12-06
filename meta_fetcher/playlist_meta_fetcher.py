import re
from meta_fetcher.meta_fetcher import MetaFetcher


class PlaylistMetaFetcher(MetaFetcher):
    RE_URL_PLAYLIST = re.compile(r'https://.+/playlist\?list=(?P<playlist_id>.+)&?')

    def fetch(self, id_):
        if id_.startswith('https'):
            playlist_url_match = self.RE_URL_PLAYLIST.match(id_)
            if playlist_url_match:
                playlist_id = playlist_url_match.group('playlist_id')
            else:
                self.logger.error('Invalid playlist URL: %s', id_)
                return
        else:
            playlist_id = id_

        playlist_preview = self.ytm.get_playlist(playlist_id, limit=1)
        track_count = playlist_preview.get('trackCount', 100)
        return self.ytm.get_playlist(playlist_id, limit=track_count)
