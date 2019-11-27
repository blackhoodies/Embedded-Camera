import time
from datetime import datetime
import dropbox
import os

folder = "/home/pi/Video"

def uploadvid(file_name):
    # FILE_OUTPUT = datetime.now().strftime("%Y_%m_%d_%H_%M.h264")
    # dbx = dropbox.Dropbox('DGcT1g3W1OAAAAAAAAAAFOcZPXq1AqRqnMd3kgYm9VXU_olkb5ahybJK4oFgeTlv ')
    with open(file_name, 'rb') as f:
        file = f.read()
    res = dbx.files_upload(file, '/video/' + file_name)
    os.remove(file_name)
    print("%s has been removed successfully" % file)


while(True):
    dbx = dropbox.Dropbox('DGcT1g3W1OAAAAAAAAAAFOcZPXq1AqRqnMd3kgYm9VXU_olkb5ahybJK4oFgeTlv ')
    list = os.listdir(folder)
    for file in list:
        if (file.endswith(".h264")):
            uploadvid(file)

