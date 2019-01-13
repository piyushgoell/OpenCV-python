##################################################################################################################################
######################    Python code for Generating any ArUco Id of any Dictionary    ###########################################
##################################################################################################################################

import cv2
import cv2.aruco as aruco

##################################################################################################################################
###############################         Function for Generating ArucoID         ##################################################
##################################################################################################################################

def aruco_generation(id_aruco, num_pixels):
  	'''
	ArUco ID Dictionaries: 
  	7X7 = 7-bit pixel, 
  	7X7_1000 = 1000 combinations of 7-bit pixel image
	**************************************************************************
  	List of Dictionaries in OpenCV's ArUco library:
	DICT_4X4_50	 
	DICT_4X4_100	 
	DICT_4X4_250	 
	DICT_4X4_1000	 
	DICT_5X5_50	 
	DICT_5X5_100	 
	DICT_5X5_250	 
	DICT_5X5_1000	 
	DICT_6X6_50	 
	DICT_6X6_100	 
	DICT_6X6_250	 
	DICT_6X6_1000	 
	DICT_7X7_50	 
	DICT_7X7_100	 
	DICT_7X7_250	 
	DICT_7X7_1000	 
	DICT_ARUCO_ORIGINAL
	DICT_APRILTAG_16h5, 
 	DICT_APRILTAG_25h9, 
	DICT_APRILTAG_36h10, 
	DICT_APRILTAG_36h11
  	**************************************************************************
	'''
	# This function returns one of the predefined dictionaries referenced by DICT_*
	# aruco.Dictionary_get(Dictionary)
 	# Change as per the requirement (aruco.DICT_NxN_Combinations) for generating Aruco Id's of Different Dictionaries
  	aruco_dict = aruco.Dictionary_get(aruco.DICT_7X7_1000)      
  
  	# This fuction is used to Draw the Aruco ID's of specific Dictionary. 
  	# aruco.drawMarker(Dictionary, Aruco id, sidePixels[, _img[, borderBits]])
  	img = aruco.drawMarker(aruco_dict,id_aruco,num_pixels)
  
  	# This function is used to convert the image from GRAY to RGB
  	# cv2.cvtColor(Image,color space conversion code)
  	img = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
  
  	# This function is used to put extra padding to the image. 
  	# cv2.copyMakeBorder(Image, Top, Bottom, Left, Right, borderType, borderColor)
  	img = cv2.copyMakeBorder(img, 50, 50, 50, 50, cv2.BORDER_CONSTANT,value=[255,255,255])
  
  	# This function is used to put text on the image.
	# cv2.putText(Image , Text, Origin, fontFace, fontScale, color, thickness, lineType, bottomLeftOrigin)
  	cv2.putText(img, "ArUco ID = "+str(id_aruco),(180,40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
  
  	# This function is used to display image in specified window on the screen.
  	# cv2.imshow('windowName',Image)
  	cv2.imshow('ArUcoID'+str(id_aruco),img)
  
  	# This function is used to save the image in JPG format in the working directory.
  	# cv2.imwrite('file name',Image)
  	cv2.imwrite('ArUco'+str(id_aruco)+'.jpg',img)
  
  	#This function is used to hold the program for indefinitely for a key stroke
  	cv2.waitKey(0)
  
  	# This function is used to simply destroys all the windows we created
  	cv2.destroyAllWindows() 
  
##################################################################################################################################
#################################          Main Function            ##############################################################
################################################################################################################################## 
if __name__ == "__main__":
  	'''
  	For generating ArUco Id's of Differnet Dictionaries 
  	There is a slight change in the line no. 45 as per the requirement
  	for example:- if you want to generate Aruco ID of 5x5_250 Dictonary
  	you need to edit aruco.DICT_7x7_1000 to aruco.DICT_5x5_250
  	'''
  	# This is a function calling statement aruco_generation(ArUco ID, size of image in pixels)
  	aruco_generation(78, 500)
  	aruco_generation(54, 800)
  
    
  
  

