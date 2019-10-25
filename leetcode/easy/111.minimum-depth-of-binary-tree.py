#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        return (min(left, right) or (max(left, right))) + 1


# @lc code=end

