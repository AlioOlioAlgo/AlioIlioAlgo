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

class MinHeap():  # 최소힙 ㅇㅇ.
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [0 for _ in range(self.capacity)]
        self.size = 0
    
    def min(self):
        return self.array[1]
    
    def _parent(self, j):
        return (j - 1) // 2  # 부모 노드 탐색
    
    def heapify(self, arr):
        arr.insert(0, 0)
        self.array = arr
        self.size = len(arr) - 1
        start = self._parent(self.size)  # 가장 뒤의 어레이의 부모부터 시작한다.
        
        for j in range(start, -1, -1):
            self._downheap(j)
    
    # 왼 오 자식 인덱스가 배열의 길이를 넘지 않았는지 체크하는 함수임.
    def _has_right(self, j):
        return self._right(j) < self.length()
    
    def _has_left(self, j):
        return self._left(j) < self.length()
    
    def _left(self, j):
        return 2 * j + 1
    
    def _right(self, j):
        return 2 * j + 2
    
    def _downheap(self, j):
        print(f"self.length() = {self.length()}")
        if self._has_left(j):
            left = self._left(j)  # 왼쪽 인덱스를 구합니다.
            small_child = left
            if self._has_right(j):
                right = self._right(j)
                if self.array[right + 1] < self.array[left + 1]:
                    small_child = right
            if self.array[small_child + 1] < self.array[j + 1]:
                self.swap(j + 1, small_child + 1)
                self._downheap(small_child)
    
    def remove_min(self):
        if not self.length():
            raise Exception("빈 배열")
        self.array[1] = 0
        self.swap(1, self.size)
        self.size -= 1
        
        # 왼쪽 노드 open 여부 확인
        self._downheap(0)
    
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

heap = MinHeap(100)
arr = [10, 9, 8, 6, 7]
heap.heapify(arr)
heap.print_arr()
