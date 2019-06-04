# -*- coding: utf-8 -*-

###############################################################################
# "Dropbox" example
###############################################################################
#  Objectives:
#   To learn some basics of the Dropbox API
#  Sources:
#   https://www.dropbox.com/developers/documentation/python?_tk=pilot_lp&_ad=sdk6&_camp=python#tutorial
#   https://dropbox-sdk-python.readthedocs.io/en/latest/api/dropbox.html?highlight=files_list_folder
#   https://dropbox-sdk-python.readthedocs.io/en/latest/api/dropbox.html?highlight=files_list_folder#dropbox.dropbox.Dropbox.files_upload
###############################################################################

import dropbox
from dropboxCredentials import TOKEN

dbx = dropbox.Dropbox(TOKEN)
dbx.users_get_current_account()


###############################################################################
# Getting the root folder files
dir(dbx.files_list_folder('').entries[0])
for entry in dbx.files_list_folder('').entries:
    print(entry.name)

###############################################################################
# Getting the modification dates of files
for entry in dbx.files_list_folder('').entries:
    print(
        entry.name + ": " +
        str(dbx.files_get_metadata("/1984.txt").server_modified) +
        "\n"
    )

###############################################################################
# Downloading a file to my computer
dbx.files_download_to_file(
    "../data/extracted/Dropbox/1984.txt",
    "/1984.txt",
    rev=None
)

###############################################################################
# Creating a folder in dropbox and uploading
dbx.files_create_folder_v2("/scriptsBackup")
filename = "nfl.py"
with open(filename, "rb") as f:
    dbx.files_upload(f.read(), "/scriptsBackup/" + filename)
