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
        # self.print()
    
    def remove_front(self):  # 맨 첫 번째 노드를 지운다. 이때 사이즈가 0 인경우 > 아무동작도 수행하지 않음 | 사이즈가 1이상이라면 헤드노드가 다음 노드를 참조한다.
        if self.size == 0:
            print("해당 DLL의 맨 첫 번째 노드는 존재하지 않습니다.")
            return Exception("에러")
        else:
            # 사이즈가 1 인 경우  tail None 처리
            if self.size == 1:
                self.tail = None
            self.head = self.head.next_ref
            self.head.prev_ref = None
            self.size -= 1
        # self.print()
    
    def back(self):
        if self.size == 0:
            return Exception("사이즈가 0입니다.")
        return self.tail.value
    
    def size_of(self):
        return self.size
    
    def front(self):
        if self.size == 0:
            return Exception("사이즈가 0입니다.")
        return self.head.value
    
    def add_back(self, e):
        t = self.Node(e, next_ref=None, prev_ref=None)
        if self.size == 0:
            self.head = t
            self.tail = t  # 끝같을 헤드값으로 참조
        else:
            self.tail.next_ref = t
            t.prev_ref = self.tail
            self.tail = t
        self.size += 1
    
    def remove_back(self):
        if self.size == 0:
            print("사이즈 0임 ㅡㅡ")
            return Exception("사이즈 0인데 값을 빼냐")
        else:
            if self.size == 1:
                self.head = None
            self.tail = self.tail.prev_ref
            self.tail.next_ref = None
        self.size -= 1
    
    def insert_prev(self, n, e):
        print("==================insert_prev========================")
        t = self.Node(e, prev_ref=None, next_ref=None)
        if self.size == 0:
            return Exception("에러")
        else:
            # print(f"self.head = {self.head.value}")
            head_value = self.head
            # print(f"head_value = {head_value.value}")
            if self.head == n:
                self.add_front(e)
                return
            elif self.tail == n:
                self.add_back(e)
                return
            
            # 앞뒤 제외 중간 노드의 경우
            #  n 이전 노드
            prev_node = n.prev_ref
            #  이전 노드 다음 값 => 새로운 연결
            # n 노드 이전 값 => 새로운 연결
            prev_node.next_ref = t
            n.prev_ref = t
            # 삽입할 노드의 앞뒤 연결
            t.prev_ref = prev_node
            t.next_ref = n
    
    def remove(self, n):
        print("==================remove========================")
        
        if self.head == n:
            self.remove_front()
            return
        elif self.tail == n:
            self.remove_back()
            return
        
        if self.size == 0:
            return Exception("에러")
        else:
            # 사이즈 1 의 경우 이전값에서 다 걸러짐
            prev_node = n.prev_ref
            next_node = n.next_ref
            
            # 연결을 n 앞뒤로 변경한다.
            prev_node.next_ref = next_node
            next_node.prev_ref = prev_node
    
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
    
    def print_reserve(self):
        if self.size == 0:
            print('[]')
        else:
            tail_node = self.tail
            print_list = []
            while tail_node:
                print_list.append(tail_node.value)
                tail_node = tail_node.prev_ref
            print(f"print_list = {print_list}")

node_test = NodeList()
node_test.add_front(1)
node_test.add_front(2)
node_test.add_front(3)
node_test.add_front(4)
node_test.insert_prev(node_test.search_second_node(), 7)  # print_list = [4, 7, 3, 2, 1]
node_test.remove(node_test.search_second_node())
node_test.remove(node_test.search_second_node())
node_test.print()
node_test.print_reserve()
