#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        if k == 0:
            return head

        curr = head
        length = 0
        while head:
            length += 1
            head = head.next

        index = length - (k % length) - 1
        length = 0

        temp = ListNode(-1)

        head = curr
        while curr:
            if length == index:
                temp.next = curr.next
                curr.next = None
                break
            length += 1
            curr = curr.next

        if temp.next == None:
            return head

        curr2 = temp.next
        while temp.next != None:
            temp = temp.next
        temp.next = head
        return curr2


# @lc code=end

