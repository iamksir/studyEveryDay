def main():
    try:
        with open('../file/王科11.3.pdf', 'rb') as fs1:
            data = fs1.read()
            print(type(data))
        with open('../file/王科11.3_副本.pdf', 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print('指定文件无法打开')
    except IOError as e:
        print('读写文件出现异常')
    print('复制完成')

if __name__ == "__main__":
    main()