# Programmers 42861 섬 연결하기
# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42861
# 난이도: LV3

def find(parents, x):
    if parents[x] != x:
        parents[x] = find(parents,parents[x])
    
    return parents[x]

def union(parents,size,a,b):
    root_a = find(parents,a)
    root_b = find(parents,b)

    if root_a == root_b:
        return False

    if size[root_a] < size[root_b]:
        root_a, root_b = root_b, root_a

    parents[root_b] = root_a
    size[root_a] += size[root_b]
    return True

def solution(n, costs):
    lands = list(range(n+1))
    sizes = [1] * (n+1)

    answer = 0
    count = 0

    costs.sort(key=lambda x : x[2])

    for a,b,cost in costs:
        if union(lands,sizes,a,b):
            answer+=cost
            count+=1

        if count == n-1:
            break

    if count != n-1:
        return -1


    return answer
