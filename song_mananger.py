import os
import shutil as sh

import bytes
import unicodedata

import taglib
import deezer2 as dz


class song_manager:
    def __init__(self):
        self.dir_id3 = [[]]
        self.mp3_id3 = [[]]
        self.plist_id3 = []
        self.rboxTagNames = []

    #extract title from inputted id3 tag
    def getTitle(self, tags, ptyTypes = None):
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
            return str()

    #extract artist from inputted id3 tag
    def getArtists(self, tags, ptyTypes = None):
        if isinstance(tags[0], (dict)) and "ARTIST" in tags[0]:
            return ' '.join(tags[0]["ARTIST"])
        elif isinstance(tags, (list)) and not isinstance(tags[0], (dict)):
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
            return str()

    def ___cpy_file(self, source_file):
        #create temp folder if doesn't exist
        try:
            os.mkdir('temp')
        except OSError as error:
            if error.args[0] != '[WinError 183]':
                print(error)
            pass
                
        
        #copy file to temp folder
        sh.copy2(source_file, 'temp')



    #recursive function to scan a directory and its subdirectories for music files and add dictionaries of id3 data to dir_id3
    def general_recursive_scraper(self, path): 
        extensions = []

        #scan each file/folder in path directory    
        for entry in os.scandir(path):
            #if directory found, recursively call function
            if entry.is_dir():
                    songTags = self.general_recursive_scraper(entry.path)
            #if file found, check for id3 data and if found, add to songTags array
            elif entry.is_file():
                    filename, file_extension = os.path.splitext(entry.path)

                    if (file_extension == ".mp3" or file_extension == ".wav" or file_extension == ".flac" or file_extension == ".aiff"):
                        try:
                            audioFile = taglib.File(entry.path)                
                            tag = audioFile.tags

                            if tag not in self.dir_id3:
                                self.dir_id3.append([tag, entry.path])
                        except:
                            print('error reading path: ' + entry.path)
                    else:
                        print('non-music file type: ' + file_extension)
        
        if [] in self.dir_id3:
            self.dir_id3.remove([])


    
    #recursive function to scan a directory and its subdirectories for mp3 files, 
    # add dictionaries of id3 data to dir_id3, and copy all raw song files into a temp folder
    def mp3_recursive_scraper(self, path):
        extensions = []

        #scan each file/folder in path directory    
        for entry in os.scandir(path):
            #if directory found, recursively call function
            if entry.is_dir():
                    songTags = self.mp3_recursive_scraper(entry.path)
            elif entry.is_file():
                    filename, file_extension = os.path.splitext(entry.path)

                    #if file found and is mp3 check for id3 data add to dir_id3 list alongside file path
                    if (file_extension == ".mp3"):
                        try:
                            audioFile = taglib.File(entry.path)                
                            tag = audioFile.tags

                            if tag not in self.dir_id3:
                                self.dir_id3.append([tag, entry.path])
                            if tag not in self.mp3_id3:
                                self.mp3_id3.append([tag, entry.path])
                        except:
                            print('error reading path: ' + entry.path)

                    #if raw file copy to temp folder
                    elif (file_extension == ".wav" or file_extension == ".flac" or file_extension == ".aiff"):
                        sh.copy2(entry.path, 'temp')
                    else:    
                        print('non-music file type: ' + file_extension)
        if [] in self.dir_id3:
            self.dir_id3.remove([])
        if [] in self.mp3_id3:
            self.mp3_id3.remove([])


    #scrape the id3 data from a rekordbox playlist exported to .txt (KUVO)
    def playlist_scraper(self, path:str):
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

            #create list of id3 data from each line
            rboxRow = []
            for value in songData:
                rboxRow.append(value)
            
            if rboxRow not in self.plist_id3:
                self.plist_id3.append(rboxRow)

        #extract id3 data descriptors
        self.rboxTagNames = self.plist_id3[0]
        self.plist_id3.pop(0)

        self.plist_id3.sort(key=lambda tags: self.getTitle(tags, ptyTypes=self.rboxTagNames))

        plistFile.close()


    #copies all songs found from directories that are not contained in playlists into a temp folder
    def import_unsorted(self):
        self.dir_id3.sort(key=lambda tags: self.getTitle(tags))

        #initialise sorting data
        unsortedTags = []
        externalSourceTags = [[]]
        ix1 = 0
        ix2 = 1

        #compare both lists of id3 data
        while ix1 < len(self.plist_id3) and ix2 < len(self.dir_id3):
            unsortedTagsEnd = len(unsortedTags) - 1
            
            title1 = self.getTitle(self.plist_id3[ix1], ptyTypes=self.rboxTagNames)
            title2 = self.getTitle(self.dir_id3[ix2])
            artist1 = self.getArtists(self.plist_id3[ix1], ptyTypes=self.rboxTagNames)
            artist2 = self.getArtists(self.dir_id3[ix2])

            if title1 > title2:
                unsortedTags.append(self.dir_id3[ix2])
                ix2 += 1
            elif title1 == title2 and artist1 == artist2:
                ix1 += 1
                ix2 += 1
            else:
                externalSourceTags.append(self.plist_id3[ix1])
                ix1 += 1



        unsortedSongs = open('unsorted_songs.txt', 'w', encoding="utf-16")

        #copy all unsorted songs to temp folder
        for tag in unsortedTags:
            self.___cpy_file(tag[1])

        unsortedSongs.close()


    #export all mp3 files stored in song_manager as either download links or failed downloads (couldn't find link)
    def export_mp3Links(self):
        #create mask layer for mp3tags
        downloadMask = [True] * len(self.mp3_id3)

        #open a deezer - python client
        client = dz.Client()

        #create text file to export download links
        deezerLinks = open('download_links.txt', 'w')

        #loop through all stored id3 tags
        for tag in self.mp3_id3:
            #if title is stored in id3 tag
            if  "TITLE" in tag[0]:

                #search deezer servers for song identified by id3 tag
                trackSearch = client.search(query =  self.getTitle(tag) + " " + self.getArtists(tag))
                if trackSearch == None:
                    continue

                #scan results from deezer servers and try to match to id3 tag
                for track in trackSearch:
                    if "ARTIST" in tag[0]:
                        isExit = False

                        artists = tag[0]["ARTIST"]
                        for artist0 in artists:
                            #if id3 tag and server result match, export server link to download_links.txt and mask the mp3_id3 index
                            if((self.getTitle(tag).lower() in track.title.lower()) and (artist0.strip().lower() in track.artist.name.lower())):
                                deezerLinks.write(track.link + ";")
                                deezerLinks.write('\n')
                                downloadMask[self.mp3_id3.index(tag)] = False

                                isExit = True
                                break
                        if (isExit):
                            break
                    else:
                        #if id3 tag and server result match, export server link to download_links.txt and mask the mp3_id3 index
                        if(self.getTitle(tag).lower() in track.title.lower()):
                            deezerLinks.write(track.link + ";")
                            deezerLinks.write('\n')
                            downloadMask[self.mp3_id3.index(tag)] = False
                            #np.delete(mp3tags, np.where(tag))
                            break
            
        deezerLinks.close()

        #create text file to export songs that did not match server results
        failedDownloads = open('failed_downloads.txt', 'w', encoding="utf-16")

        #write title and artist of songs that did not match server results to failed_downloads.txt
        for tag in  self.mp3_id3:
            if downloadMask[self.mp3_id3.index(tag)] and "TITLE" in tag[0]:
                failedDownloads.write(self.getTitle(tag))
                failedDownloads.write('\n')
                if "ARTIST" in tag[0]:
                    failedDownloads.write('; '.join(tag[0]["ARTIST"]))
                    failedDownloads.write('\n')
                
                failedDownloads.write("path: " + tag[1])

                failedDownloads.write('\n')
                failedDownloads.write('\n')

        failedDownloads.close()


    