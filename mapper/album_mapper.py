import logging
import requests

from domain.album import Album


class AlbumMapper:
    def __init__(self, track_mapper):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.track_mapper = track_mapper

    def map(self, album_meta):

        album = Album()
        album.playlist_id = album_meta.get('audioPlaylistId') or album.playlist_id
        album.artists = [artist['name'] for artist in (album_meta.get('artists') or album.artists)]
        album.title = album_meta.get('title') or album.title
        album.description = album_meta.get('description') or album.description
        album.year = album_meta.get('year') or album.year
        album.track_count = album_meta.get('trackCount') or album.track_count

        thumbnails = album_meta.get('thumbnails')
        if thumbnails and len(thumbnails) > 1:
            thumbnails = sorted(thumbnails, key=lambda x: x['width'])
            thumbnail = thumbnails[-2]
            url = thumbnail['url']
            try:
                album.thumbnail = requests.get(url).content
            except requests.HTTPError as e:
                self.logger.warning('Failed to get thumbnail for album %s', album.title)

        tracks = []
        for index, track_meta in enumerate(album_meta.get('tracks') or [], start=1):
            track = self.track_mapper.map(track_meta, album)
            if track is None:
                continue
            track.index = index
            tracks.append(track)
        album.tracks = tracks

        return album
