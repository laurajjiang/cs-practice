#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        m = len(matrix) - 1
        n = len(matrix[0]) - 1
        # dir is used to know in which direction are we traversing.
        # 0 -> left to right
        # 1 -> up to down
        # 3-> right to left
        # 4-> down to up

        dir = 0

        t, b, r, l = 0, m, n, 0
        res = []
        while t <= b and l <= r:
            if dir == 0:
                for i in range(l, r + 1):
                    res.append(matrix[t][i])
                t += 1
                dir = 1
            elif dir == 1:
                for i in range(t, b + 1):
                    res.append(matrix[i][r])
                r -= 1
                dir = 3
            elif dir == 3:
                for i in range(r, l - 1, -1):
                    res.append(matrix[b][i])
                b -= 1
                dir = 4
            else:
                for i in range(b, t - 1, -1):
                    res.append(matrix[i][l])
                l += 1
                dir = 0
        return res
