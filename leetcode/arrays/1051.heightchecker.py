class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        swaps = 0
        sortedHeights = heights[:]
        sortedHeights.sort()

        for i in range(len(heights)):
            if sortedHeights[i] != heights[i]:
                swaps += 1

        return swaps
