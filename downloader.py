import os
root = 'D:\\Rekordbox USB Backup\\Contents'
for entry in os.scandir(root):
   if entry.is_dir():
       typ = 'dir'
   elif entry.is_file():
       typ = 'file'
   elif entry.is_symlink():
       typ = 'link'
   else:
       typ = 'unknown'
   print('{name} {typ}'.format(
       name=entry.name,
       typ=typ,
   ))




















#--------------------------------#





#import deezer

#client = deezer.Client()

#tracks = client.search(query = 'brazil', artist = 'AMC')

#for track  in tracks:
#    print(track.link)

#from deemix.__main__ import download
#download(['https://www.deezer.com/track/887959993'], 'flac')
#print('euan sus')