import cv2
import dlib #68개의 점으로 얼굴을 인식한다

cap = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")


face_detector = dlib.get_frontal_face_detector()
img = cv2.imread("test.jpg")
faces = face_detector(img)

for f in faces:
    crop = img[f.top():f.bottom(), f.left():f.right()]
    cv2.imwrite("cropped.jpg",crop)