import os
import sys

from regex import S
import eyed3
from sympy import AlgebraicNumber

def directory_scraper(path):
    for entry in os.scandir(path):
        if entry.is_dir():
                directory_scraper(entry.path)
        elif entry.is_file():
                filename, file_extension = os.path.splitext(entry.path)

                typ = 'file'
                if (file_extension == ".mp3"):
                    audioFile = eyed3.load(entry.path)
                    tag = audioFile.tag
                    
                    if(type(tag.artist).__name__ == 'str'):
                        print('Artist: ' + tag.artist)
                    if(type(tag.album).__name__ == 'str'):
                        print('Album: ' + tag.album)
                    if(type(tag.title).__name__ == 'str'):
                        print('Title: ' + tag.title)
        elif entry.is_symlink():
                typ = 'link'
        else:
                typ = 'unknown'
    
        #print('{name} {typ}'.format(
        #     name=entry.name,
        #     typ=typ,
        #))

sys.setrecursionlimit(5000)

root = 'D:\\Rekordbox USB Backup\\Contents'
directory_scraper(root)















#--------------------------------#





#import deezer

#client = deezer.Client()

#tracks = client.search(query = 'brazil', artist = 'AMC')

#for track  in tracks:
#    print(track.link)

#from deemix.__main__ import download
#download(['https://www.deezer.com/track/887959993'], 'flac')
#print('euan sus')