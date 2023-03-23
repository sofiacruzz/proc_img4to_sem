import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('Tigre.jpg',cv2.IMREAD_COLOR)
#cv2.rectangle(img,(27,0),(56,28),(0,0,0),-1)
#cv2.rectangle(img,(27,56),(56,84),(0,0,0),-1)
#cv2.rectangle(img,(0,25),(27,54),(255,255,255),-1)
#cv2.rectangle(img,(56,25),(84,54),(255,255,255),-1)
#cv2.imshow('mi primera imagen',img)
#cv2.imwrite('Tigre_gris.jpg',img)
#num_rows, num_cols=img.shape[:2]
#rotation_matrix = cv2.getRotationMatrix2D((num_cols/2,num_rows/2),-180,1)
#translation_matrix=np.float32([[-1,0,960],[0,1,0]])
#print(translation_matrix)
img_reverso=img[:,:,::-1]
img_yuv=cv2.cvtColor(img_reverso,cv2.COLOR_BGR2YUV)
plt.imshow(img_yuv)
plt.title('tigre tono original')
plt.show()
#img2=cv2.warpAffine(img,translation_matrix,(num_cols,num_rows))
#img3=cv2.warpAffine(img2,rotation_matrix,(num_cols,num_rows))
#img=cv2.rotate(img,cv2.ROTATE_45_CLOCKWISE)

#img4=cv2.resize(img3, None, fx=0.5,fy=0.5,interpolation=cv2.INTER_LINEAR)
#cv2.imshow('tigre con todas las transformaciones',img4)
#cv2.imwrite('Tigre_final.jpg',img4)

#print(img.shape)
#print(type(img))
#print(img.size)
#print(img)



cv2.waitKey(0)
