class Playlist:
    def __init__(self):
        self.playlist_id = None
        self.title = None
        self.description = None
        self.thumbnail = b''
        self.track_count = 0
        self.tracks = []
        self.year = 0

    def get_playlist_dir_name(self):
        return self.title or 'UNNAMED_PLAYLIST'
