#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        result = []
        if not root:
            return result
        q = deque()
        q.append(root)

        while q:
            level = len(q)
            for i in range(level):
                curr = q.popleft()
                if i == level - 1:
                    result.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

        return result


# @lc code=end

