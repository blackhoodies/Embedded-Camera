import dropbox 
import time
dbx = dropbox.Dropbox('

with open('tesa.mp4','rb') as f:
	data = f.read()
res = dbx.files_upload(data, '/a/tesa.mp4')
time.sleep(300)
dbx.files_delete('/a/tesa.mp4')

