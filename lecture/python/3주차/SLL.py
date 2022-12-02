"""
 *packageName    :
 * fileName       : SLL, DLL 구현
 * author         : ipeac
 * date           : 2022-12-02
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-02        ipeac       최초 생성
 """

class NodeList:  # 노드 리스트
    class Node:  # 노드 개별
        def __init__(self, value=0, next_ref=None):  # 생성자 개개 노드의 값과 다음 레퍼런스를 담는다.
            self.value = value
            self.next_ref = next_ref
    
    def __init__(self, head=None, size=0):  # 총 노드 리스트의 첫번째 노드를 설정해준다, size계산의 용이를 위해 size변수를 0으로 선언후 이후 값변경시마다 연산할 예정이다.
        self.head = head
        self.size = size
    
    def add_front(self, e):  # 맨 첫번째에 노드를 담는다. 이때 해당 헤드 노드가 없는 경우 헤드노드를 생성 , 있다면 새로운 노드는 헤드노드를 다음 값으로 가진다.
        if self.size == 0:
            self.head = self.Node(e, None)
        else:
            # print("add_front size over 1")
            self.head = self.Node(e, self.head)
        self.size += 1
        self.print()
    
    def remove_front(self):  # 맨 첫 번째 노드를 지운다. 이때 사이즈가 0 인경우 > 아무동작도 수행하지 않음 | 사이즈가 1이상이라면 헤드노드가 다음 노드를 참조한다.
        if self.size == 0:
            print("해당 SLL의 맨 첫 번째 노드는 존재하지 않습니다.")
            return Exception("에러")
        else:
            self.head = self.head.next_ref
            self.size -= 1
        self.print()
    
    def size_of(self):
        return self.size
    
    def front(self):
        return self.head.value
    
    def print(self):
        if self.size == 0:
            print('[]')
        else:
            head_node = self.head
            print_list = []
            while head_node:  # 해당 헤드 노드부터 천천히 하나씩 포인터를 옮기면서 프린트한다. 포인터를 옮긴 값에 next 노드가 존재하지 않는 다면 멈출것이다.
                print_list.append(head_node.value)
                head_node = head_node.next_ref
            print(f"print_list = {print_list}")

node_test = NodeList()
node_test.add_front(1)
node_test.add_front(2)
node_test.add_front(3)
print(node_test.front())
node_test.remove_front()
print(node_test.size_of())  # size 는 예약어라 사용이 불가능했습니다.

node_test.add_front(5)
