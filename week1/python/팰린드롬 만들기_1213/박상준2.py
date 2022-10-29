"""
 *packageName    : 
 * fileName       : 박상준2
 * author         : ipeac
 * date           : 2022-10-27
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-27        ipeac       최초 생성
 """
# print(f"word = {word}")
from collections import Counter, deque

word = input()

# word = 'ABACABA'
word_counter = sorted(list(Counter(word).items()), key=lambda x: x[0], reverse=True)
ans = deque()
odd_cnt = 0
odd_value = ''
for word, count in word_counter:
    if count % 2 != 0:
        odd_cnt += 1
        odd_value = word
        
        if odd_cnt >= 2:
            print("I'm Sorry Hansoo")
            exit()
        
        for i in range(count // 2):
            ans.appendleft(word)
            ans.append(word)
    
    else:
        repeat = count // 2
        for i in range(repeat):
            ans.appendleft(word)
            ans.append(word)

if odd_value:
    ans.insert(len(ans) // 2, odd_value)
print(''.join(ans))
