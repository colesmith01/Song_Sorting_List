To run downloader, python3 must be installed

The scripts/packages required to run downloader.py can be installed from:
https://github.com/deafmute1/deemix-librip
https://eyed3.readthedocs.io/en/latest/installation.html

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

You also may want to comment out:

log.warning(ex)

in the parseError(ex) function under core.py of the eyed3 package to reduce errors while scanning directories.

In order to scan and download from the desired directory, paste the directory path onto line 11 of downlaoder.py, then run the following command:
downloader.py


you can now copy the contents of download_links to the deemix-gui search bar