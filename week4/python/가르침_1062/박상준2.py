"""
 *packageName    :
 * fileName       : 박상준2
 * author         : ipeac
 * date           : 2022-11-10
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-10        ipeac       최초 생성
 """
from itertools import combinations

n, k = map(int, input().split())
base = ['a', 'n', 't', 'i', 'c']  # 5개의 필수 요소
# 안배운 단어 모음집
alpha = set(chr(i) for i in range(ord('a'), ord('z') + 1)) - set(base)
word = [input().rstrip()[4:-4] for _ in range(n)]
# print(f"word = {word}")
# word = ['rc', 'hello', 'car']
ans = 0

def can_read(word, learned):
    count = 0
    # 단어 마다
    for w in word:
        # 읽을 수 있는지?
        readable = True
        # 각 알파벳이 learned 안에 있는지 체크한다.
        for c in w:
            # 없으면 readable false 처리
            if not learned[ord(c)]:
                readable = False
                break
        # 리더블이 true 라면 사전에 존재하는 단어이다.
        if readable:
            count += 1
    return count

if k >= 5:
    learned = [False] * 150
    for b in base:
        learned[ord(b)] = True
    for combi in combinations(alpha, k - 5):  # 필수요소 제외 알파벳중에 k-5 개를 고려한다.
        for c in combi:
            learned[ord(c)] = True
        count = can_read(word, learned)
        for c in combi:
            learned[ord(c)] = False
        ans = max(ans, count)
    print(ans)
else:
    # 5보다 작으면 필수 요소를 채울 수 없기에
    print(0)
