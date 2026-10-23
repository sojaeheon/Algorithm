# JUNGOL 1863 종교
# 문제: https://jungol.co.kr/problem/1863
# 난이도: Gold 5

import sys

def find(parent,x):
    if parent[x] != x:
        parent[x] = find(parent,parent[x])

    return parent[x]

def union(parent,size,a,b):

    root_a = find(parent,a)
    root_b = find(parent,b)

    if root_a == root_b:
        return False
    if size[root_a] < size[root_b]:
        root_a, root_b = root_b, root_a

    parent[root_b] = root_a
    size[root_a] += size[root_b]
    return True 

def solution(N, pairs):
    students = list(range(N+1))
    size = [1] * (N+1)
    religion_count = N

    for first, second in pairs:
        if union(students,size,first,second):
            religion_count-=1
    return religion_count


if __name__ == "__main__":
    input = sys.stdin.buffer.readline

    N, M = map(int, input().split())
    pairs = [tuple(map(int, input().split())) for _ in range(M)]

    print(solution(N, pairs))
