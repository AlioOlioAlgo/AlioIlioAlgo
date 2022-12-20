"""
 *packageName    :
 * fileName       : 트리노드depthheight
 * author         : ipeac
 * date           : 2022-12-18
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-18        ipeac       최초 생성
 """

class TreeNode:
    def __init__(self, parent=None, element=None, childrens=None):
        if childrens is None:
            childrens = []
        self.parent = parent
        self.element = element
        self.childrens = childrens
    
    # 부모 설정 함수
    def set_parent(self, parent):
        self.parent = parent
    
    # 자식 추가 함수 (자식은 여러개 가능)
    def append_children(self, children):
        self.childrens.append(children)

root = TreeNode(None, 3, None)  # 루트
child1_depth1 = TreeNode(root, 1, None)
child2_depth1 = TreeNode(root, 7, None)
child3_depth1 = TreeNode(root, 4, None)
child1_depth2 = TreeNode(child1_depth1, 6, None)
child2_depth2 = TreeNode(child1_depth1, 6, None)
child3_depth2 = TreeNode(child2_depth1, 6, None)
child4_depth2 = TreeNode(child3_depth1, 6, None)
child5_depth2 = TreeNode(child3_depth1, 6, None)
# 0 자식의 자식 설정
child1_depth1.append_children(child1_depth2)
child1_depth1.append_children(child2_depth2)

# 1 자식의 자식 설정
child2_depth1.append_children(child3_depth2)

# 2 자식의 자식 설정
child3_depth1.append_children(child4_depth2)
child3_depth1.append_children(child5_depth2)

def depth(find_node, cnt):
    # 부모는 무조건 하나임.
    if find_node == root:
        return cnt
    return depth(find_node.parent, cnt + 1)

def height(find_node, cnt):
    return height(find_node)
    pass

# 1. 재귀로 풀기 +
# 2. 반복문 으로 풀기 +
# depth()
# height()
#
print(depth(child3_depth2, 0))
print(height())
