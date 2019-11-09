class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        i = j = head
        while i and j and j.next:
            i = i.next
            j = j.next.next
            if i == j:
                return True
        return False
