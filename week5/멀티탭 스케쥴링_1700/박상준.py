"""
 *packageName    :
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-11-28
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-28        ipeac       최초 생성
 """
# n  멀티 탭의 구멍의 갯수 k  전기 용품의 총 사용 횟수

n, k = map(int, input().split())
electron = list(map(int, input().split()))

current_use = set()
ans = 0
for idx, item in enumerate(electron):  # 아이템을 꽂는다.
    print("==========================================")
    print(f"idx,item = {idx, item}")
    print(f"current_use = {current_use}")
    print(f"electron[idx+1:] = {electron[idx + 1:]}")
    if len(current_use) < n:
        current_use.add(item)
    else:  # 현재 사용중인 포트가 꽉참
        print("꽉참")
        if item in current_use:
            print("패스")
            continue  # 패스함
        elif item not in current_use:  # 현재 진행중인 아이템이 사용중인 포트에 없음
            save_idx = -1
            # 대기열에 존재하지 않는 아이템을 빼고 현재 아이템을 넣는다.
            for value in current_use:
                print(f"value = {value}")
                if value not in electron[idx + 1:]:  # 대기열에 존재하지 않는 아이템인 경우 제거 대상임
                    print("제거")
                    print(f"item = {item}")
                    current_use.discard(value)
                    current_use.add(item)
                    ans += 1
                    break
                # 대기열에 해당 값이 존재하는 경우에는 for value in current_use를 돌면서 가장 늦게 등장하는 요소를 제거해 줘야한다.
                elif value in electron[idx + 1:]:
                    save_idx = max(save_idx, electron[idx + 1:].index(value))
                    print(f"save_idx = {save_idx}")
            else:  # break없이 정상적으로 대기열의 값을 모두 저장한 경우에는 해당 save_idx 값을 discard 하고 electron[save_idx] 값을 투입한다.
                print("for 의 else")
                print(f"electron[save_idx] = {electron[save_idx]}")
                print(f"item = {item}")
                current_use.discard(electron[idx + 1:][save_idx])
                current_use.add(item)
                ans += 1
print(ans)
