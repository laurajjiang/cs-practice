# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        l3 = ListNode(-1)
        curr = l3
        carry = 0
        while l1 or l2: 
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2: 
                sum += l2.val
                l2 = l2.next
            sum += carry
            curr.next = ListNode(sum % 10)
            curr = curr.next
            carry = sum / 10
        if carry: 
            curr.next = ListNode(1)
        return l3.next