import argparse
from _ytmdwnldr import YTMDwnldr


def main():
    parser = argparse.ArgumentParser('YTMDWNLDR', description='Downloads from Youtube Music')
    parser.add_argument('--dest', dest='destination_path', default='.',
                        help='output directory for downloads')
    parser.add_argument('--auth', dest='use_auth', action='store_true',
                        help='if specified, then performs authorized requests')
    parser.add_argument('--brand', dest='brand_id',
                        help='optional ID of the brand account')
    parser.add_argument('--headers', dest='headers_path', default='headers_auth.json',
                        help='path to JSON file with request headers')

    subparsers = parser.add_subparsers(title='Download types', dest='download_type')
    album_parser = subparsers.add_parser('album', help='Download one or many albums')
    album_parser.add_argument('album_id', nargs='+',
                              help='URL, playlist ID or browse ID of an album')

    playlist_parser = subparsers.add_parser('playlist', help='Download one or many playlists')
    playlist_parser.add_argument('playlist_id', nargs='+',
                                 help='URL or playlist ID of a playlist')

    args = parser.parse_args()
    download_type = args.download_type
    destination_path = args.destination_path
    use_auth = args.use_auth
    headers_path = args.headers_path
    brand_id = args.brand_id

    downloader = YTMDwnldr(destination_path, use_auth, headers_path, brand_id)
    downloader.go(download_type, args)


if __name__ == '__main__':
    main()
