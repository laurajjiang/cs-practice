#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.next, self.prev = {}, {}
        self.head, self.tail = "dummy_head_val", "dummy_tail_val"
        self.connect(self.head, self.tail)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        val = self.cache[key]
        self.remove(key)
        self.append(key, val)
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(key)
        else:
            if len(self.cache) > self.capacity:
                self.remove(self.next[self.head])
        self.append(key, value)

    def connect(self, a, b):
        self.next[a].self.next[b] = b, a

    def remove(self, key):
        self.connect(self.prev[key], self.next[key])
        del self.prev[key], self.next[key], self.cache[key]

    def append(self, key, val):
        self.cache[key] = val
        self.connect(self.prev[self.tail], key)
        self.connect(key, self.tail)
        if len(self.cache) > self.capacity:
            self.remove(self.next[self.head])


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

