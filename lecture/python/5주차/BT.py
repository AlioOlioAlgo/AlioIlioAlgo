"""
 *packageName    :
 * fileName       : BT
 * author         : ipeac
 * date           : 2022-12-26
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-26        ipeac       최초 생성
 """

class BinaryTree:
    def __init__(self, left=None, right=None, parent=None, value=None):
        self.left = left
        self.right = right
        self.value = value
        self.parent = parent
    
    def print_preorder(self):
        # 전위 순회 값 출력 -> 리스트 형태로 값을 출력한다.
        def dfs(target_tree):
            print(target_tree.value, end=" ")
            if target_tree.left:
                dfs(target_tree.left)
            if target_tree.right:
                dfs(target_tree.right)
        
        dfs(self)
    
    def add(self, e):  # 부모보다 작으면 왼쪽 크면 오른쪽
        def _add(node, e):
            if node.value < e:
                if node.right:
                    _add(node.right, e)
                else:
                    node.right = BinaryTree(None, None, node, e)
            if node.value > e:
                if node.left:
                    _add(node.left, e)
                else:
                    node.left = BinaryTree(None, None, node, e)
        
        _add(self, e)

root = BinaryTree(None, None, None, 5)
root.add(7)
root.add(4)
root.add(3)
# root.print_preorder()
root.add(1)
root.add(2)
root.print_preorder()
