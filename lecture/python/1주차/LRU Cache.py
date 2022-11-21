"""
 *packageName    :
 * fileName       : LRU Cache
 * author         : ipeac
 * date           : 2022-11-21
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-21        ipeac       최초 생성
 """

class LRUCache:
    dic = {}
    
    def __init__(self, capacity: int):
        this.capacity = capacity  # 초기 용량 할당
    
    def get(self, key: int) -> int:
        if key in dic:  # O(1)
            return dic[key]
        else:
            return -1
    
    def put(self, key: int, value: int) -> None:
        if len(dic) == capacity:
            del dic[0]  # O(1) <- 첫번째 인덱스 값을 지우기 때문
        dic[key] = value
    # Your LRUCache object will be instantiated and called as such:

# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
keys = input()
values = input()
# print(keys)
# print(values)

obj = None
ans = []
for idx, key in enumerate(keys):
    if key == "LRUCache":
        obj = LRUCache(values[idx])
        ans.append("null")
    elif key == "put":
        obj.put(values[idx])
        ans.append("null")
    elif key == "get":
        ans.append(obj.get(values[idx]))
print(*ans)
