#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1, p2 = l1, l2
        linkedSums = ListNode(-1)
        while p1 and p2: 
            linkedSums->val = p1->val + p2->val
            p1, p2 = p1->next, p2->next  
        return linkedSums    
 # @lc code=end

