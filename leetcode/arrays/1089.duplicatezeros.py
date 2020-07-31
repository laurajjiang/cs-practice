class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        duplicateZeros = 0
        length_ = len(arr) - 1

        for left in range(len(arr)):
            if left > length_ - duplicateZeros:
                break
            if arr[left] == 0:
                if left == length_ - duplicateZeros:
                    arr[length_] = 0
                    length_ -= 1
                    break
                duplicateZeros += 1

        lastIdx = length_ - duplicateZeros
        print(lastIdx)
        for i in range(lastIdx, -1, -1):
            print(i)
            if arr[i] == 0:
                arr[i + duplicateZeros] = 0
                duplicateZeros -= 1
                arr[i + duplicateZeros] = 0
            else:
                arr[i + duplicateZeros] = arr[i]

