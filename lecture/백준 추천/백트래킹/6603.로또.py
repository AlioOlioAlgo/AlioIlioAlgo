"""
 *packageName    : 
 * fileName       : 6603.로또
 * author         : ipeac
 * date           : 2023-03-15
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-03-15        ipeac       최초 생성
 """

def make_lotto(idx, selected):
    if len(selected) == 6:
        print(' '.join(map(str, selected)))
        return
    if idx == k:
        return

    selected.append(arr[idx])
    make_lotto(idx + 1, selected)
    selected.pop()
    make_lotto(idx + 1, selected)

while True:
    line = list(map(int, input().split()))
    if line[0] == 0:
        break
    k = line[0]
    arr = list(line[1:])
    make_lotto(0, [])
    print()
