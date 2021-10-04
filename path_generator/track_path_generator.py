from pathlib import Path


class TrackPathGenerator:
    def generate_relative_path(self, track, ext='mp3'):
        album = track.album
        artist_path = Path(album.get_artists_dir_name())
        album_path = artist_path.joinpath(album.get_album_dir_name())
        return album_path.joinpath(track.get_track_file_name(ext=ext))
