"""
 *packageName    :
 * fileName       : Array Based Min Heap
 * author         : ipeac
 * date           : 2023-01-01
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-01-01        ipeac       최초 생성
 """

class MinHeap:  # 최소힙 ㅇㅇ.
    def __init__(self):
        self.array = []
        self.size = 0
    
    def min(self):
        pass
    
    def remove_min(self):
        pass
    
    def add(self, element):
        pass
    
    def length(self):
        return self.size
    
    def parent_node(self, i):
        if i < 0 or i > self.length():
            raise Exception("힙의 길이를 벗어났습니다.")
        return
