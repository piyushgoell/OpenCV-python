import cv2
import cv2.aruco as aruco

def aruco_generation(id_aruco, num_pixels):
  aruco_dict = aruco.Dictionary_get(aruco.DICT_7X7_1000)
  img = aruco.drawMarker(aruco_dict,id_aruco,num_pixels)
  img = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
  img = cv2.copyMakeBorder(img, 50, 50, 50, 50, cv2.BORDER_CONSTANT,value=[255,255,255])
  cv2.putText(img, "ArUco ID = "+str(id_aruco),(180,40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
  cv2.imshow('ArUcoID'+str(id_aruco),img)
  cv2.imwrite('ArUco'+str(id_aruco)+'.jpg',img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
 
if __name__ == "__main__":
  aruco_generation(78, 500)
  
    
  
  

