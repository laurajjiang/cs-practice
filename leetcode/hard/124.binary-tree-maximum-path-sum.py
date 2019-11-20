#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.sum = float("-inf")
        self.dfs(root)
        return self.sum

    def dfs(self, root):
        if not root:
            return 0
        leftSubSum = max(0, self.dfs(root.left))
        rightSubSum = max(0, self.dfs(root.right))

        self.sum = max(self.sum, leftSubSum + rightSubSum + root.val)
        return max(leftSubSum, rightSubSum) + root.val


# @lc code=end

