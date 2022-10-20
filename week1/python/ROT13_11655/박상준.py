"""
 *packageName    : 
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-10-19
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-19        ipeac       최초 생성
 """
# A~Z 65 79 a-z 97 122
s = input()
# s = "Baekjoon Online Judge"
ans = ''

# 아스키 코드 값 비교
def judge(value, max_value, min_value):
    global ans
    # 아스키 코드 기준 +13 으로 알파벳의 인덱스를 밀어냅니다.
    ord_value = ord(value) + 13
    # 만약 upper lower case 에서 해당 값이 대 소문자 max 아스키 value 보다 크다면
    # 제일 낮은 아스키 값부터 max값과의 차이를 min 값에 더해주면! 13자리 밀린 값이 완성됩니다.
    if ord_value > max_value:
        ord_value = min_value + (ord_value - max_value)-1
    # 아스키 값을 다시 문자형으로 변경해서 ans에 더하기
    ans += chr(ord_value)

for value in s:
    # 알파벳이냐.. 대소문자냐 구별하기위해서 + 자바의 경우는 그냥 아스키 값 자체로 비교하면될듯
    if value.isalpha() and value.isupper():
        judge(value, 90, 65)
    elif value.isalpha() and value.islower():
        judge(value, 122, 97)
    else:
        ans += value
print(ans)
