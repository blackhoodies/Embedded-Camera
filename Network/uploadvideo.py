import dropbox

dbx = dropbox.Dropbox('DGcT1g3W1OAAAAAAAAAAFOcZPXq1AqRqnMd3kgYm9VXU_olkb5ahybJK4oFgeTlv')

with open('namevideo.mp4', 'rb') as f:
        data = f.read()

res = dbx.files_upload(data, '/video.mp4')

