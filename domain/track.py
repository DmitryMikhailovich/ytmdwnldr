from .album import Album


class Track:
    def __init__(self):
        self.video_id = None
        self.index = 0
        self.title = None
        self.artist = None
        self.album = Album()

    def get_track_file_name(self, ext='mp3'):
        if self.index:
            return '%02d - %s.%s' % (self.index, self.title, ext)
        else:
            return '%s.%s' % (self.title, ext)

    @property
    def album_front_cover(self):
        return self.album.thumbnail

    @property
    def comment(self):
        return 'https://music.youtube.com/watch?v=%s' % self.video_id

    @property
    def release_year(self):
        return self.album.year

    @property
    def album_title(self):
        return self.album.title

    @property
    def album_artists(self):
        return '/'.join(self.album.artists) or 'Unknown artist'

    @property
    def track_number(self):
        if self.index:
            if self.album.track_count:
                return '%d/%d' % (self.index, self.album.track_count)
            else:
                return '%d' % self.index
        else:
            return ''
