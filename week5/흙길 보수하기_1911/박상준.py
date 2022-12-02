"""
 *packageName    :
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-11-30
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-30        ipeac       최초 생성
 """
n, pool_size = map(int, input().split())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]
arr.sort(key=lambda x: x[0])
print(f"arr = {arr}")
max_end = 0
ans = 0
for idx, a, in enumerate(arr):
    print("==========================================")
    if idx == 0:
        max_end = a[1]
    else:
        print(f"max_end = {max_end}")
        if max_end > a[0]:  # 제일긴 호수의 뒷값이 현재 내 호수의 시작점보다 뒤라면 해당 값만큼 시작점을 증가시켜야한다.
            a[0] += max_end - a[0]
            print(f"a[0] = {a[0]}")
    
    pool_length = a[1] - a[0]
    print(f"pool_length = {pool_length}")
    if pool_length <= 0:  # 호수의 길이가 0이하면 그냥 연산할 이유조차 없음
        continue
    
    if pool_length % pool_size == 0:
        print("나눠짐")
        ans += pool_length // pool_size
        print(f"ans = {ans}")
    elif pool_length % pool_size != 0:  # 나머지가 존재한다면
        print('안됨')
        a[1] += pool_size - (pool_length % pool_size)  # 끝자리를 나머지만큼 증가시켜줍니다.
        ans += pool_length // pool_size + 1
        print(f"ans = {ans}")
    print(f"a = {a}")
    max_end = max(a[1], max_end)
print(ans)
