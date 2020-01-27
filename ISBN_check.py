import urllib
import urllib.request
import json


def __getInfoFromDouban(isbn):
    try:
        # 将isbn作为变量传递到url中，得到对应的地址
        url = 'https://api.douban.com/v2/book/isbn/' + isbn
        # 使用urllib模块打开url
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        request = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(request)
        # 读取url的网页内容，并用utf8编码
        result = response.read().decode('utf8')
        # 将返回的字符串转成json格式
        result_json = json.loads(result)
        # 信息获取失败，抛出一个异常
    except urllib.error.HTTPError as e:
        raise e
    return result_json


f = open("code.txt")
data = []
with open('code.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip('\n')
        data.append(line)

for i in range(len(data)):
    __getInfoFromDouban(data[i])
