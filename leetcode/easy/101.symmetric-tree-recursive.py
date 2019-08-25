#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isSymmetricHelperFx(root.left, root.right)

    def isSymmetricHelperFx(self, p, q):
        if not p or not q:
            return p == q
        if p.val != q.val:
            return False
        return self.isSymmetricHelperFx(p.left, q.right) and self.isSymmetricHelperFx(
            p.right, q.left
        )
