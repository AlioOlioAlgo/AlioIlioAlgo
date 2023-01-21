"""
 *packageName    :
 * fileName       : 108.Conert Sorted Array to Binary Search Tree
 * author         : ipeac
 * date           : 2023-01-08
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-01-08        ipeac       최초 생성
 """

# Definition for a binary tree node.
from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            print(f"self = {self}")
            return None
        mid = len(nums) // 2
        print("==========================================")
        print(f"mid = {mid}")
        
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid + 1:])
        
        return node
