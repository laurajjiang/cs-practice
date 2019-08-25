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

from collections import deque


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        list = deque([(root.left, root.right)])
        while list:
            p, q = list.popleft()
            if not self._check(p, q):
                return False
            if p:
                list.append((p.left, q.right))
                list.append((p.right, q.left))
        return True

    def _check(self, p, q):
        if not p or not q:
            return p == q
        return p.val == q.val

