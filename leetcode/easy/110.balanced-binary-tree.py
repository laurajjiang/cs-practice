#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root == None:
            return True
        left = self.depth(root.left)
        right = self.depth(root.right)
        return (
            (abs(left - right) < 2)
            and self.isBalanced(root.left)
            and self.isBalanced(root.right)
        )

    def depth(self, node: TreeNode):
        if node == None:
            return 0
        return max(self.depth(node.left), self.depth(node.right)) + 1


# @lc code=end

