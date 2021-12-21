import cv2
import numpy as np
from PIL import Image
import os


class LearnFaceID:
    path = ''
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    def learnImage(id):
        LearnFaceID.path = 'dataset/' + str(id) + '/'
        print(LearnFaceID.path)
        if os.path.isdir(LearnFaceID.path) == False:
            print(LearnFaceID.path)
            return

        print(0)
        path, dirs, files = next(os.walk(LearnFaceID.path))
        file_count = len(files)
        print(file_count)
        if (file_count == 0):
            print(file_count)
            return


        faces, ids = LearnFaceID.getImageAndLabels(id)
        LearnFaceID.recognizer.train(faces, np.array(ids))
        path = "./ymldata"
        os.makedirs(path, exist_ok=True)

        print(file_count)
        fileName = 'ymldata/' + id + '.yml'
        LearnFaceID.recognizer.write(fileName)

    def getImageAndLabels(id):
        imagePaths = [os.path.join(LearnFaceID.path, f) for f in os.listdir(LearnFaceID.path)]
        print(imagePaths)
        faceSamples=[]
        ids = []
        for imagePath in imagePaths:
            PIL_img = Image.open(imagePath).convert('L')  # grayscale로 변환
            img_numpy = np.array(PIL_img, 'uint8')
            file = os.path.basename(imagePath)
            print(file)
            #id = file.split('.')[0]
            id = int(os.path.split(imagePath)[-1].split(".")[1])
            faces = LearnFaceID.detector.detectMultiScale(img_numpy)

            for (x, y, w, h) in faces:
                faceSamples.append(img_numpy[y:y + h, x:x + w])
                ids.append(id)
                print(id)

        return faceSamples, ids
