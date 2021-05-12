import cv2
car = cv2.CascadeClassifier("C:\\Users\\HP\\Desktop\\Project Videos\\cars.xml")
bike = cv2.CascadeClassifier("C:\\Users\\HP\\Desktop\\Project Videos\\two.xml")
vid = cv2.VideoCapture("C:\\Users\\HP\\Desktop\\Project Videos\\bikes.mp4")
a = 1
while True:
    a += 1
    check, frame = vid.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cars = car.detectMultiScale(gray, 1.1, 9)
    bikes = bike.detectMultiScale(gray,1.1 , 9)
    for x,y,w,h in cars:
        plate = frame[y:y +h, x:x + w]
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,255,0), 2)
        cv2.rectangle(frame, (x ,y -40), (x+w, y), (255,255,0), -2)
        cv2.putText(frame,'CAR',(x, y -10), cv2.FONT_HERSHEY_PLAIN,1, (255,0,0),3)
        cv2.imshow('car', plate)
    for x,y,w,h in bikes:
        plate = frame[y:y +h, x:x + w]
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,255,0), 2)
        cv2.rectangle(frame, (x ,y -40), (x+w, y), (255,255,0), -2)
        cv2.putText(frame,'BIKES',(x, y -10), cv2.FONT_HERSHEY_PLAIN,2, (255,0,0),2)
        cv2.imshow('car', plate)
    cv2.imshow('cap', frame)
    key = cv2.waitKey(1)
    if key ==ord('q'):
        break
vid.release()
cv2.destroyAllWindows()