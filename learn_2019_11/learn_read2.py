import time

def main():

    #读取整个文件内容
    # with open('致橡树.txt', 'r', encoding='utf-8') as f:
    #     print(f.read())

    #通过循环逐行读取
    # with open('致橡树.txt', mode='r', encoding='utf-8') as f:
    #     for line in f:
    #         print(line, end=' ')
    #         time.sleep(0.5)
    # print()


    #将文件按行读取到列表中
     with open('../file/致橡树.txt', encoding='utf-8') as f:
        while True:
            lines = f.readline()
            print(lines)
            if len(lines) == 0:
                break

if __name__ == "__main__":
    main()