def binary_search(array, target):
    beg = 0
    mid = len(array) // 2
    end = len(array) - 1
    while beg + 1 != end and beg != end:
        if target == array[mid]:
            return mid
        if target < array[mid]:
            end = mid
            mid = (beg + end) // 2
        if target > array[mid]:
            beg = mid
            mid = (beg + end) // 2
