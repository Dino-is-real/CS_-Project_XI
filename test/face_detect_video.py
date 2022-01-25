import cv2

video = cv2.VideoCapture("k.mp4")
trained_face_data =cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while 1:
    ret , img = video.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    rects = trained_face_data.detectMultiScale(gray, scaleFactor=1.2,minNeighbors=3)

    for (x,y,w,h) in rects:
       cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow("ok",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
