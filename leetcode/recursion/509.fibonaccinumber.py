class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <= 1:
            return N
        self.dict = {0: 0, 1: 1}
        return self.calculate(N)

    def calculate(self, N):
        if N in self.dict.keys():
            return self.dict[N]
        self.dict[N] = self.calculate(N - 1) + self.calculate(N - 2)
        return self.calculate(N)

