'''
To get ISBN and

'''
import urllib
import urllib.request
import json
import pandas as pd
import os
import isbnlib
from isbnlib import ISBNLibException
from isbnlib.dev import NoDataForSelectorError

def GetBookInfo(isbn):
        # url = 'https://api.douban.com/v2/book/isbn/' + isbn
        # douban has a very strict policy to check  web crawler
        # therefore, we change to 'https://www.98api.cn/api/isbn.php'
    url = 'https://www.98api.cn/api/isbn.php?isbn=' + isbn
    # https://www.googleapis.com/books/v1/volumes?q=isbn:<ISBN>
    # use urllib to open url
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    # read html from response and decode with 'utf-8'
    result = response.read().decode('utf8')
    # json
    result_json = json.loads(result)
    result = json.dumps(result_json, sort_keys = True, indent = 4, separators = (',', ':'))
    #file_title = str(json.loads(json.dumps(result_json)).get('title'))
    #df  = pd.DataFrame.from_dict(result_json)
    #df.to_csv("Data/"+file_title+".csv", encoding='utf-8')
    #return result_json
    #a = json.dumps(result_json)
        # 信息获取失败，抛出一个异常

    # If you want different book INFO in different file you can use this to find book_name
    file_title = str(json.loads(json.dumps(result_json)).get('title'))
    file = open("Data/JSON/" + file_title + '.json', 'w')
    file.write(result)
    file.close()
'''
def GetBookInfo():
    f = open("code.txt")
    data = []
    with open('code.txt', 'r') as f:
        for line in f.readlines():
            line = line.strip('\n')
            data.append(line)

    for i in range(len(data)):
        try:
            book = isbnlib.meta(data[i])
            book_name = book['Title']
            file = open("Data/JSON/" + book_name + '.json', 'w')
            file.write(json.dumps(book))
            file.close()
        except KeyError:
            pass
        continue
'''
def JsonToCSV():
    path = "Data/JSON/"
    name = os.listdir(path)
    for i in range(len(name)):
        df = pd.read_json(path + str(name[i]))
        df.to_csv("Data/CSV/" + str(name[i].replace(".json", "")) + ".csv", encoding='utf-8', index = False)




# main
f = open("code.txt")
data = []
with open('code.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip('\n')
        data.append(line)

for i in range(len(data)):
    GetBookInfo(data[i])

JsonToCSV()