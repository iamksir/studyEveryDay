import time

def main():
    total = 0
    number_list = {x for x in range(1, 100000001)}
    start = time.clock()
    for number in number_list:
        total += number
    print(total)
    end = time.clock()
    print('共耗时%.3fs' % (end - start))

if __name__ == "__main__":
    main()