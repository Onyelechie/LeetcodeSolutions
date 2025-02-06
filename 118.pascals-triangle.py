#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        array = [[1]]
        for i in range(numRows-1):
            temp = [0] + array[i] + [0]
            temp_arr = []
            for i in range(len(temp)-1): 
                temp_arr.append(temp[i]+temp[i+1])
            array.append(temp_arr)
        return array
# @lc code=end

