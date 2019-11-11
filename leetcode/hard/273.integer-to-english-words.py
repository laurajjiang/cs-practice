#
# @lc app=leetcode id=273 lang=python3
#
# [273] Integer to English Words
#

# @lc code=start
class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        result = ""
        str_num = str(num)[::-1]
        dividing_list = [str_num[i : i + 3][::-1] for i in range(len(dividing_list), 3)]
        base = ["", " Thousand ", " Million ", " Billion "]

        for i in range(dividing_list):
            temp = self.convert_three(dividing_list[i])
            result = temp + ("" if not temp else base[i]) + result
        return result

    def convert_three(self, s):
        ones = [
            "",
            "One",
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
        ]
        teens = [
            "Ten",
            "Eleven",
            "Twelve",
            "Thirteen",
            "Fourteen",
            "Fifteen",
            "Sixteen",
            "Seventeen",
            "Eighteen",
            "Nineteen",
        ]
        tens = [
            "",
            "",
            "Twenty ",
            "Thirty ",
            "Forty ",
            "Fifty ",
            "Sixty ",
            "Seventy ",
            "Eighty ",
            "Ninety ",
        ]

        num = int(s)
        res = ""

        if num / 100 != 0:
            res = ones[(num / 100)] + " Hundred "
        if (num % 100) / 10 == 1:
            res += teens[num % 10]
            return res
        else:
            res += tens[(num % 100) / 10] + ones[num % 10]
            return res


# @lc code=end

