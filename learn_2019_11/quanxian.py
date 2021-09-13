class Test:
    def __int__(self,too):
        self.__too = too

    def __bar(self):
        print(self.__too)
        print('__bar')

def main():
    test = Test()
    test.__bar()
    print(test.__too)

if __name__ == "__main__":
     main()