"""
 *packageName    : 
 * fileName       : 이상한 진수2
 * author         : ipeac
 * date           : 2023-02-15
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-02-15        ipeac       최초 생성
"""
a = list(map(str, input()))
# print(f"a  ==> {a}")
tmp_a = []
zero_check = False

def make_big_number():
    global zero_check
    global tmp_a
    for integer in a:
        if not zero_check and integer == "0":
            tmp_a.append("1")
            zero_check = True
        else:
            tmp_a.append(integer)
    print(f"tmp_a  ==> {tmp_a}")
    # print(f"zero_check  ==> {zero_check}")
    # 1111 <- 입력으로 주어진 경우

make_big_number()
string = ""
if not zero_check:
    for i in range(len(a) - 1):
        string += "1"
    string += "0"
    print(int(string, 2))

else:
    tmp_a = "".join(tmp_a)
    print(int(tmp_a, 2))
