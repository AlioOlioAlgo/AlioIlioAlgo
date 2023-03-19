"""
 *packageName    : 
 * fileName       : 16897.계란으로 계란치기
 * author         : ipeac
 * date           : 2023-03-04
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-03-04        ipeac       최초 생성
"""
n = int(input())
eggs = [
    list(map(int, input().split()))
    for _ in range(n)
]
# print(f"eggs  ==> {eggs}")
# print("======================================================")

ans = 0

def dfs(idx, eggs):
    global ans
    if idx == n - 1:
        ans = max(ans, sum([1 for i in eggs if i[0] <= 0]))
        return
    if eggs[idx][0] <= 0:  # 손에 들고 있는 계란이 깨진 경우 다음으로 ..
        dfs(idx + 1, eggs)
        return
    
    for i in range(n):
        if i != idx and eggs[i][0] > 0:  # 나 자신이 아니고, 왼손에 든 계란이 내구도가 다 떨어진 계란이 아니여야합니다.
            eggs_copy = [i[:] for i in eggs]
            print(f"eggs_copy  ==> {eggs_copy}")
            eggs_copy[idx][0] -= eggs_copy[i][1]
            eggs_copy[i][0] -= eggs_copy[idx][1]
            
            if eggs_copy[idx][0] <= 0:
                eggs_copy[idx] = [0, 0]
            
            if eggs_copy[i][0] <= 0:
                eggs_copy[i] = [0, 0]
            
            dfs(idx + 1, eggs_copy)

dfs(0, eggs)
print(ans)
