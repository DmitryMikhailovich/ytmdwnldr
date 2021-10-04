from mutagen.mp3 import EasyMP3
from mutagen.easyid3 import EasyID3
from mutagen.id3 import APIC, PictureType, Encoding


def album_front_cover_set(id3, key, value):
    id3[APIC.FrameID] = APIC(mime='image/jpeg',
                             type=PictureType.COVER_FRONT,
                             encoding=Encoding.UTF8,
                             desc='Album front cover',
                             data=value)


EasyID3.RegisterTextKey('comment', 'COMM')
EasyID3.RegisterKey('albumfrontcover', setter=album_front_cover_set)


class MP3Tagger:
    def tag(self, file_path, track):
        meta = EasyMP3(str(file_path))

        meta['albumfrontcover'] = track.album_front_cover
        meta['albumartist'] = track.album_artists
        meta['album'] = track.album_title
        meta['date'] = track.release_year
        meta['tracknumber'] = track.track_number
        meta['artist'] = track.artist
        meta['title'] = track.title
        meta['comment'] = track.comment

        meta.save()
