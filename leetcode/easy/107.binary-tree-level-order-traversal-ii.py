#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []
        depth = 1
        self.helper(result, depth, root)
        result.reverse()
        return result

    def helper(self, result: int, depth: int, node: TreeNode):
        if not node:
            return
        if len(result) < depth:
            result.append([])
        result[depth - 1].append(node.val)
        self.helper(result, depth + 1, node.left)
        self.helper(result, depth + 1, node.right)


# @lc code=end

