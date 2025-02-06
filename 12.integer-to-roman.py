#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        map = {
            1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X",
            40: "XL", 50: "L", 90: "XC", 100: "C",
            400: "CD", 500: "D", 900: "CM", 1000: "M"
        }
        answer = ""
        for i in map.keys().__reversed__():
            if num/i != 0:
                answer += f"{map[i]}"*int(num/i)
            num = num % i
        return answer
        
# @lc code=end

