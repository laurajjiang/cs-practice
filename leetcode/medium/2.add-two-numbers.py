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
        isCarry = 0
        linkedSums = ListNode(-1)
        linkedSums_tail = linkedSums
        while l1 or l2 or isCarry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            isCarry, out = divmod(val1 + val2 + isCarry, 10)
            linkedSums_tail.next = ListNode(out)
            linkedSums_tail = linkedSums_tail.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return linkedSums.next


# @lc code=end

