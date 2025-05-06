import cv2
import matplotlib.pyplot as plt
import numpy as np

# Carrega a imagem em escala de cinza
imagem = cv2.imread('img/projeto2/circulos_1.png')
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

kernel = np.ones((5,5),np.uint8)
# Suaviza a imagem para reduzir ruído
imagem_suavizada = cv2.medianBlur(imagem_cinza, 5)
plt.imshow(imagem_suavizada)

# Detecta círculos usando a Transformada de Hough
circulos = cv2.HoughCircles(
    imagem_suavizada,
    cv2.HOUGH_GRADIENT,
    dp=1.0,              # precisão da resolução (ajuste conforme necessário)
    minDist=50,          # distância mínima entre centros dos círculos
    param1=100,           # limiar superior para o detector de bordas Canny
    param2=40,           # limiar para o centro do círculo
    minRadius=50,         # raio mínimo
    maxRadius=100        # raio máximo
)

# Se foram encontrados círculos
if circulos is not None:
    circulos = np.uint16(np.around(circulos))
    cimg = imagem.copy()
    for i in circulos[0,:]:
        # draw the outer circle
        cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv2.circle(cimg,(i[0],i[1]),2,(255,0,0),10)
        # Exibe contagem
        print(f'Foram detectados {len(circulos[0])} círculos.')

    # Exibe a imagem com os círculos
    plt.imshow(cimg)
else:
    print('Nenhum círculo detectado.')
plt.show()