#
# @lc app=leetcode id=538 lang=python3
#
# [538] Convert BST to Greater Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        curr_root = root
        stack = []
        cumulative_sum = 0

        while root or stack:
            while root:
                stack.append(root)
                root = root.right
            root = stack.pop()

            _ = root.val
            root.val += cumulative_sum
            cumulative_sum += _

            root = root.left

        return curr_root

        # @lc code=end

