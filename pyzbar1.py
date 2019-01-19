
#importing all libraries
from __future__ import print_function
import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2
import time
def pic_cap():#capturing pictures
  cam = cv2.VideoCapture(1)
  ret, frame = cam.read()
  cv2.imshow("test", frame)
  k = cv2.waitKey(1)
  cam.release()
  return frame



def decode(im) : #function to decode the barcode pictures
  # Find barcodes and QR codes
  decodedObjects = pyzbar.decode(im)
 
  # Print results
  for obj in decodedObjects:
    print('Type : ', obj.type)
    print('Data : ', obj.data,'\n')
     
  return decodedObjects
 
 
# Display barcode and QR code location  
def display(im, decodedObjects):
 
  # Loop over all decoded objects
  for decodedObject in decodedObjects: 
    points = decodedObject.polygon
 
    # If the points do not form a quad, find convex hull
    if len(points) > 4 : 
      hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
      hull = list(map(tuple, np.squeeze(hull)))
    else : 
      hull = points;
     
    # Number of points in the convex hull
    n = len(hull)
 
    # Draw the convex hull
    for j in range(0,n):
      cv2.line(im, hull[j], hull[ (j+1) % n], (255,0,0), 3)
 
  # Display results 
  cv2.imshow("Results", im);
  cv2.waitKey(1)
  time.sleep(4)

def scan_code():
    #show_webcam()
    frame = pic_cap()  
    decodedObjects = decode(frame)
    display(frame, decodedObjects)
scan_code()