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
T = int(input())  # 테스트 케이스
for _ in range(T):
    ans = 0
    diction = {}
    # print("==========================================")
    N, Q = map(int, input().split())  # N (사람수) Q (사람수 + 상품주는 횟수)
    # 1(입력)     A(ID)       B(점수)
    # 2(상품 추첨)          K(등수)
    for case in range(Q):
        input_arr = list(map(int, input().split()))
        if input_arr[0] == 1:
            id = input_arr[1]
            score = input_arr[2]
            diction[id] = score
            diction = dict(sorted(diction.items(), key=lambda x: -x[1]))
            # print(f"diction = {diction}")
            pass
        else:
            k = input_arr[1]
            # print(f"k = {k}")
            # print(f"diction = {list(diction.keys())}")
            ans += list(diction.keys())[k - 1]
    print(ans)
