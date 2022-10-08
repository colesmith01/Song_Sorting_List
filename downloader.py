import os
import sys
import shutil as sh
import numpy as np

import deezer2

import eyed3


#define root directory
#root = 'E:\Contents'
root = 'D:\Rekordbox USB Backup\Contents0'

#recursive function to scan a directory and its subdirectories for mp3 files and return a numpy array of id3 data
def directory_scraper(path, songTags:np.array):
    extensions = np.array([])

    #scan each file/folder in path directory    
    for entry in os.scandir(path):
        #if directory found, recursively call function
        if entry.is_dir():
                songTags = directory_scraper(entry.path, songTags)
        #if file found, check for id3 data and if found, add to songTags array
        elif entry.is_file():
                filename, file_extension = os.path.splitext(entry.path)

                typ = 'file'
                if (file_extension == ".mp3"):
                    audioFile = eyed3.core.load(entry.path)
                    tag = audioFile.tag
                    songTags = np.append(songTags, tag)
                elif (file_extension == ".wav" or file_extension == ".flac" or file_extension == ".aiff"):
                    sh.copy2(entry.path, 'temp')
                else:    
                   print('non-music file type: ' + file_extension)
        elif entry.is_symlink():
                typ = 'link'
        else:
                typ = 'unknown'
    
    return songTags

# -----------------------------------

#create array of id3 data
mp3tags = np.array([])
mp3tags = directory_scraper(root, mp3tags)

#create mask layer for mp3tags
downloadMask = np.ones(len(mp3tags), dtype=bool)

#open a deezer - python client
client = deezer2.Client()

#create text file to export download links
deezerLinks = open('download_links.txt', 'w')

#loop through all stored id3 tags
for tag in mp3tags:
    #if title is stored in id3 tag
    if(type(tag.title).__name__ == 'str'):
        #if no artist is stored in id3 tag, set to empty string
        if(type(tag.artist).__name__ != 'str'):
            tag.artist = " "
        #if artist is stored in id3 tag, split into array of individual artists
        else:
            artists = tag.artist.split(',')
            if(len(artists) == 1):
                artists = tag.artist.split(';')
            if(len(artists) == 1):
                artists = tag.artist.split('/')
            if(len(artists) == 1):
                artists = tag.artist.split('&')

        #search deezer servers for song identified by id3 tag
        trackSearch = client.search(query = tag.title + " " + tag.artist)

        #scan results from deezer servers and try to match to id3 tag
        for track in trackSearch:
            if(tag.artist != " "):
                isExit = False
                for artist0 in artists:
                    #if id3 tag and server result match, export server link to download_links.txt and mask the mp3tags index
                    if((tag.title.lower() in track.title.lower()) and (artist0.strip().lower() in track.artist.name.lower())):
                        deezerLinks.write(track.link + ";")
                        deezerLinks.write('\n')
                        downloadMask[np.where(mp3tags == tag)] = False
                        #np.delete(mp3tags, np.where(tag))

                        isExit = True
                        break
                if (isExit):
                    break
            else:
                #if id3 tag and server result match, export server link to download_links.txt and mask the mp3tags index
                if(tag.title.lower() in track.title.lower()):
                    deezerLinks.write(track.link + ";")
                    deezerLinks.write('\n')
                    downloadMask[np.where(mp3tags == tag)] = False
                    #np.delete(mp3tags, np.where(tag))
                    break


deezerLinks.close()
#create text file to export songs that did not match server results
failedDownloads = open('failed_downloads.txt', 'w', encoding="utf-8")

#write title and artist of songs that did not match server results to failed_downloads.txt
for tag in mp3tags:
    if(downloadMask[np.where(mp3tags == tag)] and type(tag.title).__name__ == 'str'):
        failedDownloads.write(tag.title)
        failedDownloads.write('\n')
        if(tag.artist != " "):
            failedDownloads.write(tag.artist)
            failedDownloads.write('\n')
        
        failedDownloads.write('\n')

failedDownloads.close()