# 최솟값 찾기
from collections import deque

N, L = map(int, input().split())
arr = list(map(int,input().split()))

dq = deque()

for i in range(N):
    
    # 뒤에서 현재 값보다 큰 값 제거
    while dq and dq[-1][1]>arr[i]:
        dq.pop()

    # 현재 값 추가
    dq.append((i, arr[i]))
    
    # 윈도우 범위를 벗어난 값 제거
    if dq[0][0] < i - L + 1:
        dq.popleft()
    
    print(dq[0][1], end=' ')


