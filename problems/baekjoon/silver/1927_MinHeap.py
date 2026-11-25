# BOJ 1927 최소 힙
# 문제: https://www.acmicpc.net/problem/1927
# 난이도: Silver 2

import sys,heapq

def solution(operations):
    answer = []
    pq = []
    for x in operations:
        if x == 0:
            if pq: answer.append(heapq.heappop(pq))
            else: answer.append(0)
        else:
            heapq.heappush(pq,x)


    return answer


if __name__ == "__main__":
    input = sys.stdin.buffer.readline

    N = int(input())
    operations = [int(input()) for _ in range(N)]

    print(*solution(operations), sep="\n")
