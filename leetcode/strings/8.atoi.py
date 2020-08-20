class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.lstrip(" ")
        if not str:
            return 0

        num = 0

        sign = -1 if str[0] == "-" else 1
        if sign == -1 or str[0] == "+":
            str = str[1:]

        for i in range(len(str)):
            if str[i] < "0" or str[i] > "9":
                if i == 0:
                    return 0
                return min(num, 2147483647) if sign == 1 else max(-1 * num, -2147483648)
            num = num * 10 + (ord(str[i]) - 48)

        return min(num, 2147483647) if sign == 1 else max(-1 * num, -2147483648)
