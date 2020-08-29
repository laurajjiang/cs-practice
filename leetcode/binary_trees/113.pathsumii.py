# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        pathList = []
        self.recurseTree(root, sum, [], pathList)
        return pathList

    def recurseTree(self, node, remainingSum, pathNodes, pathList):
        if not node:
            return

        pathNodes.append(node.val)

        if remainingSum == node.val and not node.left and not node.right:
            pathList.append(list(pathNodes))
        else:
            self.recurseTree(node.left, remainingSum - node.val, pathNodes, pathList)
            self.recurseTree(node.right, remainingSum - node.val, pathNodes, pathList)

        pathNodes.pop()

