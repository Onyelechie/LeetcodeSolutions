#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):        
            count += self.count_pal(s,i,i)
            count += self.count_pal(s,i,i+1)
        return count


    def count_pal(self, s, l , r):
        count = 0
        while (l >= 0) and (r < len(s)) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        return count

        
# @lc code=end

