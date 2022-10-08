import os
import shutil as sh

import bytes
import unicodedata
import taglib


def get_title(tags, ptyTypes = None):
    if tags != []:
        if isinstance(tags[0], (dict)):
            return tags[0]["TITLE"][0]
        elif isinstance(tags, (list)):
            if ptyTypes != None:
                i = None

                for tagName in ptyTypes:
                    if tagName == 'Track Title':
                        i = ptyTypes.index(tagName)
                        break

                if i == None:
                    print("Error: No Track Title tag type found in ptyTypes")
                else:
                    return tags[i]
            else:
                print("Error: ptyTypes required for list type tags element")
    else:
        return ''

def get_artists(tags, ptyTypes = None):
    if isinstance(tags[0], (dict)):
        return ' '.join(tags[0]["ARTIST"])
    elif isinstance(tags, (list)):
        if ptyTypes != None:
            i = None

            for tagName in ptyTypes:
                if tagName == 'Artist':
                    i = ptyTypes.index(tagName)

            if i == None:
                print("Error: No Artist tag type found in ptyTypes")
            else:
                artists = tags[i].replace(',', "")
                artists = tags[i].replace(';', "")
                
                return artists
        else:
            print("Error: ptyTypes required for list type tags element")
    else:
        return ''


#recursive function to scan a directory and its subdirectories for mp3 files and return a numpy array of id3 data
def directory_scraper(path, songTags:list):
    extensions = []

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
                    try:
                        audioFile = taglib.File(entry.path)                
                        tag = audioFile.tags
                        songTags.append([tag, entry.path])
                    except:
                        print('error reading path: ' + entry.path)
                else:
                   print('non-music file type: ' + file_extension)
        elif entry.is_symlink():
                typ = 'link'
        else:
                typ = 'unknown'
    
    return songTags

root = 'D:\Music Downloads'

#create array of id3 data
id3Tags = [[]]
id3Tags = directory_scraper(root, id3Tags)

plistFile = open('C:\\Users\\user\\Documents\\rekordbox\\Playlists\\All Tracks USB.txt', 'rb')
rboxTags = []

for line in plistFile:
    if line == b'\x00\n' or line == b'\x00':
        continue

    encClassif = b'\xff'

    if not(line.startswith(encClassif)):
        line = encClassif + line
    
    songData = line.decode('utf16', 'replace').split('\t')

    rboxRow = []
    for value in songData:
        rboxRow.append(value)
    

    rboxTags.append(rboxRow)

rboxTagNames = rboxTags[0]
rboxTags.pop(0)

plistFile.close()

#-----------------------------------

rboxTags.sort(key=lambda tags: get_title(tags, ptyTypes=rboxTagNames))
id3Tags.sort(key=lambda tags: get_title(tags))

unsortedTags = []
externalSourceTags = [[]]
ix1 = 0
ix2 = 1

while ix1 < len(rboxTags) and ix2 < len(id3Tags):
    unsortedTagsEnd = len(unsortedTags) - 1
    
    title1 = get_title(rboxTags[ix1], ptyTypes=rboxTagNames)
    title2 = get_title(id3Tags[ix2])
    artist1 = get_artists(rboxTags[ix1], ptyTypes=rboxTagNames)
    artist2 = get_artists(id3Tags[ix2])

    if title1 > title2:
        unsortedTags.append(id3Tags[ix2])
        ix2 += 1
    elif title1 == title2 and artist1 == artist2:
        ix1 += 1
        ix2 += 1
    else:
        externalSourceTags.append(rboxTags[ix1])
        ix1 += 1



unsortedSongs = open('unsorted_songs.txt', 'w', encoding="utf-16")

#write title and artist of songs that did not match server results to failed_downloads.txt
for tag in unsortedTags:
    sh.copy2(tag[1], 'temp')
    # unsortedSongs.write(tag[1])
    # unsortedSongs.write('\n')
    # unsortedSongs.write(get_title(tag))
    # unsortedSongs.write('\n')
    # unsortedSongs.write(get_artists(tag))
    # unsortedSongs.write('\n')
        
    # unsortedSongs.write('\n')

unsortedSongs.close()