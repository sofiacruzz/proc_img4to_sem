import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('ventanas.jpg', cv2.IMREAD_UNCHANGED) #Carga la imagen sin cambios
img_gris=cv2.imread('ventanas.jpg',cv2.IMREAD_GRAYSCALE)

retval,img_thresh=cv2.threshold(img_gris,100,255,cv2.THRESH_BINARY)
img_reverso = img[:,:,::-1]  #Invierte los colores a BGR a RGB
#img_YCrCb = cv2.cvtColor(img_reverso, cv2.COLOR_RGB2YCrCb)
#img_YUV = cv2.cvtColor(img_reverso, cv2.COLOR_RGB2YUV)  #se declara la 4ta variable

matrix3 = (30,30)#kernel 3x3
matrix1=np.ones(img_reverso.shape)*.8
matrix2=np.ones(img_reverso.shape)*1.5

#img_oscura =np.uint8(cv2.multiply(np.float64(img_reverso),matrix1))
#img_clara=np.uint16(cv2.multiply(np.float64(img_reverso),matrix2))
img_borrosa = cv2.blur(img_reverso, matrix3)


plt.figure(figsize=[10,5])

#         aqui se pone el numero de columnas
plt.subplot(2,2,1);plt.imshow(img);plt.title("Costa original");
plt.subplot(2,2,2);plt.imshow(img_borrosa);plt.title("Costa borrosa");
plt.subplot(2,2,3);plt.imshow(img_gris, cmap='gray');plt.title("Costa oscura");
plt.subplot(2,2,4);plt.imshow(img_thresh, cmap='gray');plt.title("Costa clara");



#plt.imshow(img_YCrCb)
#plt.title('Tigre YCrCb')
plt.show()
