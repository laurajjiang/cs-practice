class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        x, y = abs(a), abs(b)

        if x < y:
            return self.getSum(b, a)

        sign = 1 if a > 0 else -1

        if a * b >= 0:
            while y != 0:
                answer = x ^ y
                carry = (x & y) << 1
                x = answer
                y = carry
        else:
            while y != 0:
                answer = x ^ y
                borrow = ((~x) & y) << 1
                x = answer
                y = borrow

        return x * sign
