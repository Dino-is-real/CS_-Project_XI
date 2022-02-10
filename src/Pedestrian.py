import cv2

def run():
    trained_face_data = cv2.CascadeClassifier('../haarcascade/haarcascade_fullbody.xml')

    cap = cv2.VideoCapture("../data/1.mp4") 

    while True:
        ret, img = cap.read()

        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        body_coordinates = trained_face_data.detectMultiScale(gray_img)

        for (x, y, w, h) in body_coordinates:
            cv2.rectangle(img, (x, y), (x + w, y + h + 100), (0, 0, 200), 10)

        cv2.imshow('Lets see', img)
        cv2.waitKey(1)
