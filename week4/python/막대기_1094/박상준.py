"""
 *packageName    :
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-11-06
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-06        ipeac       최초 생성
 """
x = int(input())
stack = [64]

while True:
    if sum(stack) == x:
        print(len(stack))
        exit()
    # 가지고 있는 막대의 길이의 합이 x보다 크다면
    if sum(stack) >= x:
        # 가지고있는 막대 중 길이가 가장 짧은 것을 절반으로 자른다.
        div = stack.pop() // 2
        # 만약, 위에서 자른 막대의 절반 중 하나를 버리고 남아있는 막대의 길이의 합이 X보다 크거나 같다면,
        # 위에서 자른 막대의 절반 중 하나를 버린다.
        stack.append(div)
        if sum(stack) >= x:
            continue
        stack.append(div)
