"""
 *packageName    :
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-12-06
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-06        ipeac       최초 생성
 """
command = list(map(int, input().split()))  # 이동할 위치에 대한 배열
horse = [[0, 0] for _ in range(4)]  # 4개의 말에 대한 정보를 저장할 리스트 [몇번의 road에 있는지 체크, road 안의 인덱스 위치]

def dfs(save_horse, command, index, score):  # n  경우의 수 score 점수 horse 몇번째 말을 움직이고 있는 지에 대한 정보이다.
    global max_score
    if index == 10:  # 10가지의 경우의 수가 존재한다. 10가지를 전부 돈 경우
        max_score = max(score, max_score)
        return
    # 4개의 말에 대해 각각 이동을 시킴으로 > 완전 탐색을 진행한다.
    for h in range(4):
        if save_horse[h][0] == -1:  # h 로드에 있는 말이 도착한 말이라면 연산을 무시한다.
            continue
        save_horse[h][1] += command[index]
        hx, hy = save_horse[h][0], save_horse[h][1]
        
        if hy >= len(board[hx]):  # 도착점을 넘은 경우임
            save_horse[h][1] = -1
            dfs(save_horse, command, index + 1, score)
            save_horse[h][0] = hx  # 백트래킹
            save_horse[h][1] -= command[index]
        else:  # 도착점을 넘지 않은 경우
            if hx == 0 and board[hx][hy] % 10 == 0 and board[hx][hy] != 40:
                save_horse[h][0] += board[hx][hy] // 10  # 10인 경우 1로 20인 경우 2 로 30인 경우 3road 의 경우의 수를 타게된다.
            is_duple = False
            for i in range(4):
                if i == h:
                    continue
                cx, cy = save_horse[i][0], save_horse[i][1]
                if cx == -1:
                    continue
                if (hx != 0 and cx != 0) and ()

board = [
    [i for i in range(42, 2)],
    [2, 4, 6, 8, 10, 13, 16, 19, 25, 30, 35, 40],
    [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 25, 30, 355, 40],
    [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 28, 27, 26, 25, 30, 35, 40]
]
max_score = 0  # 최대 점수 기산
# horse [ road에 대한 인덱스, 어떤 road 인지]

play(horse, )
