import cv2 as cv
import numpy as np

def img_process(fgMask):
    """
    backSub = cv.createBackgroundSubtractorKNN()
    kernel1 = cv.getStructuringElement(shape=cv.MORPH_ELLIPSE, ksize=(2,2))
    kernel2 = cv.getStructuringElement(shape=cv.MORPH_ELLIPSE, ksize=(2,2))
    #kernel1 = np.ones((3,3),np.uint8)
    #kernel2 = np.ones((3,3), np.uint8)

    fgMask = cv.threshold(fgMask, 100, 255, cv.THRESH_BINARY)[1]
    fgMask = cv.morphologyEx(fgMask, cv.MORPH_OPEN, kernel1,iterations = 3)
    fgMask = cv.dilate(fgMask, kernel2, iterations = 2)
    fgMask = cv.morphologyEx(fgMask, cv.MORPH_CLOSE, kernel2, iterations = 13)
    """
    backSub = cv.createBackgroundSubtractorKNN()
    kernel1 = cv.getStructuringElement(shape=cv.MORPH_ELLIPSE, ksize=(2,2))
    kernel2 = cv.getStructuringElement(shape=cv.MORPH_ELLIPSE, ksize=(2,2))
    #kernel1 = np.ones((3,3),np.uint8)
    #kernel2 = np.ones((3,3), np.uint8)

    fgMask = cv.threshold(fgMask, 230, 255, cv.THRESH_BINARY)[1]
    fgMask = cv.morphologyEx(fgMask, cv.MORPH_OPEN, kernel1,iterations = 2)
    fgMask = cv.dilate(fgMask, kernel2, iterations = 2)
    fgMask = cv.morphologyEx(fgMask, cv.MORPH_CLOSE, kernel2, iterations = 2)
    return fgMask

def find_ellipse(fgMask):

    eList = []
    contours,hierarchy = cv.findContours(fgMask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    for c in contours:
        if (len(c) >= 5):
                ellipse = cv.fitEllipse(c)
                if (ellipse[1][1] > 100 and ellipse[1][0] > 20):
                    eList.append(ellipse)

                #frame = cv.ellipse(frame,ellipse,(255,255,0),2)

    return eList

def extract_features(prev_rect, prev_ellipse, current_rect, current_ellipse):
    angle = current[2]
    ratio = float(current[1][0])/current[1][1]
    if (previous is None):
        velocity = 0.0

    prev_ratio = float(previous[1][0])/previous[1][1]

    velocity = ratio - prev_ratio

    return [angle, ratio, velocity]

count = 0

def draw_flow(img, flow, step=16):
    h, w = img.shape[:2]
    y, x = np.mgrid[int(step/2):h:step, int(step/2):w:step].reshape(2,-1)
    fx, fy = flow[y,x].T
    lines = np.vstack([x,y,x+fx,y+fy]).T.reshape(-1,2,2)
    lines = np.int32(lines + 0.5)
    #vis = cv.cvtColor(img, cv.COLOR_GRAY2BGR)

    cv.polylines(img, lines, 0, (0,255,0))
    for (x1,y1), (x2,y2) in lines:
        cv.circle(img, (x1,y1), 1, (0,255,0),-1)
    return img   

def draw_hsv(flow):
    h, w = flow.shape[:2]
    fx, fy = flow[:,:,0], flow[:,:,1]
    ang = np.arctan2(fy,fx) + np.pi
    v = np.sqrt(fx*fx+fy*fy)
    hsv = np.zeros((h,w,3), np.uint8)
    hsv[...,0] = ang*(180/np.pi/2)
    hsv[...,1] = 255
    hsv[...,2] = np.minimum(v*4, 255)
    bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
    return bgr

def warp_flow(img, flow):
    h, w = flow.shape[:2]
    flow = -flow
    flow[:,:,0] += np.arange(w)
    flow[:,:,1] += np.arange(h)[:, np.newaxis]
    res =cv.remap(img, flow, None, cv.INTER_LINEAR)
    return res
