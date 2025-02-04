#
# @lc app=leetcode id=780 lang=python3
#
# [780] Reaching Points
#

# @lc code=start
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx > sx and ty > sy:
            if tx > ty:
                tx %= ty
            else:
                ty %= tx
        
        if tx == sx and ty >= sy and (ty - sy) % sx == 0:
            return True
        if ty == sy and tx >= sx and (tx - sx) % sy == 0:
            return True
        
        return False
# @lc code=end

