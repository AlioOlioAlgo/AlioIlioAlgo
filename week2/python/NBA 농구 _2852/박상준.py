"""
 *packageName    : 
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-10-24
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-24        ipeac       최초 생성
 """

n = int(input())
scores = []

for i in range(n):
    scores.append(input().split())
scores = sorted(scores, key=lambda x: x[1])
scores.append([-1, '48:00'])

print(f"scores = {scores}")

one, two = 0, 0
pivot = ''
one_ans, two_ans = 0, 0
for team, time in scores:
    if one == two:
        pass
    elif one > two:
        min_, sec = map(int, time.split(":"))
        min_p, sec_p = map(int, pivot.split(":"))
        one_ans += (min_ * 60 + sec) - (min_p * 60 + sec_p)
    else:
        min_, sec = map(int, time.split(":"))
        min_p, sec_p = map(int, pivot.split(":"))
        two_ans += (min_ * 60 + sec) - (min_p * 60 + sec_p)
    pivot = time
    if int(team) == 1:
        one += 1
    elif int(team) == 2:
        two += 1
q, r = divmod(one_ans, 60)
print(f"q, r = {q, r}")
# print(str(q).zi)
