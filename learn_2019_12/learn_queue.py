from queue import Queue

# 创建一长度为5的队列
q = Queue(5)
# 判空盘：队列为空返回True，反之False
print(q.empty())
# 入队：向队列中添加元素
q.put(1)
# 量对：返回当前队列大小
print(q.qsize())
# 判队满：队列满了返回True，反之False
print(q.full())
q.put('abc')
q.put([2,3,4])
print(q.qsize())
print(q.full())
q.put({'d': 56})
q.put((7,8))
print(q.qsize())
print(q.full())
# 出队：先进先出
print(q.get())
print(q.get())
print(q.get())
print(q.qsize())
print(q.full())
print(q.get())
print(q.get())
print(q.qsize())