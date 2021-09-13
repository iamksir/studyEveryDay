from random import randint
from time import sleep,time
from multiprocessing import Process
from os import getpid

# 正常程序执行
# def download_task(filename):
#     print('开始下载%s...' % filename)
#     time_to_download = randint(5, 10)
#     sleep(time_to_download)
#     print('%s下载完成， 耗时%s秒' % (filename, time_to_download))
#
# def main():
#     start = time()
#     download_task('致橡树.txt')
#     download_task('Joler.avi')
#     end = time()
#     print('共耗时%.2f秒' % (end - start))
#
#
# if __name__ == "__main__":
#     main()

# 多进程模式
def download_task(filename):
    print('启动下载进程，进程号[%d]' % getpid())
    print('开始下载%s' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成，耗时%d秒' % (filename, time_to_download))

def main():
    start = time()
    p1 = Process(target=download_task, args=('致橡树.txt',))
    p1.start()
    p2 = Process(target=download_task, args=('Joker.avi',))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('共耗时%.2f秒' % (end - start))

if __name__ == "__main__":
    main()