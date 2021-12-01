from domain.track import Track
from domain.album import Album


class TrackMapper:
    def map(self, track_meta, album_obj=None):
        if not track_meta['isAvailable']:
            return None
        track = Track()
        track.video_id = track_meta.get('videoId') or track.video_id
        track.index = track_meta.get('index') or track.index
        track.title = track_meta.get('title') or track.title
        artists = track_meta.get('artists') or [{'name': ''}]
        track.artist = artists[0]['name']
        if album_obj:
            track.album = album_obj
        else:
            album_obj = Album()
            if track_meta.get('album'):
                album_obj.title = track_meta.get('album')['name']
            track.album = album_obj

        return track
