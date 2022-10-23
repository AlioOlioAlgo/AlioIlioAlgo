"""
 *packageName    : 
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-10-23
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-23        ipeac       최초 생성
 """
n = int(input())
find = [list(input()) for _ in range(n)]
ans = []
for word_q in find:
    tmp = ''
    for w in word_q:
        if w.isdigit():
            tmp += w
        else:
            if tmp:
                ans.append(int(tmp))
                tmp = ''
    if tmp:
        ans.append(int(tmp))

ans.sort()
for i in ans:
    print(i)
