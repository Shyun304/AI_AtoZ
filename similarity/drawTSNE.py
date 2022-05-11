import cv2
from os.path import isfile, join
import numpy as np
import dlib

while(True):
# Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
       break
    img = frame
# Ask the detector to find the bounding boxes of each face. The 1 in the second argument indicates that we should upsample the image 1 #time. This
# will make everything bigger and allow us to detect more faces.
   dets = detector(img, 1)
   print(“Number of faces detected: {}”.format(len(dets)))
# Now process each face we found.
   for k, d in enumerate(dets):
       print(“Detection {}: Left: {} Top: {} Right: {} Bottom:  {}”.format( k, d.left(), d.top(), d.right(), d.bottom()))
 # Get the landmarks/parts for the face in box d.
       shape = sp(img, d)
 # Compute the 128D vector that describes the face in img identified by
 # shape. In general, if two face descriptor vectors have a Euclidean
 # distance between them less than 0.6 then they are from the same
 # person, otherwise they are from different people. Here we just print
 # the vector to the screen.
      features.append(facerec.compute_face_descriptor(img, shape))
      images.append(frame)
cap.release()
cv2.destroyAllWindows()
features = np.array(features) # Converts features array to numpy #array