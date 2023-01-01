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
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [0 for _ in range(self.capacity)]
        self.size = 0
    
    def min(self):
        pass
    
    def remove_min(self):
        pass
    
    def add(self, element):
        if self.size > self.capacity:
            raise Exception("힙의 최대 사이즈 초과")
        self.size += 1
        self.array[self.size] = element
        
        current = self.size
        
        while self.array[current] < self.array[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)
    
    def length(self):
        return self.size
    
    def parent(self, i):
        if i < 0 or i > self.length():
            raise Exception("힙의 최대 사이즈 초과")
        return i // 2
    
    def print_arr(self):
        print(f'힙어레이 => {self.array}')
    
    def swap(self, swap_index1, swap_index2):
        self.array[swap_index1], self.array[swap_index2] = self.array[swap_index2], self.array[swap_index1]

min_heap = MinHeap(20)

min_heap.add(4)
min_heap.add(5)
min_heap.add(6)
min_heap.add(15)
min_heap.add(9)
min_heap.add(7)
min_heap.add(16)
min_heap.add(25)
min_heap.add(14)
min_heap.add(12)
min_heap.add(11)
min_heap.add(13)
min_heap.add(20)
min_heap.print_arr()
min_heap.add(2)
min_heap.print_arr()
