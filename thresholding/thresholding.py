import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import tkinter


img = cv.imread('File422_25.jpg',0)

_,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY);
_,th2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV);
_,th3 = cv.threshold(img,200,255,cv.THRESH_TRUNC);
_,th4 = cv.threshold(th1,127,255,cv.THRESH_TOZERO);

titles = ['original','threshbin','tjresbininv','threshtrunc','threshtozero'];
images = [img,th1,th2,th3,th4]

for i in range(5):
    plt.subplot(2,3,i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])


#cv.imshow("image",img);
#cv.imshow('THRESH_BINARY',th1);
#cv.imshow('THRESH_BINARY_INV',th2);
#cv.imshow('THRESH_TRUNC',th3);
#cv.imshow('THRESH_TOZERO',th4);

#cv.waitKey(0)
#cv.destroyAllWindows()

plt.show()