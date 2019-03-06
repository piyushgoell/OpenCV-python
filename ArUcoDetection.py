import cv2
import cv2.aruco as aruco

aruco_list = {}
img = cv2.imread('Image2.jpg',1) 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_7X7_1000)
#print(aruco_dict)
parameters = aruco.DetectorParameters_create()
#print(parameters)
corners, ids, _ = aruco.detectMarkers(gray, aruco_dict, parameters = parameters)
#print(corners)
print(ids)
gray = aruco.drawDetectedMarkers(gray, corners,ids)

cv2.imshow('frame',img) 
cv2.waitKey(0)
cv2.destroyAllWindows() 
