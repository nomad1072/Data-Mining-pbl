import cv2
import numpy as numpy

img = cv2.imread('Offside1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()

(kps, descs) = sift.detectAndCompute(gray, None)
print ("# kps: {}, descriptors: {}".format(len(kps), descs.shape))


img = cv2.drawKeypoints(gray, kps, img)
cv2.imwrite('Offside1_sift_keypoints.jpg',img)

cv2.imshow('Offside1_sift_keypoints.jpg', img)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)
matches = bf.match(des1, de)