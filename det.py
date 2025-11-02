import cv2
import numpy as np




img=cv2.imread("blob.jpg")
parameter=cv2.SimpleBlobDetector_Params()

#Area Filtering
parameter.filterByArea=True
parameter.minArea=100
#filtering circulairity 
parameter.filterByCircularity=True
parameter.minCircularity=0.9

#Convexity
parameter.filterByConvexity=True
parameter.minConvexity=0.2

# Inertia
parameter.filterByInertia=True
parameter.minInertiaRatio=0.01