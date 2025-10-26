import cv2
import numpy as np

img=cv2.imread("blobs.jpg",0)

#set the filtering parameters and initialize the paramiters setting using cv2.simpleblobdetector
params=cv2.SimpleBlobDetector_Params()

#area filtering
params.filterByArea=True
params.minArea=100
#filtering by circulairity
params.filterByCircularity=True
params.minCircularity=0.9

#filtering by Convexity
params.filterByConvexity=True
params.minConvexity=0.2

#filtering by Inertia
params.filterByInertia=True
params.minInertiaRatio=0.01