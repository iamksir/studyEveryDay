def seq_search(items, key):
    '''顺序查找'''
    for index, item in enumerate(items):
        if item == key:
            return index
    return -1

if __name__ == "__main__":
    items = [1,9,2,8,3,7,4,6,5]
    L = seq_search(items, key=2)
    print(L)