from domain.album import Album
from mapper.playlist_mapper import PlaylistMapper


class AlbumMapper(PlaylistMapper):
    def __init__(self, track_mapper):
        super().__init__(track_mapper)
        self.container_cls = Album

    def map(self, album_meta):
        album = super().map(album_meta)

        album.playlist_id = album_meta.get('audioPlaylistId') or album.playlist_id
        album.artists = [artist['name'] for artist in (album_meta.get('artists') or album.artists)]

        for track in album.tracks:
            track.album = album

        return album
