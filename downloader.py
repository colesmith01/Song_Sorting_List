#import deezer

#client = deezer.Client()

#tracks = client.search(query = 'brazil', artist = 'AMC')

#for track  in tracks:
#    print(track.link)

from deemix.__main__ import download
download(['https://www.deezer.com/track/887959993'], 'flac')
print('euan sus')