from random import randint
from time import sleep, time
from threading import Thread

class DownloadTask(Thread):

    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print('开始下载%s...' % self._filename)
        time_to_download = randint(5, 10)
        sleep(time_to_download)
        print('%s下载完成，共耗时%d秒' % (self._filename, time_to_download))

def main():
    start = time()
    t1 = DownloadTask('致橡树.txt')
    t1.start()
    t2 = DownloadTask('Joker.avi')
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('共耗时%.2f秒' % (end - start))

if __name__ == "__main__":
    main()