#!/usr/local/bin/python3
import cv2
import copy as cp
import numpy as np

def invertColor(img):
    return 255 - img

def colorDodge(img, img2):
    ret = cp.deepcopy(img)
    for i in range(len(ret)):
        for j in range(len(ret[0])):
            a = int(ret[i][j])
            b = int(img2[i][j])
            if b == 255: 
                ret[i][j] = np.unit8(255)
            else:
                ret[i][j] = np.uint8(min(255, (a << 8) / (255-b)))
    return ret

def sketchImage(img, ksize = (7, 7), sigmaX = 2., sigmaY = 2., h = 30, templateWindowSize = 7, searchWindowSize = 21):
    ivt = invertColor(img)
    blur = cv2.GaussianBlur(ivt, ksize=ksize, sigmaX = sigmaX, sigmaY = sigmaY)
    # blur = cv2.fastNlMeansDenoising(blur, h = h, templateWindowSize= templateWindowSize, searchWindowSize= searchWindowSize)
    return colorDodge(img, blur)

img = cv2.imread('samples/miku.png', 0)
# img = cv2.resize(src = img, dsize = (0, 0), fx = 0.5, fy = 0.5)
res = sketchImage(img)
cv2.imshow('sketched', res)
cv2.waitKey(0)
