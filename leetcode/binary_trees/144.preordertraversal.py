# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Preorder traversal is NLR - node -> left -> right
class Solution(object):
    def __init__(self):
        self.list = []

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if root is None:
            return []
        self.list.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)
        return self.list


#         if root is None:
#             return []
#         stack, order = [root], []

#         while stack:
#             node = stack.pop()
#             order.append(node.val)
#             if node.right:
#                 stack.append(node.right)
#             if node.left:
#                 stack.append(node.left)

#         return order
