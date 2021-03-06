import cv2
import numpy as np

cap = cv2.VideoCapture('pwv.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()

# PEGA TUDO QUE ESTA EM MOVIMENTO E RETIRA BACKGROUND
while True:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)

    cv2.imshow('original', frame)
    cv2.imshow('fg', fgmask)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
