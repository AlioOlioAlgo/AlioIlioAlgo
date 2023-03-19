"""
 *packageName    :
 * fileName       : 정수명령처리6
 * author         : ipeac
 * date           : 2022-12-26
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-26        ipeac       최초 생성
 """
import heapq

class PriorityQueue:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        heapq.heappush(self.items, -item)
    
    def pop(self):
        if not len(self.items):
            raise Exception("배열이 비어있습니다.")
        print(-heapq.heappop(self.items))
    
    def size(self):
        print(len(self.items))
    
    def empty(self):
        if not len(self.items):
            print(1)
            return
        print(0)
    
    def top(self):
        if not len(self.items):
            raise Exception("배열이 비어있습니다.")
        print(-self.items[0])

n = int(input())
ans = PriorityQueue()
for _ in range(n):
    input_list = input().split()
    if input_list[0] == 'push':
        PriorityQueue.push(ans, int(input_list[1]))
    elif input_list[0] == 'pop':
        PriorityQueue.pop(ans)
    elif input_list[0] == 'size':
        PriorityQueue.size(ans)
    elif input_list[0] == 'empty':
        PriorityQueue.empty(ans)
    elif input_list[0] == 'top':
        PriorityQueue.top(ans)
