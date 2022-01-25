import cv2

trained_face_data = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

img = cv2.imread("../data/modi.png")


while True:
    # succesful_frame_read, frame = webcam.read()  # bool , frame

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face_coordinates = trained_face_data.detectMultiScale(gray_img)

    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 5)

    # print(face_coordinates)

    cv2.imshow('Lets see', img)
    cv2.waitKey(1)
