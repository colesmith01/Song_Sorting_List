song_manager is an object that can be used to sort and download songs from directories and rekordbox playlists
In order to use the song download function a deezer subscription is necessary

The scripts/packages required to run song_manager.py can be installed from:
https://github.com/deafmute1/deemix-librip
https://github.com/supermihi/pytaglib
https://deemix.app/

in client.py of the deezer2 package, you may want to replace the following code @ ~line 195:

json = response.json()
if "error" in json:
    raise ValueError(
        "API request return error for object: {} id: {}".format(
            object_t, object_id
        )
    )
return self._process_json(json, parent)

with:

if (
    response.status_code != 204 and
    response.headers["content-type"].strip().startswith("application/json")
):
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
        # decide how to handle a server that's misbehaving to this extent
        "API request return error for object: {} id: {}".format(
            object_t, object_id
        )
        #response = ""
        return self._process_json(list(), parent)

In order to prevent json read errors.


After using export_mp3Links(), in order to download the extracted songs you can now copy the contents of download_links to the deemix-gui search bar