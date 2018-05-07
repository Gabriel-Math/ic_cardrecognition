import cv2
import numpy as np

img = cv2.imread('IC_CARD.png', cv2.IMREAD_COLOR)

# img[55,55] = [255,255,255] # CONVERTE UM PIXEL(COR)
# px = img[55,55] # PEGA O PIXEL
# print(px)

# img[100:150, 100:150] = [255,255,255] # CONVERTE UMA REGIAO(COR)
# roi = img[100:150, 100:150] # PEGA TODOS OS PIXELS EM UMA REGIAO

# watch_face = img[37:111, 107:194] # COPIA
# img[0:74, 0:87] = watch_face # COLA


cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
