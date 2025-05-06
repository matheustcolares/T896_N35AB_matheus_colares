import cv2
import numpy as np
import matplotlib.pyplot as plt

imagem_com_fundo_verde = cv2.imread('img/projeto1/img_fundo_verde_3.png')
novo_fundo = cv2.imread('img/projeto1/background_1.png')

novo_fundo = cv2.resize(novo_fundo, (imagem_com_fundo_verde.shape[1], imagem_com_fundo_verde.shape[0]))

hsv = cv2.cvtColor(imagem_com_fundo_verde, cv2.COLOR_BGR2HSV)

limite_inferior = np.array([35, 40, 40])    
limite_superior = np.array([85, 255, 255])

mascara_verde = cv2.inRange(hsv, limite_inferior, limite_superior)

mascara_invertida = cv2.bitwise_not(mascara_verde)

pessoa = cv2.bitwise_and(imagem_com_fundo_verde, imagem_com_fundo_verde, mask=mascara_invertida)

fundo = cv2.bitwise_and(novo_fundo, novo_fundo, mask=mascara_verde)

resultado = cv2.add(pessoa, fundo)

resultado = cv2.cvtColor(resultado, cv2.COLOR_BGR2RGB)

plt.imshow(resultado,cmap='grey')
plt.show()
