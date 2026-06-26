# DFS

DFS(Depth-First Search)는 한 방향으로 최대한 깊게 들어간 뒤, 더 이상 갈 수 없으면 되돌아와 다른 방향을 탐색하는 알고리즘이다.

재귀 또는 스택으로 구현한다.

## 1. 핵심 개념

DFS는 현재 정점에서 갈 수 있는 정점 하나를 선택해 계속 깊게 들어간다.

```text
현재 정점 방문
갈 수 있는 다음 정점 선택
끝까지 들어감
더 갈 곳이 없으면 되돌아감
```

이런 구조 때문에 연결성 확인, 백트래킹, 트리 순회에 자주 사용된다.

## 2. 언제 쓰는가

- 연결 요소 개수 세기
- 그래프 또는 격자 탐색
- 사이클 탐지
- 트리 순회
- 백트래킹
- 모든 경우 탐색
- SCC, BCC 같은 고급 그래프 알고리즘의 기반

## 3. 재귀 DFS

```python
def dfs(now):
    visited[now] = True

    for nxt in graph[now]:
        if visited[nxt]:
            continue

        dfs(nxt)
```

재귀 DFS는 코드가 짧고 이해하기 쉽다.

## 4. 스택 DFS

재귀를 사용하지 않고 직접 스택으로 구현할 수 있다.

```python
def dfs(start):
    stack = [start]

    while stack:
        now = stack.pop()

        if visited[now]:
            continue

        visited[now] = True

        for nxt in graph[now]:
            if not visited[nxt]:
                stack.append(nxt)
```

재귀 깊이가 너무 깊은 문제에서는 스택 구현이 더 안전할 수 있다.

## 5. 격자 DFS

```python
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(r, c):
    visited[r][c] = True

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]

        if nr < 0 or nr >= n or nc < 0 or nc >= m:
            continue

        if board[nr][nc] == 0:
            continue

        if visited[nr][nc]:
            continue

        dfs(nr, nc)
```

섬 개수 세기, 영역 개수 세기 문제에서 자주 사용한다.

## 6. 연결 요소 개수

```python
count = 0

for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        count += 1
```

DFS를 한 번 시작할 때마다 새로운 연결 요소를 하나 찾은 것이다.

## 7. 백트래킹과 DFS

DFS는 가능한 선택지를 깊게 탐색하는 구조라서 백트래킹과 잘 맞는다.

```python
def backtrack(depth):
    if depth == target:
        print(path)
        return

    for x in candidates:
        if used[x]:
            continue

        used[x] = True
        path.append(x)
        backtrack(depth + 1)
        path.pop()
        used[x] = False
```

핵심은 재귀 호출 후 상태를 원래대로 되돌리는 것이다.

## 8. BFS와 DFS 선택

| 상황 | 추천 |
| --- | --- |
| 최단 거리 | BFS |
| 연결성 확인 | BFS 또는 DFS |
| 모든 경우 탐색 | DFS |
| 백트래킹 | DFS |
| 트리 순회 | DFS |

## 9. 복잡도

그래프에서는 `O(V + E)`이다.

격자에서는 칸 수가 `N * M`이면 `O(NM)`이다.

## 10. 자주 하는 실수

### 방문 처리를 늦게 하는 경우

재귀 DFS에서는 함수에 들어오자마자 방문 처리하는 것이 보통 안전하다.

```python
visited[now] = True
```

### 부모로 되돌아가는 경우

트리 DFS에서는 부모 정점을 제외해야 한다.

```python
def dfs(now, parent):
    for nxt in tree[now]:
        if nxt == parent:
            continue
        dfs(nxt, now)
```

### 재귀 깊이 초과

정점 수가 많으면 다음 설정이 필요할 수 있다.

```python
import sys
sys.setrecursionlimit(10**6)
```

### 방향 그래프와 무방향 그래프 혼동

무방향 그래프는 간선을 양쪽에 넣는다.

```python
graph[a].append(b)
graph[b].append(a)
```

## 11. 정리

DFS는 깊게 들어가며 탐색하는 알고리즘이다. 연결성, 트리, 백트래킹처럼 "한 선택을 끝까지 따라가 보는 문제"에서 특히 강하다.
