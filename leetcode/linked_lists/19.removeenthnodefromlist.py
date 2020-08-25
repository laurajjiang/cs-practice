# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        curr = ListNode(-1)
        curr.next = head
        first = second = curr
        for _ in range(n):
            first = first.next
        
        while first and first.next:
            first = first.next
            second = second.next
        
        second.next = second.next.next
        return curr.next