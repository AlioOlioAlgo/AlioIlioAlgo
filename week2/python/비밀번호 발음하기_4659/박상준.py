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
mo = ['a', 'e', 'i', 'o', 'u']
za = ['q', 'w', 'r', 't', 'y', 'i', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
while True:
    word = list(word_i := input())
    if word_i == 'end':
        exit()
    # 모음 개수 카운트용
    mo_count = 0
    # 모음과 자음의 연속성 체크
    mo_seq = 0
    za_seq = 0
    
    for idx, w in enumerate(word):
        # idx 0 인경우 앞뒤 체크 x 1 부터만
        if idx != 0:
            idx_ = word[idx] + word[idx - 1]
            # 3번 조건
            if word[idx] == word[idx - 1] and (word[idx] + word[idx - 1] != 'ee' and word[idx] + word[idx - 1] != 'oo'):
                print(f'<{word_i}> is not acceptable.')
                break
        # 모음인 경우 자음 연속성 제거 , 모음 개수 +1 , 모음 연속성 +1
        if w in mo:
            za_seq = 0
            mo_count += 1
            mo_seq += 1
        # 반대
        else:
            mo_seq = 0
            za_seq += 1
        # 자 모 가 연속성이 3이상이면 X
        if za_seq >= 3 or mo_seq >= 3:
            print(f'<{word_i}> is not acceptable.')
            break
        # 마지막인 경우 모음 카운트가 0 이면 안됨. 그외 OK
        if idx == len(word) - 1:
            if mo_count == 0:
                print(f'<{word_i}> is not acceptable.')
                break
            print(f'<{word_i}> is acceptable.')
            break
