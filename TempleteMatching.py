import cv2
import numpy as np

#Load input image
img = cv2.imread('Images/Image1.jpg')
#Convert it to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Load templete image
template = cv2.imread('Images/template.jpg',0)

cv2.imshow('Result',template)
#Get the shape of the template image
w, h = template.shape[::-1]

# All the 6 methods for comparison in a list
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR','cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

# Apply template Matching
result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# Creating Boundary Box
top_left = max_loc
bottom_right = (top_left[0] +w, top_left[1] + h)
cv2.rectangle(img, top_left,bottom_right, (0,0,255), 2)

cv2.imshow('Result',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
