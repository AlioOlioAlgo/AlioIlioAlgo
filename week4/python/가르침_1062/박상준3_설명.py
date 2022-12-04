"""
 *packageName    :
 * fileName       : 박상준3
 * author         : ipeac
 * date           : 2022-12-03
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-03        ipeac       최초 생성
 """
from itertools import combinations

n, k = map(int, input().split())  # n   단어의 개수 k    가르칠 수 있는 글자의 개수
must_learned = ['a', 'n', 't', 'i', 'c']
# 단어는 영어 소문자로 이루어져있다. >
not_learned_word_list = set([chr(i) for i in range(ord('a'), ord('z') + 1)]) - set(must_learned)  # 아직 배우지 않는 글자의 리스트
print(f"not_learned_word_list = {not_learned_word_list}")
words = [
    input()
    for _ in range(n)
]

# 배울 수 있는 단어에서 일단 5개를 빼면 현재 배울 수 있는 글자의 개수가 된다.
can_learn_word_cnt = k - len(must_learned)
# print(f"can_learn_word_cnt = {can_learn_word_cnt}")
# print(f"words = {words}")
#
# 일단 필수 단어 요소를 못채우는 경우는 절대 남극의 단어를 읽을 수 없다.
learn = [0 for _ in range(26)]  # 알파벳 갯수만큼 일단 0 배열을 생성한다.

for must_word in must_learned:  # 필수적으로 배워야하는 글자를 learned 에 체크해서 넣어준다. 소문자 아스키 'a' 는 97  'z'는 122 까지이다.
    # 0부터 기록하기 위해서 -97 을 빼줘야한다.
    learn[ord(must_word) - 97] = 1
print(f"learn = {learn}")  # 체크완료 필수단어는 learned가 체크되었다.

def can_read(word, leared_arr):
    #  단어를 읽을 수 있는지 여부를 체크한다.
    for w in word:
        print(f"w = {w}")
        if leared_arr[ord(w) - 97]:
            pass
        else:
            return False
    return True

pass
ans = 0

if k >= 5:
    # 이전 선언한 배열을 복사한 새로운 임시 배열을 가진다.
    # 필수단어를 채울 수 있는 경우는 내가 배워야하는 단어들을 하나하나씩 꺼내서 조합해본다. 해당 단어 조합한 반복횟수중에 가장 많은 단어를 배울 수 있는 경우는 답안으로 생각하면된다.
    # 일단은 내가 배운 단어를 기록해야하니.  내가 배운 단어를 체크하기 위하여 learned 라는 배열을 선언후 필수 글자를 기록한다. >  해당 배열은 if 문 밖에 기록하는 것이 반복적인 연산을 > 줄일 것이라 생각했는데 > 잘못 생각한거임 어차피 learned 배열을 초기화시켜야함
    # [추가] 생각해보니 그냥 이전에 반복 돌린 배열을 깊은 복사로 들고와서 사용하는게 코드가 깔끔해보였다.
    #
    # 내가 새로 배울 수 있는 횟수만큼 | 배울 수 있는 배열안에서 조합을 돌린다. 그 단어를 배운다는 가정하에 몇개의 단어를 읽을 수 있는지 체크하는 함수를 만들어야 한다.
    #
    for combi in combinations(not_learned_word_list, k - 5):
        tmp_learned_arr = learn[:]
        
        print("==========================================")
        print(f"combi = {combi}")
        for c in combi:
            tmp_learned_arr[ord(c) - 97] = 1
        print(f"tmp_learned_arr = {tmp_learned_arr}")
        
        cnt = 0
        
        for word in words:
            if not can_read(word, tmp_learned_arr):
                print("읽을수 없었음")
                continue
            else:
                print("읽을 수 있었음")
                cnt += 1
        if cnt == n:  # 만약에 cnt 가 단어의 최대 갯수라면 그대로 프린트하고 종료함
            print(n)
            exit()
        ans = max(ans, cnt)  # 최대로 많이 읽을 수 있는 단어를 리턴한다.
    
    print(ans)
else:
    print(0)
