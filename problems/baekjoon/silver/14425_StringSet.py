# BOJ 14425 문자열 집합
# 문제: https://www.acmicpc.net/problem/14425
# 난이도: Silver 4

import sys


def solution(strings, queries):
    string_set = set(strings)
    answer = 0

    for query in queries:
        if query in string_set:
            answer += 1

    return answer


if __name__ == "__main__":
    input = sys.stdin.readline

    n, m = map(int, input().split())
    strings = [input().strip() for _ in range(n)]
    queries = [input().strip() for _ in range(m)]

    print(solution(strings, queries))
