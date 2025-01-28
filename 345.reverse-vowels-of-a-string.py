#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        answer = list(s)
        vow_index = []
        vow_value = []
        for index , value in enumerate(answer):
            if value in vowels:
                vow_index.append(index)
                vow_value.append(value)
        vow_value.reverse()
        for i , index in enumerate(vow_index):
            answer[index] = vow_value[i]
        return ''.join(answer)



# @lc code=end

