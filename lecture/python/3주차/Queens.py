"""
 *packageName    :
 * fileName       : Queens
 * author         : ipeac
 * date           : 2022-12-03
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-03        ipeac       최초 생성
 """
n, m = map(int, input().split())  # n  n* n 크기의 판이 존재한다.
remaining_queen = n - m

row = [0] * n
visited = [0] * n

for i in range(n):
    input_value = list(map(str, input().split()))
    print(f"input_value = {input_value}")
    if 'Q' in input_value:
        row[i] = input_value.index('Q')
print(f"row = {row}")

def check_queen(x):
    for i in range(x):  # 모든 열에 이쓴ㄴ
    
    pass

def make_queen(x, cnt):  # row 배열의 x 위치에 값을 하나씩 넣어본다.
    if cnt == remaining_queen + 1:  # cnt 가 남은 퀸 수+1 값과 동일하다면 해당 모두 놓았으며 가능한 수가 있다는 의미임
        print('true')
        return
    for i in range(n):
        row[x] = i  # 세로값을 하나하나씩 넣어서 테스트해본다.
        if check_queen(x):
            make_queen(x + 1, cnt + 1)  # 열 이동 , 카운트 +1
