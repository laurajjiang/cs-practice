#
# @lc app=leetcode id=884 lang=python3
#
# [884] Uncommon Words from Two Sentences
#

# @lc code=start
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        seen, common = set(), set()
        for word in A.split() + B.split():
            if word in seen:
                common.add(word)
            seen.add(word)
        return list(seen - common)


# @lc code=end

