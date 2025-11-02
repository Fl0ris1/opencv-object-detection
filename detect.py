import cv2
import numpy as np

img=cv2.imread("blobs.jpg",0)

#set the filtering parameters and initialize the paramiters setting using cv2.simpleblobdetector
params=cv2.SimpleBlobDetector_Params()

#area filtering Areo
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


#create a detector with the parameters
detector=cv2.SimpleBlobDetector_create(params)

#detect blobs
keypoints=detector.detect(img)

#draw blobs as red circles
blank=np.zeros((1,1))
blobs=cv2.drawKeypoints(img,keypoints,blank,(90,34,255),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

#display text on the image
number_of_blobs=len(keypoints)
text=f"There are {number_of_blobs} blobs in the image"
cv2.putText(blobs,text,(20,550),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
#display the final image
cv2.imshow("All blobs",blobs)
cv2.waitKey(0)
cv2.destroyAllWindows()