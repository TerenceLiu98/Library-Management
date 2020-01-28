'''
To get ISBN and

'''
import urllib
import urllib.request
import json
import os

def getInfoFromDouban(isbn):
        # url = 'https://api.douban.com/v2/book/isbn/' + isbn
        # douban has a very strict policy to check  web crawler
        # therefore, we change to 'https://www.98api.cn/api/isbn.php'
    url = 'https://www.98api.cn/api/isbn.php?isbn=' + isbn
    # use urllib to open url
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    # read html from response and decode with 'utf-8'
    result = response.read().decode('utf8')
    # json
    result_json = json.loads(result)
    a = json.dumps(result_json)
        # 信息获取失败，抛出一个异常

    # If you want different book INFO in different file you can use this to find book_name
    file_title = str(json.loads(json.dumps(result_json)).get('title'))
    file = open("Data/"+ file_title + '.json', 'w')
    file.write(a)
    file.close()



f = open("code.txt")
data = []
with open('code.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip('\n')
        data.append(line)

for i in range(len(data)):
    getInfoFromDouban(data[i])
