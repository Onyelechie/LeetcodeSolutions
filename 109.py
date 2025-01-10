#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        temp_array = []
        top = head
        tree = TreeNode()
        if top is not None:
            temp_array.append(top.val)
            while top.next is not None:
                top = top.next
                temp_array.append(top.val)
            #temp_array.sort()
        for i in range(len(temp_array)/2):
            tree

