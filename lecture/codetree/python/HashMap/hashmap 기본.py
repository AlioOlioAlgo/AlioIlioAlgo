"""
 *packageName    : 
 * fileName       : dictionary
 * author         : ipeac
 * date           : 2023-02-17
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-02-17        ipeac       최초 생성
 """
n = int(input())
dic = dict()

for i in range(n):
    function = input()
    if function.startswith("add"):
        _, key, value = function.split(" ")
        dic[key] = value
    elif function.startswith("find"):
        _, key = function.split(" ")
        value = dic.get(key)
        if value is None:
            print("None")
        else:
            print(value)
    
    else:
        _, key = function.split(" ")
        dic.pop(key)
