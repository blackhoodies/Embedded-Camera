import time
from datetime import datetime
import dropbox
import os


folder = '/video'

while(True):
    dbx = dropbox.Dropbox('DGcT1g3W1OAAAAAAAAAAFOcZPXq1AqRqnMd3kgYm9VXU_olkb5ahybJK4oFgeTlv ')

    list = dbx.files_list_folder(folder)

    for file in list.entries:
        if isinstance(file, dropbox.files.FileMetadata):
            day = datetime.now().minute - file.server_modified.minute
            if (day >= 3):
                dbx.files_delete(folder+'/'+file.name)


