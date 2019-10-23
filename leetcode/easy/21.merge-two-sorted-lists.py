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
        head, merged_list = ListNode(0)
        left, right = l1, l2
        while left or right:
            if left == None:
                merged_list.next = right
                break
            if right == None:
                merged_list.next = left
                break
            if left.val < right.val:
                merged_list.next = merged_list = ListNode(left.val)
                left = left.next
            if left.val > right.val:
                merged_list.next = merged_list = ListNode(right.val)
                right = right.next
        return head.next


# @lc code=end

