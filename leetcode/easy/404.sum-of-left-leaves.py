#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        sum = 0

        def dfs(root):
            if not root:
                return
            if root.left and not root.left.left and not root.left.right:
                nonlocal sum
                sum += root.left.val
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return sum


# @lc code=end

