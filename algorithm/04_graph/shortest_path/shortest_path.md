# Shortest Path

최단 경로 알고리즘은 그래프에서 정점 사이의 최소 비용을 구하는 알고리즘이다.

문제 조건에 따라 사용하는 알고리즘이 달라진다.

## 1. 알고리즘 선택

| 상황 | 알고리즘 |
| --- | --- |
| 간선 비용이 모두 1 | BFS |
| 시작점 하나, 음수 간선 없음 | Dijkstra |
| 시작점 하나, 음수 간선 있음 | Bellman-Ford |
| 모든 정점 쌍 최단 거리 | Floyd-Warshall |

## 2. 복잡도 비교

| 알고리즘 | 복잡도 | 특징 |
| --- | --- | --- |
| BFS | `O(V + E)` | 가중치 없는 그래프 |
| Dijkstra | `O(E log V)` | 음수 간선 불가 |
| Bellman-Ford | `O(VE)` | 음수 간선 가능, 음수 사이클 감지 |
| Floyd-Warshall | `O(V^3)` | 모든 정점 쌍 |

## 3. Dijkstra

Dijkstra는 시작점에서 모든 정점까지의 최단 거리를 구한다. 음수 간선이 없어야 한다.

```python
import heapq

INF = 10**18

def dijkstra(start):
    dist = [INF] * (n + 1)
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        cost, now = heapq.heappop(heap)

        if dist[now] < cost:
            continue

        for nxt, weight in graph[now]:
            new_cost = cost + weight

            if new_cost < dist[nxt]:
                dist[nxt] = new_cost
                heapq.heappush(heap, (new_cost, nxt))

    return dist
```

## 4. Dijkstra 핵심

힙에는 `(현재까지의 비용, 정점)`을 넣는다.

```python
heapq.heappush(heap, (new_cost, nxt))
```

이미 더 짧은 거리로 처리된 값이면 건너뛴다.

```python
if dist[now] < cost:
    continue
```

## 5. Bellman-Ford

Bellman-Ford는 음수 간선이 있어도 사용할 수 있다. 또한 음수 사이클을 확인할 수 있다.

```python
INF = 10**18

def bellman_ford(start):
    dist = [INF] * (n + 1)
    dist[start] = 0

    for i in range(n):
        for now, nxt, cost in edges:
            if dist[now] == INF:
                continue

            if dist[nxt] > dist[now] + cost:
                dist[nxt] = dist[now] + cost

                if i == n - 1:
                    return None

    return dist
```

`n`번째 반복에서도 거리가 줄어든다면 음수 사이클이 존재한다.

## 6. Floyd-Warshall

모든 정점에서 모든 정점까지의 최단 거리를 구한다.

```python
INF = 10**18
dist = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dist[i][i] = 0

for a, b, cost in edges:
    dist[a][b] = min(dist[a][b], cost)

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
```

핵심 의미:

```text
dist[i][j] = i에서 j로 가는 현재 최단 거리
k번 정점을 거쳐 가는 경우를 고려한다.
```

## 7. 무방향 그래프 입력

무방향 그래프는 양쪽에 모두 간선을 넣는다.

```python
graph[a].append((b, cost))
graph[b].append((a, cost))
```

방향 그래프는 한쪽만 넣는다.

```python
graph[a].append((b, cost))
```

## 8. INF 설정

`INF`는 가능한 최단 거리보다 충분히 커야 한다.

```python
INF = 10**18
```

간선 비용과 정점 수가 크면 `10**9`로 부족할 수 있다.

## 9. 자주 하는 실수

### Dijkstra에 음수 간선 사용

음수 간선이 있으면 Dijkstra는 올바른 답을 보장하지 않는다.

### 힙에 정점만 넣는 경우

비용 기준으로 꺼내야 하므로 `(비용, 정점)` 형태로 넣어야 한다.

### 무방향 그래프 간선 한쪽만 저장

문제에서 양방향이라고 하면 반드시 두 번 넣는다.

### Floyd-Warshall 중간 정점 반복 순서

`k`가 가장 바깥 반복문이어야 한다.

```python
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            ...
```

## 10. 정리

최단 경로는 조건을 보고 알고리즘을 고르는 것이 가장 중요하다. 간선 비용이 모두 같으면 BFS, 음수 없는 한 시작점 문제는 Dijkstra, 음수 간선이 있으면 Bellman-Ford, 모든 쌍이면 Floyd-Warshall을 사용한다.
