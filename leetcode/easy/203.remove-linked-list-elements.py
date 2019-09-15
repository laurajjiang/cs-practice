#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head

        pointer = head
        p = head.next

        while p:
            if val == p.val:
                p = p.next
                head.next = p
            else:
                head = head.next
                p = p.next

        head = pointer
        if head.val == val:
            pointer = head.next

        return pointer

