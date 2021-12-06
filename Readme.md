# YTMDWNLDR  

Command line tool for downloading music from YTM. WIP.

## Usage  
### Optional arguments  
- `--dest` - Override download destination directory. 
Tool downloads to the current directory by default.  
- `--headers` - path to JSON file with headers for YTMusic. 
Searches for `headers_auth.json` in current directory by default.   
- `--auth` - if set, then uses headers file to authenticate. 
Perform anonymous requests by default.  
- `--brand` - brand account ID.  

### Download album  
```shell
python ytmdwnldr.py [optional args] album {browse_url|album_playlist_url|browse_id|playlist_id} [[{browse_url|album_playlist_url|browse_id|playlist_id}] ... ]
```

### Download playlist
```shell
python ytmdwnldr.py [optional args] playlist {playlist_url|playlist_id} [[{playlist_url|playlist_id}] ... ]
```
