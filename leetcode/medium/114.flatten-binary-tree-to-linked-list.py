#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        dfs = []
        curr = root
        while True:
            if curr.right:
                dfs.append(curr.right)
            if curr.left:
                dfs.append(curr.left)
            if dfs:
                curr.right = dfs.pop()
                curr.left = None
                curr = curr.right
            else:
                break


# @lc code=end

