"""
 *packageName    :
 * fileName       : 763.Partition Labels
 * author         : ipeac
 * date           : 2023-01-08
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-01-08        ipeac       최초 생성
 """
from typing import *

def partitionLabels(s: str) -> List[int]:
    alpha = {s[i]: i for i in range(len(s))}
    print(f"alpha = {alpha}")

partitionLabels("ababcbacadefegdehijhklij")
