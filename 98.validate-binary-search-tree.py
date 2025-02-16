#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.valid(root,float('-inf'),float('inf'))
    
    def valid(self, root,left,right):
        if not root:
            return True
        if not (left < root.val < right):
            return False
        return self.valid(root.left,left,root.val) and self.valid(root.right,root.val,right) 
        
# @lc code=end

