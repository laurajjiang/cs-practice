# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        level_queue = deque()
        if root is None:
            return []
        node_queue = deque([root, None])
        isStartLeft = True

        while len(node_queue) > 0:
            curr = node_queue.popleft()
            if curr:
                if isStartLeft:
                    level_queue.append(curr.val)
                else:
                    level_queue.appendleft(curr.val)
                if curr.left:
                    node_queue.append(curr.left)
                if curr.right:
                    node_queue.append(curr.right)
            else:
                levels.append(level_queue)
                if len(node_queue) > 0:
                    node_queue.append(None)

                level_queue = deque()
                isStartLeft = not isStartLeft
        return levels
