# Python IO

Python 문제 풀이에서 자주 사용하는 입출력 템플릿입니다.

## 1. 기본 템플릿

```python
import sys
input = sys.stdin.readline
```

입력이 많으면 `input()` 대신 `sys.stdin.readline`을 사용합니다.

## 2. 정수 하나

```python
n = int(input())
```

## 3. 한 줄 여러 정수

```python
a, b = map(int, input().split())
```

## 4. 리스트 입력

```python
arr = list(map(int, input().split()))
```

## 5. 여러 줄 리스트

```python
n = int(input())
arr = [int(input()) for _ in range(n)]
```

## 6. 2차원 배열

정수 격자:

```python
board = [list(map(int, input().split())) for _ in range(n)]
```

문자 격자:

```python
board = [list(input().strip()) for _ in range(n)]
```

공백 없는 숫자 격자:

```python
board = [list(map(int, input().strip())) for _ in range(n)]
```

## 7. 그래프 입력

무방향 그래프:

```python
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
```

가중치 그래프:

```python
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
```

## 8. 출력

```python
print(answer)
print(*arr)
```

## 9. 많은 출력

```python
result = []

for x in arr:
    result.append(str(x))

print('\n'.join(result))
```

## 10. 재귀 깊이

DFS나 트리 DP에서 재귀가 깊어질 수 있으면 제한을 늘립니다.

```python
import sys
sys.setrecursionlimit(10**6)
```

## 11. 자주 쓰는 import

```python
from collections import deque, Counter, defaultdict
from itertools import permutations, combinations
from bisect import bisect_left, bisect_right
import heapq
import math
```

## 12. 정리

- 입력이 많으면 `sys.stdin.readline`을 사용한다.
- 출력이 많으면 문자열로 모아서 한 번에 출력한다.
- 그래프는 1-index 입력이 많으므로 `n + 1` 크기로 만드는 경우가 많다.
- 재귀 DFS를 쓰면 재귀 깊이를 확인한다.
