# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        currNode = head
        nextNode = head
        prevNode = None

        while nextNode is not None:
            nextNode = currNode.next
            currNode.next = prevNode
            head = prevNode = currNode
            currNode = nextNode
        return head

