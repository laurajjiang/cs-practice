#
# @lc app=leetcode id=706 lang=python3
#
# [706] Design HashMap
#

# @lc code=start


class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


class MyHashMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10
        self.m = [None] * self.size

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        index = key % self.size
        if self.m[index] == None:
            self.m[index] = ListNode(key, value)
        else:
            currNode = self.m[index]
            while True:
                if currNode.key == key:
                    currNode.val = value
                    return
                if currNode.next is None:
                    break
                currNode = currNode.next
            currNode.next = ListNode(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = key % self.size
        if self.m[index] == None:
            return -1
        else:
            currNode = self.m[index]
            while currNode:
                if currNode.key == key:
                    return currNode.val
                currNode = currNode.next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = key % self.size
        if self.m[index] != None:
            currNode = self.m[index]
            if currNode.key == key:
                self.m[index] = currNode.next
            else:
                while currNode is not None and currNode.next is not None:
                    if currNode.next.key == key:
                        currNode.next = currNode.next.next
                    else:
                        currNode = currNode.next
        return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end

