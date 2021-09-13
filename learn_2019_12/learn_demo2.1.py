from multiprocessing import Process, Queue
import time

def task_handler(curn_list, result_queue):
    total = 0
    for number in curn_list:
        total += number
    # Queue.put()写队列
    result_queue.put(total)

def main():
    processes = []
    number_list = [x for x in range(1, 100000001)]
    result_quese = Queue()
    index = 0
    #启动8个进程将数据切片后进行运算
    for _ in range(8):
        p = Process(target=task_handler, args=(number_list[index: index +12500000], result_quese))
        index += 12500000
        processes.append(p)
        p.start()

    start = time.clock()
    for p in processes:
        p.join()

    #合并执行结果
    total = 0
    # 如果队列为空，返回True，反之false
    while not result_quese.empty():
        # Queue.get()读取对列
        total += result_quese.get()
    print(total)
    end = time.clock()
    print('共耗时%.3fs' % (end - start))

if __name__ == "__main__":
    main()