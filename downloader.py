from array import array
import os
import sys
import numpy as np

from regex import S
import eyed3
from sympy import AlgebraicNumber

def directory_scraper(path, songTags:np.array):    
    for entry in os.scandir(path):
        if entry.is_dir():
                directory_scraper(entry.path, songTags)
        elif entry.is_file():
                filename, file_extension = os.path.splitext(entry.path)

                typ = 'file'
                if (file_extension == ".mp3"):
                    audioFile = eyed3.core.load(entry.path)
                    tag = audioFile.tag

                    np.append(songTags, tag)
                    #songTags.append(tag)
        elif entry.is_symlink():
                typ = 'link'
        else:
                typ = 'unknown'
    return songTags
        #print('{name} {typ}'.format(
        #     name=entry.name,
        #     typ=typ,
        #))


root = 'D:\\Rekordbox USB Backup\\Contents'
mp3tags = np.array([])
directory_scraper(root, mp3tags)


for tag in mp3tags:
    if(type(tag.artist).__name__ == 'str'):
        print('Artist: ' + tag.artist)
    if(type(tag.album).__name__ == 'str'):
        print('Album: ' + tag.album)
    if(type(tag.title).__name__ == 'str'):
        print('Title: ' + tag.title)















#--------------------------------#





#import deezer

#client = deezer.Client()

#tracks = client.search(query = 'brazil', artist = 'AMC')

#for track  in tracks:
#    print(track.link)

#from deemix.__main__ import download
#download(['https://www.deezer.com/track/887959993'], 'flac')
#print('euan sus')