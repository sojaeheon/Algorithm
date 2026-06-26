# Minimum Spanning Tree

최소 신장 트리(MST, Minimum Spanning Tree)는 모든 정점을 연결하면서 간선 비용의 합이 최소가 되는 트리이다.

## 1. 핵심 조건

MST는 다음 조건을 만족한다.

- 모든 정점을 연결한다.
- 사이클이 없다.
- 선택한 간선 수는 `V - 1`개이다.
- 간선 비용의 합이 최소이다.

그래프가 연결되어 있지 않으면 모든 정점을 잇는 신장 트리를 만들 수 없다.

## 2. 언제 쓰는가

- 모든 도시를 최소 비용으로 연결한다.
- 네트워크, 전선, 도로를 최소 비용으로 설치한다.
- 모든 지점이 연결되어야 한다.
- 두 정점 사이의 최단 거리보다 전체 연결 비용이 중요하다.

최단 경로와 MST는 다르다.

```text
최단 경로: 한 정점에서 다른 정점까지 가장 싸게 가는 길
MST: 전체 정점을 모두 연결하는 최소 비용 구조
```

## 3. Kruskal 알고리즘

Kruskal은 간선을 비용 순서대로 정렬하고, 사이클이 생기지 않는 간선만 선택한다.

## 4. Kruskal 코드

```python
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    root_a = find(a)
    root_b = find(b)

    if root_a == root_b:
        return False

    parent[root_b] = root_a
    return True


edges.sort()
parent = [i for i in range(n + 1)]
total = 0
count = 0

for cost, a, b in edges:
    if union(a, b):
        total += cost
        count += 1

        if count == n - 1:
            break
```

## 5. Kruskal 흐름

```text
1. 모든 간선을 비용 기준으로 정렬한다.
2. 가장 싼 간선부터 확인한다.
3. 두 정점이 이미 같은 집합이면 선택하지 않는다.
4. 다른 집합이면 간선을 선택하고 두 집합을 합친다.
5. 간선이 V - 1개 선택되면 끝난다.
```

## 6. Prim 알고리즘

Prim은 하나의 정점에서 시작해, 현재 트리와 연결되는 가장 싼 간선을 계속 선택한다.

## 7. Prim 코드

```python
import heapq


def prim(start):
    heap = [(0, start)]
    visited = [False] * (n + 1)
    total = 0
    count = 0

    while heap:
        cost, now = heapq.heappop(heap)

        if visited[now]:
            continue

        visited[now] = True
        total += cost
        count += 1

        for nxt_cost, nxt in graph[now]:
            if not visited[nxt]:
                heapq.heappush(heap, (nxt_cost, nxt))

    if count != n:
        return None

    return total
```

## 8. Kruskal과 Prim 비교

| 구분 | Kruskal | Prim |
| --- | --- | --- |
| 중심 | 간선 | 정점 |
| 주요 자료구조 | 서로소 집합 | 힙 |
| 적합한 경우 | 간선 목록이 주어짐 | 인접 리스트가 편함 |
| 복잡도 | `O(E log E)` | `O(E log V)` |

대부분의 코딩 테스트에서는 Kruskal이 구현이 단순해서 자주 사용된다.

## 9. MST와 최단 경로 비교

| 구분 | MST | 최단 경로 |
| --- | --- | --- |
| 목적 | 전체 연결 비용 최소 | 특정 경로 비용 최소 |
| 대표 알고리즘 | Kruskal, Prim | BFS, Dijkstra, Bellman-Ford |
| 결과 | 트리 | 거리 배열 또는 경로 |

MST에서 두 정점 사이의 경로가 항상 최단 경로인 것은 아니다.

## 10. 자주 하는 실수

### 무방향 그래프 처리

MST는 보통 무방향 그래프에서 다룬다. Prim에서는 양방향 간선을 넣어야 한다.

```python
graph[a].append((cost, b))
graph[b].append((cost, a))
```

### 연결 그래프가 아닌 경우

모든 정점이 연결되지 않으면 MST가 존재하지 않는다. 선택한 간선 수나 방문 정점 수를 확인한다.

```python
if count != n - 1:
    print("MST 없음")
```

### 최단 경로 문제와 혼동

"모든 정점을 연결"이 핵심이면 MST이고, "A에서 B까지 최소 비용"이면 최단 경로이다.

## 11. 정리

MST는 전체 정점을 최소 비용으로 연결하는 문제에 사용한다. 간선 중심으로 생각하면 Kruskal, 정점 중심으로 확장하면 Prim을 사용한다.
