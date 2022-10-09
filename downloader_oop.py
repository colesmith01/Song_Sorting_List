import song_mananger as sm


root = 'D:\Rekordbox USB Backup\Contents0'
songs = sm.song_manager()

songs.mp3_recursive_scraper(root)

songs.export_mp3Links()