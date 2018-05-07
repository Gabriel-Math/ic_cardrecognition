import cv2
import numpy as np

img = cv2.imread('IC_CARD.png', cv2.IMREAD_COLOR)

# cv2.line(img, (0,0), (150, 150), (255,255,255), 15)
# DESENHA UMA LINHA NA TELA

# cv2.rectangle(img, (15,25),(200,150), (0,255,0), 5)
# DESENHA UM RETANGULO NA TELA

# cv2.circle(img, (100,63), 55, (0,0,255), -1)
# DESENHA UM CIRCULO NA TELA

# pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
# CRIA PONTOS

# cv2.polylines(img, [pts], True, (0,255,255), 3)
# MOSTRA OS PONTOS E CONECTA ELES

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'IC Teste', (0,130), font, 1, (200,255,255), 2, cv2.LINE_AA)
# ESCREVE NA TELA

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
