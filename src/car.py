import cv2

trained_face_data = cv2.CascadeClassifier('../haarcascade/haarcascade_car.xml')

cap= cv2.VideoCapture("../data/dataset_video1.avi")

while True:
    ret, frames = cap.read()
    if not ret:
        exit()
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    cars = trained_face_data.detectMultiScale( gray, 1.1, 1)
    for (x,y,w,h) in cars:
        cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.imshow('K boi', frames)
    if cv2.waitKey(33) == 13:
        break

cv2.destroyAllWindows()
