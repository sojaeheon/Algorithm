# Strongly Connected Component

SCC(Strongly Connected Component)는 방향 그래프에서 서로 모든 정점으로 도달 가능한 정점들의 묶음이다.

같은 SCC 안의 정점들은 서로 왕복이 가능하다.

## 1. 언제 쓰는가

- 방향 그래프의 순환 구조를 묶어야 한다.
- 서로 도달 가능한 그룹을 찾아야 한다.
- 그래프를 SCC 단위로 압축해야 한다.
- 2-SAT 문제를 풀어야 한다.
- 방향 그래프에서 강한 연결성을 분석해야 한다.

## 2. SCC 예시

```text
1 -> 2 -> 3
^         |
|_________|
```

1, 2, 3은 서로 도달 가능하므로 하나의 SCC이다.

## 3. 핵심 아이디어

DFS 방문 순서를 기록하면서, 현재 정점이 도달할 수 있는 가장 빠른 방문 순서를 계산한다.

Tarjan 알고리즘에서는 다음 배열을 사용한다.

| 이름 | 의미 |
| --- | --- |
| `ids` | DFS 방문 순서 |
| `finished` | SCC로 확정되었는지 여부 |
| `stack` | 아직 SCC가 확정되지 않은 정점 |

## 4. Tarjan 코드

```python
import sys
sys.setrecursionlimit(10**6)


def dfs(now):
    global order

    order += 1
    ids[now] = order
    stack.append(now)

    parent = ids[now]

    for nxt in graph[now]:
        if ids[nxt] == 0:
            parent = min(parent, dfs(nxt))
        elif not finished[nxt]:
            parent = min(parent, ids[nxt])

    if parent == ids[now]:
        component = []

        while True:
            x = stack.pop()
            finished[x] = True
            component.append(x)

            if x == now:
                break

        scc.append(component)

    return parent
```

초기화:

```python
n = int(input())
graph = [[] for _ in range(n + 1)]

ids = [0] * (n + 1)
finished = [False] * (n + 1)
stack = []
scc = []
order = 0

for i in range(1, n + 1):
    if ids[i] == 0:
        dfs(i)
```

## 5. parent 값의 의미

`parent`는 현재 정점에서 DFS 트리 간선과 역방향 간선을 통해 도달할 수 있는 가장 작은 방문 순서이다.

만약 `parent == ids[now]`라면 `now`가 SCC의 루트가 된다. 이때 스택에서 `now`가 나올 때까지 꺼낸 정점들이 하나의 SCC이다.

## 6. SCC 압축

SCC를 하나의 정점으로 압축하면 DAG가 된다. 이 성질을 이용해 SCC 단위로 DP를 하거나 선후 관계를 분석할 수 있다.

## 7. 복잡도

모든 정점과 간선을 한 번씩 보므로 `O(V + E)`이다.

## 8. 자주 하는 실수

### finished 확인 누락

이미 SCC로 확정된 정점은 현재 SCC 계산에 영향을 주면 안 된다.

```python
elif not finished[nxt]:
    parent = min(parent, ids[nxt])
```

### 재귀 깊이

그래프가 크면 재귀 제한을 늘려야 한다.

```python
sys.setrecursionlimit(10**6)
```

### 방향 그래프 조건

SCC는 방향 그래프에서 의미가 있다. 무방향 그래프의 연결 요소와 헷갈리지 않는다.

## 9. 정리

SCC는 방향 그래프에서 서로 왕복 가능한 정점들의 그룹이다. Tarjan 알고리즘은 DFS 순서와 스택을 이용해 `O(V + E)`에 SCC를 찾는다.
