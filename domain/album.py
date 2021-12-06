from .playlist import Playlist


class Album(Playlist):
    def __init__(self):
        super().__init__()
        self.artists = []

    def get_artists_dir_name(self):
        if not self.artists:
            return 'Unknown artist'
        if len(self.artists) > 3:
            return 'Various artists'
        return ', '.join(self.artists)

    def get_album_dir_name(self):
        return '%s - %s' % (self.year or '0000', self.title or 'UNKNOWN TITLE')
