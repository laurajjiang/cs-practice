# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None: 
            return None 
        s1, s2 = [], []
        l3 = None
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next 
        carry = 0
        while len(s1) and len(s2): 
            val = s1.pop() + s2.pop() + carry
            carry = val // 10
            node = ListNode(val % 10)
            node.next = l3
            l3 = node
        while len(s1): 
            val = s1.pop() + carry
            carry = val // 10
            node = ListNode(val % 10)
            node.next = l3
            l3 = node
        while len(s2):
            val = s2.pop() + carry
            carry = val // 10
            node = ListNode(val % 10)
            node.next = l3
            l3 = node
        if carry:
            node = ListNode(carry)
            node.next = l3
            l3 = node
        return l3 