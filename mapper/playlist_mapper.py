from domain.playlist import Playlist
from domain.album import Album
from mapper.mapper import Mapper


class PlaylistMapper(Mapper):
    def __init__(self, track_mapper):
        super().__init__()
        self.track_mapper = track_mapper
        self.container_cls = Playlist

    def map(self, meta):

        playlist = self.container_cls()
        playlist.playlist_id = meta.get('id') or playlist.playlist_id
        playlist.title = meta.get('title') or playlist.title
        playlist.description = meta.get('description') or playlist.description
        playlist.year = meta.get('year') or playlist.year
        playlist.track_count = meta.get('trackCount') or playlist.track_count

        playlist.thumbnail = self.get_thumbnail(meta)

        tracks = []
        tracks_meta = [track_meta for track_meta in (meta.get('tracks') or []) if track_meta['isAvailable']]
        for index, track_meta in enumerate(tracks_meta, start=1):
            track = self.track_mapper.map(track_meta)
            track.index = index
            album_obj = Album()
            if track_meta.get('album'):
                album_obj.title = track_meta.get('album')['name']
            track.album = album_obj

            tracks.append(track)
        playlist.tracks = tracks

        return playlist
