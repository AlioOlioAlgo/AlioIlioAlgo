"""
 *packageName    :
 * fileName       : 박상준2
 * author         : ipeac
 * date           : 2023-01-01
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-01-01        ipeac       최초 생성
 """
n = int(input())
line_list = sorted(list(map(int, input().split())) for _ in range(n))
# print(f"line_list = {line_list}")
length = line_list[0][1] - line_list[0][0]

end_length = line_list[0][1]  # 이전 값의 끝점

for idx in range(1, len(line_list)):
    # print(f"start,end = {start, end}")
    if line_list[idx][1] <= end_length:  # 끝길이보다 작은 end 라면 총길이에도 별 차이가 없을 것이다.
        continue
    elif line_list[idx][0] < end_length < line_list[idx][1]:
        length += line_list[idx][1] - end_length
        end_length = line_list[idx][1]
    elif end_length <= line_list[idx][0]:
        length += line_list[idx][1] - line_list[idx][0]
        end_length = line_list[idx][1]

print(length)
