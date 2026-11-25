# BOJ 10815 숫자 카드
# 문제: https://www.acmicpc.net/problem/10815
# 난이도: Silver 5

import sys


def solution(cards, queries):
    owned_cards = set(cards)
    return [1 if number in owned_cards else 0 for number in queries]


if __name__ == "__main__":
    input = sys.stdin.buffer.readline

    n = int(input())
    cards = list(map(int, input().split()))
    m = int(input())
    queries = list(map(int, input().split()))

    answer = solution(cards, queries)
    sys.stdout.write(" ".join(map(str, answer)) + "\n")
