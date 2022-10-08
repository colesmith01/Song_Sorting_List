import os
import shutil as sh

import bytes
import unicodedata
import taglib


class song_manager:
    def __init__(self):
        self.dir_id3 = [[]]
        self.plist_id3 = []
        self.rboxTagNames = []

    #recursive function to scan a directory and its subdirectories for mp3 files and return a numpy array of id3 data
    def general_recursive_scraper(self, path):
        extensions = []

        #scan each file/folder in path directory    
        for entry in os.scandir(path):
            #if directory found, recursively call function
            if entry.is_dir():
                    songTags = self.general_recursive_scraper(entry.path, self.dir_id3)
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


    #scrape the id3 data from a rekordbox playlist exported to .txt (KUVO)
    def playlist_scraper(self, dir:str):
        #open playlist file to read byte data
        plistFile = open(dir, 'rb')

        #read each line of id3 data from txt file
        for line in plistFile:
            
            #skip empty lines
            if line == b'\x00\n' or line == b'\x00':
                continue

            #declare utf classifier
            encClassif = b'\xff'

            #add utf classifier to lines w/out
            if not(line.startswith(encClassif)):
                line = encClassif + line
            
            #decode byte data of line
            songData = line.decode('utf16', 'replace').split('\t')

            #create 
            rboxRow = []
            for value in songData:
                rboxRow.append(value)
            

            self.plist_id3.append(rboxRow)

        self.rboxTagNames = self.plist_id3[0]
        self.plist_id3.pop(0)

        plistFile.close()




    def ___title(tags, ptyTypes = None):
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

    def ___artists(tags, ptyTypes = None):
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