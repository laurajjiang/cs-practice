class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        dict = {}
        for i in range(len(arr)):
            if 2 * arr[i] in dict.values() or (
                arr[i] / 2 in dict.values() and arr[i] % 2 == 0
            ):
                return True
            dict[i] = arr[i]
        return False
