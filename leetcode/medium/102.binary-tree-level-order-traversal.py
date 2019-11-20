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
        levels = []
        self.traversal(0, root, levels)
        return levels

    def traversal(self, currLevel, root, levels):
        if not root:
            return []
        if len(levels) <= currLevel:
            levels += [[root.val]]
        else:
            levels[currLevel] += [root.val]
        self.traversal(currLevel + 1, root.left, levels)
        self.traversal(currLevel + 1, root.right, levels)


# @lc code=end

