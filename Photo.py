#coding:utf-8
import cv2
cap = cv2.VideoCapture(0)# Create an object: VideoCapture

flag = 1
num = 1
while(cap.isOpened()):
    ret_flag, Vshow = cap.read()
    cv2.imshow("Capture",Vshow)  # Turn on the Windows, named as 'Capture'
    k = cv2.waitKey(1) & 0xFF # delay 1 frame number
    if k == ord('s'):  # If click ‘s’，print the picture's name, get & save picture
        cv2.imwrite("picture/"+ str(num) + ".jpg", Vshow)
        print(cap.get(3));
        print(cap.get(4));
        print("success to save"+str(num)+".jpg")
        print("-------------------------")
        num += 1
    elif k == ord('q'): #click ‘q’，quit
        break
cap.release() # release camera
