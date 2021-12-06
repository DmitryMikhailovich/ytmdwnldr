from mapper.mapper import Mapper
from domain.track import Track


class TrackMapper(Mapper):
    def map(self, meta):
        track = Track()
        track.video_id = meta.get('videoId') or track.video_id
        track.index = meta.get('index') or track.index
        track.title = meta.get('title') or track.title
        artists = meta.get('artists') or [{'name': ''}]
        track.artist = artists[0]['name']
        track.thumbnail = self.get_thumbnail(meta)

        return track
