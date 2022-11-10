"""
 *packageName    :
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-11-10
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-10        ipeac       최초 생성
 """
from itertools import combinations

word_num, letter_num = map(int, input().split())
answer = 0
alphabet = set(chr(i) for i in range(97, 123)) - {'a', 'n', 't', 'i', 'c'}
words = [input().rstrip()[4:-4] for _ in range(word_num)]

# print(f"words = {words}")
# words = ['rc', 'hello', 'car']

def isit_readable(words, learned):
    count = 0
    for word in words:
        can_read = True
        for w in word:
            # 안배운 알파벳이 존재한다면 false 처리
            if not learned[ord(w)]:
                can_read = False
                break
        if can_read:
            count += 1
    return count

if letter_num >= 5:
    learned = [False] * 150
    for x in {'a', 'n', 't', 'i', 'c'}:
        learned[ord(x)] = True
    
    # 남은 알파벳 중에 k-5개를 선택해본다.
    for teach in list(combinations(alphabet, letter_num - 5)):
        # 가르칠 알파벳 하나씩 반복
        for t in teach:
            learned[ord(t)] = True
        count = isit_readable(words, learned)
        answer = max(answer, count)
        # 백트래킹
        for t in teach:
            learned[ord(t)] = False
    print(answer)
else:
    print(0)
