"""
 *packageName    : 
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-10-20
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-20        ipeac       최초 생성
 """
# 반례 몰라서 질문찾아봄;

n = int(input())
pattern = input()
words = [
    input()
    for _ in range(n)
]

# * 기준으로 앞 뒤 나눈다.
pattern_start, pattern_end = pattern.split("*")

for word in words:
    ## 여기가 제일 중요할듯.
    #  패턴의 양끝의 길이 보다 단어의 길이가 짧다면
    # 앞 뒤 패턴이 서로 겹치는 문자가 발생한다.
    if len(word) < len(pattern_start) + len(pattern_end):
        print("NE")
        continue
        # 단어의 앞과 뒤를 검증하는 로자ㅣㄱ
    if word.startswith(pattern_start) and word.endswith(pattern_end):
        print("DA")
    else:
        print("NE")
