# BFS

BFS(Breadth-First Search)는 시작점에서 가까운 정점부터 차례대로 탐색하는 알고리즘이다. 큐를 사용하며, 가중치가 없는 그래프에서 최단 거리를 구할 때 가장 기본적으로 사용한다.

## 1. 핵심 개념

BFS는 한 정점에서 갈 수 있는 곳을 먼저 모두 확인한 뒤, 그 다음 거리의 정점으로 넘어간다.

```text
거리 0: 시작점
거리 1: 시작점에서 한 번에 갈 수 있는 정점
거리 2: 두 번 이동해서 갈 수 있는 정점
```

그래서 간선의 비용이 모두 같다면, 처음 방문한 순간의 거리가 최단 거리이다.

## 2. 언제 쓰는가

- 가중치가 없는 그래프의 최단 거리
- 격자에서 최소 이동 횟수
- 미로 탐색
- 한 단계씩 퍼져나가는 문제
- 연결 요소 탐색
- 최단 이동 횟수를 구하는 문제

문제에서 "최소 몇 번 이동", "가장 빠른 시간", "가까운 곳부터" 같은 표현이 나오고 간선 비용이 모두 같다면 BFS를 먼저 생각한다.

## 3. 기본 코드

```python
from collections import deque


def bfs(start):
    q = deque([start])
    visited[start] = True

    while q:
        now = q.popleft()

        for nxt in graph[now]:
            if visited[nxt]:
                continue

            visited[nxt] = True
            q.append(nxt)
```

## 4. 거리 배열 사용

최단 거리가 필요하면 `visited` 대신 `dist` 배열을 사용할 수 있다.

```python
from collections import deque


def bfs(start):
    dist = [-1] * (n + 1)
    dist[start] = 0
    q = deque([start])

    while q:
        now = q.popleft()

        for nxt in graph[now]:
            if dist[nxt] != -1:
                continue

            dist[nxt] = dist[now] + 1
            q.append(nxt)

    return dist
```

`dist[x] == -1`이면 아직 방문하지 않은 정점이다.

## 5. 격자 BFS

격자 문제에서는 좌표 `(r, c)`를 큐에 넣는다.

```python
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(sr, sc):
    q = deque([(sr, sc)])
    dist[sr][sc] = 0

    while q:
        r, c = q.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue

            if board[nr][nc] == 1:
                continue

            if dist[nr][nc] != -1:
                continue

            dist[nr][nc] = dist[r][c] + 1
            q.append((nr, nc))
```

## 6. 여러 시작점 BFS

시작점이 여러 개인 경우, 모든 시작점을 큐에 먼저 넣고 BFS를 시작한다.

```python
q = deque()

for r in range(n):
    for c in range(m):
        if board[r][c] == 1:
            q.append((r, c))
            dist[r][c] = 0

while q:
    r, c = q.popleft()

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]

        if nr < 0 or nr >= n or nc < 0 or nc >= m:
            continue
        if dist[nr][nc] != -1:
            continue

        dist[nr][nc] = dist[r][c] + 1
        q.append((nr, nc))
```

토마토처럼 여러 위치에서 동시에 퍼지는 문제에 사용한다.

## 7. BFS와 DFS 차이

| 알고리즘 | 자료구조 | 특징 |
| --- | --- | --- |
| BFS | 큐 | 가까운 곳부터 탐색 |
| DFS | 스택/재귀 | 한 방향으로 깊게 탐색 |

최단 거리가 필요하면 보통 BFS를 사용한다. 단, 간선 가중치가 다르면 Dijkstra 같은 다른 알고리즘이 필요하다.

## 8. 복잡도

그래프에서 모든 정점과 간선을 한 번씩 확인하므로 `O(V + E)`이다.

격자에서는 칸 수가 `N * M`이면 `O(NM)`이다.

## 9. 자주 하는 실수

### 방문 처리를 큐에서 꺼낼 때 하는 경우

큐에 넣을 때 방문 처리하는 것이 중복 삽입을 줄인다.

```python
dist[nxt] = dist[now] + 1
q.append(nxt)
```

### `list.pop(0)` 사용

`pop(0)`은 `O(N)`이라 느리다. BFS는 반드시 `deque.popleft()`를 사용한다.

### 장애물 조건 누락

격자 BFS에서는 범위, 장애물, 방문 여부를 모두 확인해야 한다.

### 가중치 있는 그래프에 BFS 사용

간선 비용이 모두 같을 때만 BFS가 최단 거리를 보장한다.

## 10. 정리

BFS는 "같은 거리의 후보를 한 번에 처리하는 탐색"이다. 최단 이동 횟수 문제가 나오면 먼저 간선 비용이 모두 같은지 확인하고, 같다면 BFS를 적용한다.
