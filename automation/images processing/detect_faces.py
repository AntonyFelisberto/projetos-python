#pip install opencv-python
import cv2

image = cv2.imread("humans.jpeg",1)
face_cascade = cv2.CascadeClassifier("faces.xml")

faces = face_cascade.detectMultiScale(image, 1.1, 4)
print(faces)

for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,255),4)

cv2.imwrite("humanFaces.jpeg",image)