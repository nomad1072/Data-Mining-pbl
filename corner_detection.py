import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('Offside1_sift_keypoints.jpg', 0)

fast = cv2.FastFeatureDetector_create()

kp = fast.detect(img, None)
img2 = cv2.drawKeypoints(img, kp, None, color = (255,0,0))

print "Threshold: ", fast.getThreshold()
print "nonmax Suppression: ", fast.getNonmaxSuppression()
print "neighborhood: ",fast.getType()
print "Total keypoints with nonmaxSuppression: ", len(kp)

cv2.imwrite('Offside1_fast_nonmax_enabled.jpg', img2)

fast.setNonmaxSuppression(0)
kp = fast.detect(img, None)

print "Total keypoints without nonmaxSuppression: ", len(kp)

img3 = cv2.drawKeypoints(img, kp ,None, color = (255,0,0))
cv2.imwrite('Offside1_fast_nonmax_disabled.jpg', img3)
