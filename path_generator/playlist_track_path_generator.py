from pathlib import Path

from path_generator.track_path_generator import TrackPathGenerator


class PlaylistTrackPathGenerator(TrackPathGenerator):
    def generate_relative_path(self, collection, track, **kwargs):
        ext = kwargs.get('ext', 'mp3')
        playlist_dir = self.escape_path_part(collection.title)
        file_name = '%s - %s.%s' % (track.artist, track.title, ext)
        file_name = self.escape_path_part(file_name)
        return Path(playlist_dir).joinpath(file_name)
