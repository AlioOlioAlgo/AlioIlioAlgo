"""
 *packageName    :
 * fileName       : 박상준2
 * author         : ipeac
 * date           : 2022-12-23
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-23        ipeac       최초 생성
 """
import collections
import sys

input = sys.stdin.readline

def suffixSum(arr, l):
    default = collections.defaultdict(int)
    for i in range(l):
        suffix = 0
        for cur in arr[i:] + arr[:i]:
            suffix += cur
            default[suffix] += 1
    default[sum(arr)] = 1
    return default

pizza = int(input())
n, m = map(int, input().split())
A, B = suffixSum([int(input()) for _ in range(n)], n), suffixSum([int(input()) for _ in range(m)], m)
print(A[pizza] + B[pizza] + sum([A[i] * B[pizza - i] for i in A]))
