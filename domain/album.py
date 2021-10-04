class Album:
    def __init__(self):
        self.playlist_id = None
        self.thumbnail = None
        self.artists = []
        self.title = None
        self.description = None
        self.year = 1900
        self.track_count = 0
        self.tracks = []

    def get_artists_dir_name(self):
        if not self.artists:
            return 'Unknown artist'
        if len(self.artists) > 3:
            return 'Various artists'
        return ', '.join(self.artists)

    def get_album_dir_name(self):
        return '%s - %s' % (self.year, self.title)
