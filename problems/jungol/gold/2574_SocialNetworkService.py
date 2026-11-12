# JUNGOL 2574 사회망 서비스(SNS)
# 문제: https://jungol.co.kr/problem/2574

import sys


def solution(N, edges):
    pass


if __name__ == "__main__":
    input = sys.stdin.buffer.readline

    N = int(input())
    edges = [tuple(map(int, input().split())) for _ in range(N - 1)]

    print(solution(N, edges))
