from pathlib import Path

from domain.album import Album
from path_generator.track_path_generator import TrackPathGenerator


class AlbumTrackPathGenerator(TrackPathGenerator):
    def generate_relative_path(self, collection, track, **kwargs):
        ext = kwargs.get('ext', 'mp3')
        if not isinstance(collection, Album):
            collection = track.album

        artists_dir_name = self.escape_path_part(collection.get_artists_dir_name())
        album_dir_name = self.escape_path_part(collection.get_album_dir_name())
        file_name = self.escape_path_part(track.get_track_file_name(ext=ext))

        artist_path = Path(artists_dir_name)
        album_path = artist_path.joinpath(album_dir_name)
        return album_path.joinpath(file_name)
