class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        maxSeen = -1
        for i in range(len(arr) - 1, -1, -1):
            temp = arr[i]
            arr[i] = maxSeen
            maxSeen = max(temp, maxSeen)
        return arr

