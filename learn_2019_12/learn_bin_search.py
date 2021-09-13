def bin_search(items, key):
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if key > items[mid]:
            start = mid + 1
        elif key < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1

if __name__ == "__main__":
    items = [1,2,3,4,5,6,7,8,9]
    L = bin_search(items, 6)
    print(L)