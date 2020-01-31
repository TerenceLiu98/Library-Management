import os
import cv2
import urllib
import urllib.request
import json
import os
import pyzbar.pyzbar as pyzbar
from PIL import Image, ImageEnhance
from Code_identify import getcode  # function: getcode
from ISBN_check import GetBookInfo, JsonToCSV
from combine import combineCSV
# import getImageVar from Pic_clarity # function: getImageVar

# get all the barcode's INFO from picture and
getcode()
print("transform isbn code, done!")

GetBookInfo()
print("get books' info, done!")
# Convert JSON to CSV; easy for me to put data in database
JsonToCSV()
print("json to csv, done!")
combineCSV()
print("conbine csv files, Done!")
