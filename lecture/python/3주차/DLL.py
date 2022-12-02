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
        def __init__(self, value=0, next_ref=None, prev_ref=None):  # 생성자 개개 노드의 값과 다음 레퍼런스를 담는다.
            self.value = value
            self.next_ref = next_ref
            self.prev_ref = prev_ref
    
    def __init__(self, head=None, size=0, tail=None):  # 총 노드 리스트의 첫번째 노드를 설정해준다, size계산의 용이를 위해 size변수를 0으로 선언후 이후 값변경시마다 연산할 예정이다.
        self.head = head
        self.tail = tail
        self.size = size
    
    def add_front(self, e):  # 맨 첫번째에 노드를 담는다. 이때 해당 헤드 노드가 없는 경우 헤드노드를 생성 , 있다면 새로운 노드는 헤드노드를 다음 값으로 가진다.
        t = self.Node(e, next_ref=None, prev_ref=None)
        if self.size == 0:
            self.head = t
            self.tail = t
        else:
            self.head.prev_ref = t
            t.next_ref = self.head
            self.head = t
        self.size += 1
        self.print()
    
    def remove_front(self):  # 맨 첫 번째 노드를 지운다. 이때 사이즈가 0 인경우 > 아무동작도 수행하지 않음 | 사이즈가 1이상이라면 헤드노드가 다음 노드를 참조한다.
        if self.size == 0:
            print("해당 DLL의 맨 첫 번째 노드는 존재하지 않습니다.")
            return Exception("에러")
        else:
            self.head = self.head.next_ref
            self.size -= 1
        self.print()
    
    def size_of(self):
        return self.size
    
    def front(self):
        return self.head.value
    
    def front_head(self):
        return self.head
    
    def add_back(self, e):
        t = self.Node(e, next_ref=None, prev_ref=None)
        if self.size == 0:
            self.head = t
            self.tail = t  # 끝같을 헤드값으로 참조
        else:
            self.tail.next_ref = t
            t.prev_ref = self.tail
        self.size += 1
    
    def remove_back(self):
        if self.size == 0:
            print("사이즈 0임 ㅡㅡ")
            return Exception("사이즈 0인데 값을 빼냐")
        else:
            self.tail = self.tail.prev_ref
            self.tail.next_ref = None
        self.size -= 1
    
    def insert_prev(self, n, e):
        t = self.Node(e, prev_ref=None, next_ref=None)
        if self.size == 0:
            return Exception("에러")
        else:
            print(f"self.head = {self.head.value}")
            head_value = self.head
            print(f"head_value = {head_value.value}")
            
            if self.head == n:
                self.add_front(e)
                return
            elif self.tail == n:
                self.add_back(e)
                return
            
            while head_value:
                if head_value.next_ref == n:
                    t.prev_ref = head_value
                    print(f"t.prev_ref = {t.prev_ref}")
                    t.next_ref = head_value.next_ref
                    print(f"t.next_ref = {t.next_ref}")
                    
                    head_value.next_ref = t
                    head_value.next_ref.next_ref = t
                
                head_value = head_value.next_ref
            
            self.print()
    
    def remove(self, n):
        if self.size == 0:
            return Exception("에러")
        else:
            head_value = self.head
            while head_value:
                if head_value == n:
                    head_value.prev_ref.next_ref = head_value.next_ref
                    head_value.next_ref.prev_ref = head_value.prev_ref
                head_value = head_value.next_ref
        self.print()
    
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
    
    def search_second_node(self):
        return self.head.next_ref

node_test = NodeList()
node_test.add_front(1)
node_test.add_front(2)
node_test.add_front(3)
node_test.add_front(4)
node_test.insert_prev(node_test.search_second_node(), 2)
node_test.print()
