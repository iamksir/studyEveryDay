# 循环引用-会导致内存泄漏
class A(object):
    def __init__(self):
        self.data = [x for x in range(100000)]
        self.child = None

    def __del__(self):
        pass

def cycle_ref():
    a1 = A()
    a2 = A()
    a1.child = a2
    a2.child = a1

if __name__ == '__main__':
    import time
    while True:
        time.sleep(0.5)
        cycle_ref()