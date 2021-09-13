from time import sleep
from random import randint
import threading

from concurrent.futures import ThreadPoolExecutor

class Account(object):
    """银行账户"""

    def __init__(self, balance = 0):
        self.balance = balance
        lock = threading.Lock()
        self.condition = threading.Condition(lock)

    def withdraw(self, money):
        """取钱"""
        with self.condition:
            while money > self.balance:
                self.condition.wait()
            new_balance = self.balance - money
            sleep(0.001)
            self.balance = new_balance

    def deposit(self, money):
        """存钱"""
        # 通过锁保护临界资源
        with self.condition:
            new_balance = self.balance + money
            sleep(0.001)
            self.balance = new_balance
            self.condition.notify_all()

def add_money(account):
    while True:
        money = randint(5, 10)
        account.deposit(money)
        print(threading.current_thread().name, ':', money, '===>', account.balance)
        sleep(0.5)

def sub_money(account):
    while True:
        money = randint(10, 30)
        account.withdraw(money)
        print(threading.current_thread().name, ':', money, '===>', account.balance)
        sleep(0.5)

if __name__ == '__main__':
    account = Account()
    with ThreadPoolExecutor(max_workers=10) as pool:
        for _ in range(5):
            pool.submit(add_money, account)
            pool.submit(sub_money, account)
