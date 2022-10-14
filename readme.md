# song_manager.py
song_manager is an object that can be used to sort and download songs from directories and rekordbox playlists.
# Required Scripts, APIs and Packages
https://github.com/deafmute1/deemix-librip (finding download links)
https://github.com/supermihi/pytaglib (reading id3 tags)
https://deemix.app/ -> deemix-gui (downloading songs)
# Optional Modifications

in client.py of the deezer2 package from deemix-librip, you may want to replace the following code @ ~line 195:

    json = response.json

    if "error" in json:
    raise ValueError(
        "API request return error for object: {} id: {}".format(
            object_t, object_id
        )
    )
    return self._process_json(json, parent)

with:

    if response.status_code != 204 and response.headers["content-type"].strip().startswith("application/json") :
    try:
        json = response.json()
        if "error" in json:
            raise ValueError(
                "API request return error for object: {} id: {}".format(
                    object_t, object_id
                )
            )
        return self._process_json(json, parent)
    except ValueError:
        "API request return error for object: {} id: {}".format(
            object_t, object_id
        )
        return self._process_json(list(), parent)
    `

In order to prevent json read errors.

# Class Methods
## general_recursive_scraper(path)
Scrapes the path input directory and sub-directories for any music files and stores the id3 data of any music found.
## mp3_recursive_scraper(path)
Scrapes the path input directory and sub-directories for any music files, copies any raw music files to a temp folder, and stores the id3 data of any mp3s found.
## playlist_scraper(path)
**ONLY WORKS WITH REKORDBOX PLAYLISTS EXPORTED TO .txt (KUVO)**
Scrapes the playlist input path for id3 data of songs exported from rekordbox library.
## import_unsorted()
Copies any music files that were not found from rekordbox playlists but were found from directory scraping into a temp folder.
## export_mp3Links()
**IN ORDER TO DOWNLOAD EXPORTED SONGS, A DEEZER SUBSCRIPTION IS NECESSARY**
Creates test files named download_links.txt & failed_downloads.txt

**download_links.txt:** Contains download links of all songs defined by id3 tags scraped from .mp3 files.
**failed_downloads.txt:** Contains the title, artist(s) and path of any songs that download links could not be found for.

In order to download the extracted songs you can now copy the contents of download_links into the deemix-gui search bar and press enter.