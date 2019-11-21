#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        res = []
        self.inorderTraversal(root, res)
        for i in range(len(res) - 1):
            if res[i].val >= res[i + 1].val:
                return False
        return True

    def inorderTraversal(self, root, res):
        if root is None:
            return True
        if root.left:
            self.inorderTraversal(root.left, res)
        res.append(root)
        if root.right:
            self.inorderTraversal(root.right, res)


# @lc code=end

