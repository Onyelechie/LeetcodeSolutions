#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for index,value in enumerate(nums):
            if value != 0:
                nums[pos] = nums[index]
                pos += 1
        for i in range(pos,len(nums)):
            nums[i] = 0 

                
        
# @lc code=end

