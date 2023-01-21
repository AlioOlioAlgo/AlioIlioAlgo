"""
 *packageName    :
 * fileName       : 1302. Deepest Leaves Sum
 * author         : ipeac
 * date           : 2022-12-25
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-25        ipeac       최초 생성
 """
from typing import Optional

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

sum_value = 0
max_depth = 0

class Solution(object):
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        global sum_value
        global max_depth
        print(f"첫 sum_value : {sum_value}")
        print(f"첫 max_depth : {max_depth}")
        
        def dfs(target_root, depth):
            global sum_value
            global max_depth
            print("==========================================")
            print(f"target_root = {target_root}")
            print(f"depth = {depth}")
            
            if target_root is None:
                return
            
            if depth > max_depth:
                max_depth = depth
                sum_value = target_root.val
                print(f"sum_value = {sum_value}")
                print(f"target_root = {target_root.val}")
            elif depth == max_depth:
                sum_value += target_root.val
                print(f"sum_value = {sum_value}")
                print(f"target_root = {target_root.val}")
            
            dfs(target_root.left, depth + 1)
            dfs(target_root.right, depth + 1)
        
        dfs(root, 0)
        
        tmp_value = sum_value
        sum_value = 0
        max_depth = 0
        return tmp_value
