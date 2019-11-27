import cv2 as cv
from utilities import img_process, find_ellipse, draw_flow, draw_hsv
import numpy as np
from centroidtracker1 import CentroidTracker1
from centroidtracker2 import CentroidTracker2
import pickle

cap = cv.VideoCapture("video2.mov")
svm_model = pickle.load(open('model.sav', 'rb'))
isFall = False

if (cap.isOpened() == False):
    print("Error opening video stream or file")

ct1 = CentroidTracker1()
ct2 = CentroidTracker2()

backSub = cv.createBackgroundSubtractorKNN()
ret, prev_frame = cap.read()
prev_frame2 = cv.cvtColor(prev_frame, cv.COLOR_BGR2GRAY)
prev_fgMask = backSub.apply(prev_frame2, None, -1)
prev_fgMask = img_process(prev_fgMask)
data = [0,0,0]
while(cap.isOpened()):
    ret, frame = cap.read()
    if (ret == True):
        frame2 = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        fgMask = backSub.apply(frame2, None, -1)

        fgMask = img_process(fgMask)
        flow = cv.calcOpticalFlowFarneback(prev_fgMask, fgMask, None, 0.5, 5, 5, 5, 5, 1.1, cv.OPTFLOW_FARNEBACK_GAUSSIAN)
        prev_fgMask = fgMask
        """
        eList = find_ellipse(fgMask)

        for e in eList:
            frame = cv.ellipse(frame, e, (255,255,0), 2)
        """
        gray_hsv = cv.cvtColor(draw_hsv(flow), cv.COLOR_BGR2GRAY)
        thresh = cv.threshold(gray_hsv, 3, 255, cv.THRESH_BINARY)[1]
        thresh = cv.dilate(thresh, cv.getStructuringElement(shape=cv.MORPH_ELLIPSE, ksize=(3,3)), iterations=3)
        thresh = cv.morphologyEx(thresh, cv.MORPH_CLOSE, cv.getStructuringElement(shape=cv.MORPH_ELLIPSE, ksize=(3,3)), iterations = 25)
        (cnts, _) = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        rects = []
        ellipses = []

        current_ratio = 0.0
        for c in cnts:
            if (len(c) >= 5):
                (x, y, w, h) = cv.boundingRect(c)
                ellipse = cv.fitEllipse(c)
                #w>50 and h>100 and w<100 and h<340
                if (w>20 and h>20 and w*h >1200 and ellipse[1][1] > 90 and ellipse[1][0] > 20):
                    cv.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 1)
                    rects.append(np.array([x,y, x+w, y+w]))
                    cv.ellipse(frame,ellipse,(255,255,0),1)
                    ellipses.append(ellipse)
                    #data = np.vstack((data, [ellipse[2], float(w)/h, float(w)/h - current_ratio]))
                    current_ratio = float(w)/h
                    #print(svm_model.predict([[ellipse[2], float(w)/h, float(w)/h - current_ratio]]))
                    if (svm_model.predict([[ellipse[2], float(w)/h, float(w)/h - current_ratio]]) == 1):
                        cv.putText(frame, "Normal", (10, 10), cv.FONT_HERSHEY_PLAIN, 1.0, (0,255,0), 2);
                    else:
                        cv.putText(frame, "Fall", (10, 10), cv.FONT_HERSHEY_PLAIN, 1.0, (0,0,255), 2);

        #np.savetxt("normal_3.txt", data)
        objs1 = ct1.update(rects)
        objs2 = ct2.update(rects)

        for (objectID, centroid) in objs1.items():

            text = "ID {}".format(objectID)
            cv.putText(frame,text,(centroid[0]-10, centroid[1]-10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0),1)
            cv.circle(frame, (centroid[0], centroid[1]), 1, (0,255,0),-1)


        cv.imshow("frame", frame)

        if cv.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break


cap.release()
