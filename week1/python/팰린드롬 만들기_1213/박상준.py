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
from collections import Counter, deque

n = list(input())
# n = ['A', 'B', 'A', 'C', 'A', 'B', 'A']
answer = deque()

# 각 알파벳 각 출현 개수들을 리스트에 담고 사전순 반대로 정렬한다.
counter = sorted(list(Counter(n).items()), reverse=True)
print(f"counter = {counter}")

# 홀수 카운트를 위한 변수
odd_count = 0
# 홀수 알파벳을 담기위함 => 마지막에 중간 위치에 인풋하기위함
odd_index = 0

# enumerate 로 해당 idx 기억
for idx, combi, in enumerate(counter):
    print("==========================================")
    key, value = combi[0], combi[1],  # 알파벳 key  ,알파벳의 개수
    print(f"key,value = {key, value}")
    # 홀수 체크
    if value % 2 != 0:
        odd_count += 1
        
        # 해당 알파벳의 출현 빈도가 2이상이라면
        if value >= 2:
            # 한번에 앞 뒤로 넣어준다. > value // 2 만큼 수행해야함
            for i in range(value // 2):
                answer.appendleft(counter[idx][0])
                answer.append(counter[idx][0])
                print(f"answer = {answer}")
        # 홀수가 2개 이상이라면 팰린드롬이 성립하지 않는다.
        if odd_count >= 2:
            print("I'm Sorry Hansoo")
            exit()
        # 마지막 삽입을 위한 문자 기억
        odd_index = key
    else:
        for i in range(value // 2):
            answer.appendleft(counter[idx][0])
            answer.append(counter[idx][0])
            print(f"answer = {answer}")
# odd_index 가 0 이 아니라면 홀수인 알파벳의 개수가 존재했다는 의미고
# 해당 의미 => 중간 answer 인덱스에 홀수 알파벳을 삽입!
if odd_index != 0:
    answer.insert(len(answer) // 2, odd_index)
for value in answer:
    print(value, end="")
