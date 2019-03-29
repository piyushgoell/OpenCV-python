##################################################################################################################################
######################    Python code for Detecting any ArUco Id of any Dictionary    ###########################################
##################################################################################################################################

import cv2
import cv2.aruco as aruco

##################################################################################################################################
###############################         Function for Detecting ArucoID         ##################################################
##################################################################################################################################
def aruco_detection(img):
  
  # Creating a empty list to store the values 
  aruco_list = {}
  
  # Conterting Image to GRAYSCALE
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  
  # This function returns one of the predefined dictionaries referenced by DICT_*
  # aruco.Dictionary_get(Dictionary)
  # Change as per the requirement (aruco.DICT_NxN_Combinations) for generating Aruco Id's of Different Dictionaries
  aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_7X7_1000)

  # This Function performs marker detection in the input image. 
  # Only markers included in the dictionary specificed above are searched.
  corners, ids, _ = aruco.detectMarkers(gray, aruco_dict)
  print(ids)
  # This function returns a marker image in its canonical form (i.e. ready to be printed)
  aruco.drawDetectedMarkers( img, corners, ids)
  
  # Displaying the Result
  cv2.imshow('frame',img)

  
if __name__ == "__main__":
# Reading the image  
  img = cv2.imread('Images/ArUco.jpg',1) 
  aruco_detection(img)
  cv2.waitKey(0)
  cv2.destroyAllWindows() 
