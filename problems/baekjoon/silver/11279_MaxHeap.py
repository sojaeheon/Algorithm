# BOJ 11279 최대 힙
# 문제: https://www.acmicpc.net/problem/11279
# 난이도: Silver 2

import heapq
import sys


def solution(operations):
    answer = []
    pq = []

    for x in operations:
        if x == 0:
            if pq:
                answer.append(-heapq.heappop(pq))
            else:
                answer.append(0)
        else:
            heapq.heappush(pq, -x)

    return answer


if __name__ == "__main__":
    input = sys.stdin.buffer.readline

    n = int(input())
    operations = [int(input()) for _ in range(n)]

    print(*solution(operations), sep="\n")
