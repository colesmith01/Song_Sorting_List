import os
import sys
import numpy as np

import deezer2
from deemix.__main__ import download

from regex import S
import eyed3
from sympy import AlgebraicNumber

def directory_scraper(path, songTags:np.array):    
    for entry in os.scandir(path):
        if entry.is_dir():
                songTags = directory_scraper(entry.path, songTags)
        elif entry.is_file():
                filename, file_extension = os.path.splitext(entry.path)

                typ = 'file'
                if (file_extension == ".mp3"):
                    #commented line 408 of core.py
                    audioFile = eyed3.core.load(entry.path)
                    tag = audioFile.tag
                    songTags = np.append(songTags, tag)
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
mp3tags = directory_scraper(root, mp3tags)

n = 0
client = deezer2.Client()

for tag in mp3tags:
    # n += 1
    # print(n)
    if(type(tag.artist).__name__ != 'str'):
        tag.artist = ' '
    if(type(tag.album).__name__ != 'str'):
        tag.album = ' '
    if(type(tag.title).__name__ != 'str'):
        tag.title = ' '

    trackSearch = client.search(query = tag.title, artist = tag.artist, album = tag.album)
    for track in trackSearch:
        artists = tag.artist.split(',')
        print(len(artists))
        print(track.title)
        # print(track.link)

    







    

#
#download(['https://www.deezer.com/track/887959993'], 'flac')
#print('euan sus')