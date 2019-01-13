import cv2
import cv2.aruco as aruco

def aruco_generation(id_aruco):
  aruco_dict = aruco.Dictionary_get(aruco.DICT_7X7_1000)
  img = aruco.drawMarker(aruco_dict,id_aruco,num_pixels)
  cv2.imshow('ArUcoID'+str(id_aruco),img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
 
if __name__ == "__main__":
  aruco_generation(78, 500)
  
    
  
  

