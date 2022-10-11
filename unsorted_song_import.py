import song_mananger as sm

root = 'D:\\Music Downloads'
playlist = 'C:\\Users\\user\\Documents\\rekordbox\\Playlists\\All Tracks USB.txt'
songs = sm.song_manager()

songs.general_recursive_scraper(root)
songs.playlist_scraper(playlist)

songs.import_unsorted()