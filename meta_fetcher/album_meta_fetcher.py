from meta_fetcher.playlist_meta_fetcher import PlaylistMetaFetcher


class AlbumMetaFetcher(PlaylistMetaFetcher):

    def fetch(self, id_):
        id_ = id_.strip()
        browse_id = None
        if id_.startswith('https'):
            playlist_url_match = self.RE_URL_PLAYLIST.match(id_)
            if playlist_url_match:
                playlist_id = playlist_url_match.group('playlist_id')
                try:
                    browse_id = self.ytm.get_album_browse_id(playlist_id)
                except Exception as e:
                    self.logger.error('Failed to fetch album browse ID for album ID %s', id_)
                    return
            else:
                browse_url_match = self.RE_URL_BROWSE.match(id_)
                if browse_url_match:
                    browse_id = browse_url_match.group('browse_id')
        else:
            try:
                browse_id = self.ytm.get_album_browse_id(id_)
            except Exception as e:
                self.logger.warning('Failed to get album browse ID for %s', id_)
                browse_id = id_
        return self.ytm.get_album(browse_id)
