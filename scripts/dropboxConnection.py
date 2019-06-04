# -*- coding: utf-8 -*-

###############################################################################
# "Dropbox" example
###############################################################################
#  Objectives:
#  Sources:
#   https://www.dropbox.com/developers/documentation/python?_tk=pilot_lp&_ad=sdk6&_camp=python#tutorial
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
# Creating a folder in dropbox
dbx.files_create_folder_v2("/tempFolder")

###############################################################################
# Getting the modification dates of files
for entry in dbx.files_list_folder('').entries:
    print(entry.name + ": " + str(dbx.files_get_metadata("/1984.txt").server_modified) + "\n")

###############################################################################
# Downloading a file to my computer
dbx.files_download_to_file("../data/extracted/Dropbox/1984.txt", "/1984.txt", rev=None)
