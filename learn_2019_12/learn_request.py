from time import time
from threading import Thread

import requests

class DownLoadHanlder(Thread):

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        filename = self.url[self.url.rfind('/') + 1:] #通过截取url中字符串命名成文件名
        resp = requests.get(self.url)
        with open('../file/'+ filename, 'wb') as f:
            f.write(resp.content)

def main():
    resp = requests.get('http://api.tianapi.com/film/index?key=8c1b3b74b22daefdcd8d066d1aabacbc&num=10')
    data_model = resp.json()
    #print(data_model)
    for mm_dict in data_model['newslist']: #遍历返回json中的‘newlist“数组
        url = mm_dict['picUrl'] #获取其中url
        DownLoadHanlder(url).start() #进行下载

if __name__ == "__main__":
    main()