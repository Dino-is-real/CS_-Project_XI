import cv2

trained_face_data = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')

cap = cv2.VideoCapture("pedestrian.mp4")


while True:
    # succesful_frame_read, frame = webcam.read()  # bool , frame
    ret, img = cap.read()

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face_coordinates = trained_face_data.detectMultiScale(gray_img)

    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(img, (x, y), (x + w, y + h + 100), (0, 0, 200), 2)

    # print(face_coordinates)

    cv2.imshow('Lets see', img)
    cv2.waitKey(1)