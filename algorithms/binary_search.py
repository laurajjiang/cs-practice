def binary_search(arr: List[int], val: int):
    lo = 0
    hi = len(arr) - 1
    mid = (lo + hi) / 2

    while lo < hi:
        if arr[mid] == val:
            return arr[mid]
        elif arr[mid] < val:
            lo = mid + 1
            mid = (lo + hi) / 2
        else:
            hi = mid - 1
            mid = (lo + hi) / 2
    return -1
