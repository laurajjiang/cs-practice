#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        self.levels = []
        self.traversal(0, root)
        return self.levels

    def traversal(self, currLevel, root):
        if not root:
            return []
        if len(self.levels) <= currLevel:
            self.levels += [[root.val]]
        else:
            self.levels[currLevel] += [root.val]
        self.traversal(currLevel + 1, root.left)
        self.traversal(currLevel + 1, root.right)


# @lc code=end

