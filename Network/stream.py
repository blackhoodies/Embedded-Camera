from flask import Flask, render_template, Response
import cv2
import os
import dropbox
import time
from datetime import datetime

dbx = dropbox.Dropbox('DGcT1g3W1OAAAAAAAAAAFOcZPXq1AqRqnMd3kgYm9VXU_olkb5ahybJK4oFgeTlv')

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


def gen():

    # if os.path.isfile(FILE_OUTPUT):
    #     os.remove(FILE_OUTPUT)

    cap = cv2.VideoCapture(0)

    if (cap.isOpened() == False):
        print("Unable to read camera feed")

    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    fourcc = cv2.VideoWriter_fourcc('X', '2', '6', '4')



    while(True):
        time_start = datetime.now()
        FILE_OUTPUT = time.strftime("%Y_%m_%d_%H_%M.h264")
        out = cv2.VideoWriter(FILE_OUTPUT, fourcc, 10, (frame_width, frame_height))
        c = datetime.now() - time_start
        while (c.total_seconds() < 300):
            c = datetime.now() - time_start
            ret, frame = cap.read()

            if not ret:
                print("Error: failed to capture image")
                break

            # save
            out.write(frame)
            cv2.imwrite('demo.jpg', frame)
            if (cv2.waitKey(1) & 0xFF == ord('q')): break
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + open('demo.jpg', 'rb').read() + b'\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='127.0.0.1')

