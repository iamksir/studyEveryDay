from time import sleep
import time
from threading import Thread, Lock

class Account(object):
    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        #获取锁之后执行代码
        self._lock.acquire()
        #j计算存款后余额
        try:
            new_balance = self._balance + money
            sleep(0.05)
            self._balance = new_balance
        finally:
            #执行释放锁的操作保证正常、异常锁都能释放
            self._lock.release()

    @property
    def balance(self):
        return self._balance

class AddMoneyThread(Thread):

    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)

def main():
    account = Account()
    threads = []
    start = time.clock()
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    end = time.clock()
    print('账户余额为：￥%d元' % account.balance)
    print('交易耗时%.2f秒' % (end - start))

if __name__ == "__main__":
    main()