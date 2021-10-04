from pathlib import Path
import youtube_dl


class YTDownloader:
    def download(self, file_path, video_id, codec='mp3'):
        file_path = Path(file_path)
        with youtube_dl.YoutubeDL({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': codec,
                'preferredquality': '0'
            }],
            'outtmpl': str(file_path.parent.joinpath(file_path.stem)) + '.%(etx)s',
        }) as ydl:
            ydl.download(['https://www.youtube.com/watch?v=%s' % video_id])
