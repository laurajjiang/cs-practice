#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = merged_list = ListNode(0)
        left, right = l1, l2
        while left and right:
            if left.val < right.val:
                merged_list.next = left
                merged_list = merged_list.next
                left = left.next
            elif left.val >= right.val:
                merged_list.next = right
                merged_list = merged_list.next
                right = right.next
        merged_list.next = left or right
        return head.next


# @lc code=end

