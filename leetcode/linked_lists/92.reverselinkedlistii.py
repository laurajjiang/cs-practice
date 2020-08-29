# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        curr, prev = head, None
        for _ in range(m - 1):
            prev = curr
            curr = curr.next

        tail, connector = curr, prev

        for _ in range(n - m + 1):
            third = curr.next
            curr.next = prev
            prev = curr
            curr = third

        if connector:
            connector.next = prev
        else:
            head = prev
        tail.next = curr
        return head
