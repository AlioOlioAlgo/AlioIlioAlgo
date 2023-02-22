"""
 *packageName    : 
 * fileName       : 순서를 바꾸었을 때 같은 단어 그룹화하기
 * author         : ipeac
 * date           : 2023-02-18
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-02-18        ipeac       최초 생성
"""
from collections import defaultdict

n = int(input())
words = [
    input()
    for _ in range(n)
]
count = defaultdict(int)
for idx, word in enumerate(words):
    word_arr = list(map(str, word))
    word_arr = sorted(word_arr)
    count[''.join(word_arr)] += 1
print(f"count  ==> {count}")
count = sorted(count.items(), key=lambda x: -x[1])
print(count[0][1])
