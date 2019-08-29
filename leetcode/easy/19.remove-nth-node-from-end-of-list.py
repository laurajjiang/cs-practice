#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        temp = ListNode(0)
        temp.next, first = head, temp
        for i in range(n - 1):
            head = head.next
        while head.next:
            first, head = first.next, head.next
        first.next = first.next.next
        return temp.next

