import os
import sys
from matplotlib import artist
import numpy as np

import deezer2
from deemix.__main__ import download

from regex import S
import eyed3
#from sympy import AlgebraicNumber

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


root = 'E:\Contents'
mp3tags = np.array([])
mp3tags = directory_scraper(root, mp3tags)

n = 0
client = deezer2.Client()


deezerLinks = open('download_links.txt', 'w')

for tag in mp3tags:
    # n += 1
    # print(n)

    if(type(tag.title).__name__ == 'str'):
        if(type(tag.artist).__name__ != 'str'):
            tag.artist = " "
        else:
            artists = tag.artist.split(',')
            if(len(artists) == 1):
                artists = tag.artist.split(';')
            if(len(artists) == 1):
                artists = tag.artist.split('/')
            if(len(artists) == 1):
                artists = tag.artist.split('&')

        trackSearch = client.search(query = tag.title + " " + tag.artist)

        for track in trackSearch:
            if(tag.artist != " "):
                isExit = False
                for artist0 in artists:
                    if((track.title.lower() in tag.title.lower()) and (artist0.strip().lower() in track.artist.name.lower())):
                        deezerLinks.write(track.link)
                        deezerLinks.write('\n')
                        np.delete(mp3tags, np.where(tag))

                        isExit = True
                        break
                if (isExit):
                    break
            else:
                if(track.title in tag.title):
                    deezerLinks.write(track.link)
                    deezerLinks.write('\n')
                    np.delete(mp3tags, np.where(tag))
                    break


failedDownloads = open('failed_downloads.txt', 'w')
for tag in mp3tags:
    failedDownloads.write(tag.title)
    failedDownloads.write('\n')
    failedDownloads.write(tag.artist)
    failedDownloads.write('\n')
    failedDownloads.write('\n')

    







    

#
#download(['https://www.deezer.com/track/887959993'], 'flac')
#print('euan sus')