#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root:
            q = [root]
        else:
            return []
        level = 0
        res = []
        while q:
            temp = []
            q_temp = []
            for node in q:
                temp.append(node.val)
                if node.left:
                    q_temp.append(node.left)
                if node.right:
                    q_temp.append(node.right)
            if level % 2 == 0:
                res.append(temp)
            else:
                res.append(temp[::-1])
            q = q_temp
            level += 1
        return res


# @lc code=end

