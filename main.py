import os
import cv2
import urllib
import urllib.request
import json
import os
import pyzbar.pyzbar as pyzbar
from PIL import Image,ImageEnhance
from ISBN_check import getInfoFromDouban

#import getImageVar from Pic_clarity # function: getImageVar
from Code_identify import getcode # function: getcode

# get all the barcode's INFO from picture and
getcode()

# get books' INFO via ISBN comparison
f = open("code.txt")
data = []
with open('code.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip('\n')
        data.append(line)

for i in range(len(data)):
    getInfoFromDouban(data[i])


