"""
 *packageName    :
 * fileName       : 알고리즘 경진대회
 * author         : ipeac
 * date           : 2022-12-19
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-19        ipeac       최초 생성
 """
import bisect

class TreeNode:
    def __init__(self, parent=None, element=None, left=None, right=None):
        self.parent = parent
        self.element = element
        self.left = left
        self.right = right
    
    # 부모 설정 함수
    def set_parent(self, parent):
        self.parent = parent
    
    # 좌 우 좌 작은수 우 큰수
    def judge(self, value):
        pass

T = int(input())  # 테스트 케이스
for _ in range(T):
    ans = 0
    num_arr = []
    # print("==========================================")
    N, Q, = map(int, input().split())  # N (사람수) Q (사람수 + 상품주는 횟수)
    gift_cnt = Q - N
    # 1(입력)     A(ID)       B(점수)
    # 2(상품 추첨)          K(등수)
    for case in range(Q):
        input_arr = list(map(int, input().split()))
        if input_arr[0] == 1:  # 상품 입력
            id = input_arr[1]
            score = input_arr[2]
            index = bisect.bisect_left(num_arr, score, key=lambda x: x[1])
            num_arr.insert(index, [id, score])
        
        
        else:  # 2
            # print("==========================================")
            k = input_arr[1]
            # print(f"k = {k}")
            ans += num_arr[-k][0]
            gift_cnt -= 1
            if not gift_cnt:
                break
            # print(f"num_arr = {num_arr}")
            # print(f"num_arr[-k][0] = {num_arr[-k][0]}")
    
    print(ans)
