#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head
        prev_node = None
        while fast and fast.next:
            fast = fast.next.next
            head = head.next

            next_node = slow.next
            slow.next = prev_node
            prev_node = slow
            slow = next_node

        if fast:
            head = head.next

        while prev_node and head:
            if prev_node.val != head.val:
                return False
            prev_node = prev_node.next
            head = head.next
        return True


# @lc code=end

