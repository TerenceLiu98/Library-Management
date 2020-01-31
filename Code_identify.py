import os
import pyzbar.pyzbar as pyzbar
from PIL import Image,ImageEnhance

def getcode():
    image_path = "picture/"
    img_name = os.listdir(image_path)
    for i in range(len(img_name)):
        img = Image.open(image_path + img_name[i])
        #处理图片
        #img = ImageEnhance.Brightness(img).enhance(2.0)#增加亮度
        #img = ImageEnhance.Sharpness(img).enhance(17.0)#锐利化
        #img = ImageEnhance.Contrast(img).enhance(4.0)#增加对比度
        #img = img.convert('L')#灰度化
        #显示原图,调用系统默认的图片显示器
        #img.show()
        texts = pyzbar.decode(img)
        # print(texts)
        #输出结果
        for text in texts:
            tt = text.data.decode("utf-8")
            # print(tt)
            f = open('code.txt', 'a')
            f.write(str(tt)+"\n")
            f.close()

# getcode()