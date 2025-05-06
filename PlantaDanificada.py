import cv2
import matplotlib.pyplot as plt
import numpy as np

# Carrega a imagem
imagem = cv2.imread('img/projeto3/img_folha_4.JPG')
imagem_hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

# Intervalo para cor verde (saudável)
verde_inf = np.array([35, 40, 40])
verde_sup = np.array([85, 255, 255])
mascara_verde = cv2.inRange(imagem_hsv, verde_inf, verde_sup)

# Intervalo para cores danificadas (amarelo/marrom/escuro)
danos_inf = np.array([10, 50, 20])
danos_sup = np.array([30, 255, 255])
mascara_dano = cv2.inRange(imagem_hsv, danos_inf, danos_sup)

# Aplica operações morfológicas para limpar ruídos
kernel = np.ones((5, 5), np.uint8)
mascara_verde = cv2.morphologyEx(mascara_verde, cv2.MORPH_OPEN, kernel)
mascara_dano = cv2.morphologyEx(mascara_dano, cv2.MORPH_OPEN, kernel)

# Cria imagens segmentadas
folha_saudavel = cv2.bitwise_and(imagem, imagem, mask=mascara_verde)
folha_danificada = cv2.bitwise_and(imagem, imagem, mask=mascara_dano)

# Combina as regiões com cores destacadas
resultado = imagem.copy()
resultado[mascara_verde > 0] = [0, 255, 0]      # verde brilhante para saudável
resultado[mascara_dano > 0] = [0, 0, 255]       # vermelho para danificado

# Exibe os resultados
plt.subplot(3,2,1)
plt.title("Original")
plt.imshow( imagem)
plt.subplot(2,2,2)
plt.title("Saudável")
plt.imshow( folha_saudavel)
plt.subplot(2,2,3)
plt.title("Danificada")
plt.imshow( folha_danificada)
plt.subplot(2,2,4)
plt.title("Resultado Final")
plt.imshow( resultado)
plt.show()