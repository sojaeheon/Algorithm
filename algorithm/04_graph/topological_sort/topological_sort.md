# Topological Sort

위상 정렬은 방향 그래프에서 선후 관계를 만족하도록 정점을 나열하는 알고리즘이다.

예를 들어 `A를 먼저 해야 B를 할 수 있다`는 관계가 있다면, 결과 순서에서 A는 B보다 앞에 나와야 한다.

## 1. 언제 쓰는가

- 작업 순서를 정해야 한다.
- 선수 과목 관계가 있다.
- 어떤 일을 하기 전에 먼저 끝나야 하는 일이 있다.
- 방향 그래프에서 사이클 여부를 확인해야 한다.
- DAG에서 DP를 해야 한다.

문제에서 "먼저", "이후", "선행", "순서", "의존성" 같은 표현이 나오면 위상 정렬을 떠올린다.

## 2. 핵심 조건

위상 정렬은 **방향 비순환 그래프(DAG)** 에서만 가능하다.

사이클이 있으면 순서를 정할 수 없다.

```text
A -> B -> C -> A
```

이런 경우 A보다 B가 뒤여야 하고, B보다 C가 뒤여야 하고, C보다 A가 뒤여야 하므로 모순이다.

## 3. 진입 차수

진입 차수는 어떤 정점으로 들어오는 간선의 개수이다.

```text
A -> B
C -> B
```

B의 진입 차수는 2이다.

진입 차수가 0인 정점은 지금 바로 처리할 수 있다.

## 4. 기본 코드

```python
from collections import deque

q = deque()

for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

result = []

while q:
    now = q.popleft()
    result.append(now)

    for nxt in graph[now]:
        indegree[nxt] -= 1

        if indegree[nxt] == 0:
            q.append(nxt)
```

## 5. 사이클 확인

위상 정렬 결과에 모든 정점이 들어가지 못했다면 사이클이 있는 것이다.

```python
if len(result) != n:
    print("cycle")
else:
    print(result)
```

## 6. 입력 처리 예시

```python
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
```

`a -> b`는 `a를 먼저 해야 b를 할 수 있다`는 뜻이다.

## 7. 여러 답이 가능한 경우

진입 차수가 0인 정점이 여러 개면 위상 정렬 결과는 여러 개가 될 수 있다.

가장 작은 번호부터 처리해야 한다면 큐 대신 힙을 사용한다.

```python
import heapq

heap = []

for i in range(1, n + 1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

while heap:
    now = heapq.heappop(heap)
    result.append(now)

    for nxt in graph[now]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            heapq.heappush(heap, nxt)
```

## 8. DAG DP

위상 정렬 순서대로 처리하면 선행 상태가 먼저 계산된다.

```python
for now in result:
    for nxt in graph[now]:
        dp[nxt] = max(dp[nxt], dp[now] + cost[nxt])
```

## 9. 복잡도

모든 정점과 간선을 한 번씩 처리하므로 `O(V + E)`이다.

힙을 사용하면 `O((V + E) log V)`가 될 수 있다.

## 10. 자주 하는 실수

### 간선 방향 반대로 저장

`a가 b보다 먼저`라면 보통 `a -> b`이다.

```python
graph[a].append(b)
indegree[b] += 1
```

### 진입 차수 감소 누락

현재 정점을 처리했으면 다음 정점의 진입 차수를 줄여야 한다.

### 사이클 확인 누락

문제에서 순서가 불가능한 경우를 요구하면 `len(result) != n`을 확인한다.

## 11. 정리

위상 정렬은 선후 관계가 있는 작업을 가능한 순서로 나열하는 알고리즘이다. 핵심은 진입 차수가 0인 정점부터 처리하고, 처리한 정점이 가리키는 간선을 제거하는 것이다.
