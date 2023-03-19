"""
 *packageName    : 
 * fileName       : hashmap 기본
 * author         : ipeac
 * date           : 2023-02-16
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-02-16        ipeac       최초 생성
"""
n = int(input())
words = [
    input()
    for _ in range(n)
]
print(f"words  ==> {words}")
remem_list = []

def is_carry(param_list):
    print(f"param_list  ==> {param_list}")
    for i in range(1, 5):
        print("======================================================")
        value = 0
        for j in range(3):
            if len(param_list[j]) >= i:
                value += int(param_list[j][-i])
                print(f"value  ==> {value}")
        if value >= 10:
            return False
    return True

ans = -1

def make_list(idx, cnt):
    global ans
    if cnt == 3:
        if is_carry(remem_list):
            print(f"remem_list  ==> {remem_list}")
            ans = max(ans, sum([int(num) for num in remem_list]))
            pass
        return
    
    for i in range(idx, n):
        remem_list.append(words[i])
        make_list(i + 1, cnt + 1)
        remem_list.pop()

make_list(0, 0)
print(ans)
