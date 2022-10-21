"""
 *packageName    : 
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-10-21
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-21        ipeac       최초 생성
 """
n = int(input())
words = [
    input()
    for _ in range(n)
]
# print(f"n = {n}")
# print(f"words = {words}")
# n = 3
# words = [['A', 'B', 'A', 'B'], ['A', 'A', 'B', 'B'], ['A', 'B', 'B', 'A']]
# n = 3
# words = ['ABAB', 'AABB', 'ABBA']
ans = 0
for word in words:
    stack = []
    for i in range(len(word)):
        if stack:
            if stack[-1] == word[i]:
                stack.pop()
            else:
                # 스택의 값이 그 다음 값과 다르다면
                stack.append(word[i])
        else:
            #  스택이 비어있다면 스택에 같은 값을 검증할 값을 담습니다.
            stack.append(word[i])
    if not stack:
        ans += 1
print(ans)
