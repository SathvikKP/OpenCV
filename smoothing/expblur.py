import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('kan.jpg')
img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
_,th1 = cv2.threshold(img1,3,255,cv2.THRESH_BINARY);
_,img = cv2.threshold(th1,3,255,cv2.THRESH_TOZERO);


kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)
blur=cv2.blur(img,(5,5))
gblur = cv2.GaussianBlur(img,(5,5),0)
_,gblurv2 = cv2.threshold(gblur,107,255,cv2.THRESH_TOZERO);
median = cv2.medianBlur(gblur,5)
_,final = cv2.threshold(median,10,255,cv2.THRESH_TOZERO);
medianv2 = cv2.medianBlur(final,1)

titles = ['image','2dconvolution','blur','gblur','gblurv2','median','final','medianv2','orig']
images = [img,dst,blur,gblur,gblurv2,median,final,medianv2,img1]

for i in range(9):
    plt.subplot(3,3,i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()