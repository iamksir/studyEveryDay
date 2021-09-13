def select_sort(origin_items, comp=lambda x,y :x < y):
    items = origin_items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i+1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
        print(items[i],items[min_index])
    return items

if __name__ == "__main__":
    items = [9,1,2,5,7,4,8,6,3]
    s = select_sort(items)
    print(s)