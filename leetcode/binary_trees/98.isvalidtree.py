# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(curr, max, min): 
            if curr is None:
                return True
            if curr.val >= max or curr.val <= min:
                return False
            return helper(curr.left, curr.val, min) and helper(curr.right, max, curr.val)
        
        return helper(root, float("inf"), float("-inf"))