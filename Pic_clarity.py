'''
Check whether the picture is clear enough
via image Variance
'''
#coding:utf-8
import cv2

def getImageVar(imgPath):
    image = cv2.imread(imgPath)
    img2gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    imageVar = cv2.Laplacian(img2gray, cv2.CV_64F).var()
    return imageVar

# getImageVar("picture/1.jpg")