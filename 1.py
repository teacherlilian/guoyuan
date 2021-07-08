import cv2 as cv
import math

cap = cv.VideoCapture(0)
ret, frame0 = cap.read()
num = 0

while True:

    ret, frame = cap.read()
    num += 1
    # weight is swinging between 0 and 1

    weight = math.fabs(math.sin(num % 360 / 360 * 2 * 3.14159))
    blend = cv.addWeighted(frame, weight, frame0, 1.0 - weight, 0)

    cv.imshow("video frame", blend)
    if cv.waitKey(1) & 0xFF == ord('q'):  # exit when 'q' is pressed
        break

cap.release()
cv.destroyAllWindows()