# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        levels = []
        level = 0
        queue = deque([root])
        while queue:
            levels.append([])
            levelLength = len(queue)

            for i in range(levelLength):
                curr = queue.popleft()
                levels[level].append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            level += 1

        return levels
