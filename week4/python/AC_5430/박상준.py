"""
 *packageName    :
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-11-08
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-08        ipeac       최초 생성
 """
import sys

input = sys.stdin.readline
t = int(input())
while t:
    # print("==========================================")
    function = list(map(str, input()))[:-1]
    # print(f"function = {function}")
    reverse_count = function.count('R')
    flag = False
    n = int(input())
    arr = input()
    arr = arr[1:len(arr) - 2].split(",")
    if len(arr) == 1 and arr[0] == '':
        print('error')
        continue
    # print(f"arr = {arr}")
    for func in function:
        if func == 'R' and reverse_count >= 0 and reverse_count % 2 != 0:
            arr.reverse()
            reverse_count -= 2
        elif func == 'D':
            # print(f"function = {function}")
            # print(f"len(arr) = {len(arr)}")
            if len(arr) == 0:
                print('error')
                flag = True
                break
            else:
                arr = arr[1:]
    if not flag:
        arr = list(map(int, arr))
        print(arr)
