import cv2
import os
from PIL import Image

class DetectFaceID:

    cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    file_count = 0;

    def ReadVideoFile(filePath, id):
        cam = cv2.VideoCapture(filePath)
        DetectFaceID.file_count = len([name for name in os.listdir('dataset/' + str(id) + '/') if os.path.isfile(name)])
        if(DetectFaceID.file_count < 11):
            DetectFaceID.videoDetector(cam, id)

    def ReadImageFile(img, id):
        height, width, channels = img.shape
        DetectFaceID.file_count = len([name for name in os.listdir('dataset/' + str(id) + '/') if os.path.isfile(name)])
        if(DetectFaceID.file_count < 11):
            DetectFaceID.imageDetctor(img, id)

    def videoDetector(cam, id):
        while True:
            img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = DetectFaceID.cascade.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                DetectFaceID.file_count += 1
                cv2.imwrite("dataset/" + str(id) + '/' + 'User.' + str(face_id) + '.' + str(DetectFaceID.file_count) + ".jpg", gray[y:y + h, x:x + w])
                cv2.imshow('image', img)
            k = cv2.waitKey(100) & 0xff
            if k == 27:
                break
            elif DetectFaceID.file_count >= 10:
                break

    def imageDetctor(img, id):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = DetectFaceID.cascade.detectMultiScale(gray, 1.3, 5)
        path = "./dataset/" + str(id)
        os.makedirs(path, exist_ok=True)
        path, dirs, files = next(os.walk(path))
        DetectFaceID.file_count = len(files)
        if(DetectFaceID.file_count < 11):
            for (x, y, w, h) in faces:
                DetectFaceID.file_count += 1
                cv2.imwrite("dataset/" + str(id) + '/' + 'User.' + str(face_id) + '.' + str(DetectFaceID.file_count) + ".jpg", gray[y:y + h, x:x + w])

        return img

    def imageShower(img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = DetectFaceID.cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        return img

