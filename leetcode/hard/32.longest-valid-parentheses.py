#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#
def longestValidParentheses(s: str) -> int:
    if s == "":
        return 0
    bal = 0
    total = 0
    for char in s:
        print(char)
        if char == ")":
            if bal > 0:
                print("current bal is ", bal)
                pass
            else:
                print("current total is ", bal)
                total += 1
        else:
            bal += 1
    if bal == 0:
        return total
    else:
        print("end total is ", total)
        print("end bal is ", bal)
        return bal


if __name__ == "__main__":
    longestValidParentheses("(()")

