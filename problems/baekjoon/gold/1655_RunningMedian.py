# BOJ 1655 가운데를 말해요
# 문제: https://www.acmicpc.net/problem/1655
# 난이도: Gold 2

import heapq
import sys


def solution(numbers):
    answer = []
    lower = []  # 작은 절반의 최대 힙 (부호를 바꿔 저장)
    upper = []  # 큰 절반의 최소 힙

    for number in numbers:
        if not lower or number <= -lower[0]:
            heapq.heappush(lower, -number)
        else:
            heapq.heappush(upper, number)

        # 작은 절반의 크기를 큰 절반과 같거나 하나 더 많게 맞춘다.
        if len(lower) > len(upper) + 1:
            heapq.heappush(upper, -heapq.heappop(lower))
        elif len(upper) > len(lower):
            heapq.heappush(lower, -heapq.heappop(upper))

        answer.append(-lower[0])

    return answer


if __name__ == "__main__":
    input = sys.stdin.buffer.readline

    n = int(input())
    numbers = [int(input()) for _ in range(n)]

    sys.stdout.write("\n".join(map(str, solution(numbers))))
