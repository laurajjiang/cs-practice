#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        temp = ListNode(0)
        temp.next = head
        prev = temp
        curr = temp.next
        if curr:
            fut = curr.next

        while curr and curr.next and fut:
            curr.next = fut.next
            fut.next = curr
            prev.next = fut

            if curr and curr.next:
                fut = curr.next.next
                curr = curr.next
                prev = prev.next.next

        return temp.next


# @lc code=end

