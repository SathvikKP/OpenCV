import cv2 as cv
import numpy as np

img = cv.imread('sudoku.png',0)

_,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY);
th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2);
th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2);
cv.imshow("image",img);
cv.imshow('THRESH_BINARY',th1);
cv.imshow('Adaptive_Mean_C',th2)
cv.imshow('Adaptive_Guassian_C',th2)

cv.waitKey(0)
cv.destroyAllWindows()