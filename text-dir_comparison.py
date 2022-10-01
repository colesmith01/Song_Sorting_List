import os
import numpy as np
import pandas as pd
import unicodedata
import eyed3

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
                if (file_extension == ".mp3" or file_extension == ".wav" or file_extension == ".flac" or file_extension == ".aiff"):
                    audioFile = eyed3.core.load(entry.path)
                    tag = audioFile.tag
                    songTags = np.append(songTags, tag)
                else:
                   print('non-music file type: ' + file_extension)
        elif entry.is_symlink():
                typ = 'link'
        else:
                typ = 'unknown'
    
    return songTags

root = 'D:\Music Downloads'

#create array of id3 data
id3tags = np.array([])
#id3tags = directory_scraper(root, id3tags)

# dataframe = pd.read_csv('C:\\Users\\user\\Documents\\rekordbox\\Playlists\\All Tracks USB.txt', sep='\t')
# print(dataframe)


plistFile = open('C:\\Users\\user\\Documents\\rekordbox\\Playlists\\All Tracks USB.txt', 'r')
rboxTags = []

for line in plistFile:
    if line =='\x00\n':
        continue
    
    songData = line.split('\t')

    rboxRow = []
    for value in songData:
        rboxRow.append(value)
    
    rboxTags.append(rboxRow)

plistFile.close()


i = 0
#loop through all stored id3 tags
for pty in rboxTags[0]:
    print(pty)
    if i != 0:
        if pty == 'Track Title':
            titleIndex = np.where(pty == rboxTags[0])
            print('test')
        if pty == 'Artist':
            artistIndex = np.where(pty == rboxTags[0]) 

    i = i+1


i = 0
for tag in rboxTags:
    print('Track: ' + tag[titleIndex])
    print('Track: ' + tag[artistIndex])