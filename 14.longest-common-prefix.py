#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        for index, values in enumerate(strs):
            check = True
            for i in strs:
                if i[index] != values:
                    check = False
                    return result
            result.append(values[index])
        return result

# @lc code=end

