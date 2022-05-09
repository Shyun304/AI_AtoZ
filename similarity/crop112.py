import cv2
import dlib #68개의 점으로 얼굴을 인식한다
import os
import tqdm
import numpy as np

# cap = cv2.VideoCapture(0)
# detector = dlib.get_frontal_face_detector()
# predictor = dlib.shape_predictor("shape_predtictor_68_face_landmarks.dat")
# impath = np.fromfile('./downloads/강동원/1.61265_32154_1316.jpg', np.uint8)
# img = cv2.imdecode(impath, cv2.IMREAD_COLOR)
# print(img)
face_detector = dlib.get_frontal_face_detector()
input_dir = "./downloads"

personID = 0
for root, dirs, files in os.walk(input_dir):
    print(root)
    picID = 0
    os.mkdir('data/'+str(personID))
    for file_name in files:
        imgpath = root+ "\\" + file_name

    
        imgpath_numpy = np.fromfile(imgpath, np.uint8)
        img = cv2.imdecode(imgpath_numpy, cv2.IMREAD_COLOR)
        # print(img)
        faces = face_detector(img)

        # outputpath = imgpath.replace('downloads','data')
        # outputpath = outputpath.replace('file_name','crop.jpg')
        outputpath = "./data/"+str(personID)+"/"+str(picID)+'_'
        # print(outputpath)
        for fidx, f in enumerate(faces):
            outputfile = outputpath+str(fidx)+'.jpg'
            try:
                crop = img[f.top():f.bottom(), f.left():f.right()]
                crop = crop.astype(np.uint8)
                
                resized = cv2.resize(crop, (112,112))
                print(resized.shape)
                cv2.imwrite(outputfile,resized)
            except:
                pass
        picID = picID+1
    personID = personID+1

   