# Biconnected Component

BCC(Biconnected Component)는 무방향 그래프에서 단절점이나 단절선을 기준으로 나뉘는 강한 연결 구조이다.

알고리즘 문제에서는 BCC 자체보다 **단절점**과 **단절선**을 먼저 다루는 경우가 많다.

## 1. 언제 쓰는가

- 무방향 그래프에서 끊어지는 정점을 찾아야 한다.
- 어떤 정점을 제거하면 그래프가 분리되는지 확인해야 한다.
- 어떤 간선을 제거하면 그래프가 분리되는지 확인해야 한다.
- 네트워크의 취약 지점을 찾는다.

## 2. 단절점

단절점은 제거했을 때 그래프의 연결 요소 개수가 증가하는 정점이다.

```text
1 - 2 - 3
```

여기서 2를 제거하면 1과 3이 분리되므로 2는 단절점이다.

## 3. 단절선

단절선은 제거했을 때 그래프의 연결 요소 개수가 증가하는 간선이다.

```text
1 - 2 - 3
```

간선 2-3을 제거하면 그래프가 나뉘므로 단절선이다.

## 4. DFS order와 low

DFS를 하면서 두 값을 관리한다.

| 이름 | 의미 |
| --- | --- |
| `order[now]` | DFS 방문 순서 |
| `low` | 현재 정점의 서브트리에서 역방향 간선으로 도달 가능한 가장 빠른 방문 순서 |

## 5. 단절점 코드

```python
def dfs(now, is_root):
    global cnt

    cnt += 1
    order[now] = cnt
    low = order[now]
    child_count = 0

    for nxt in graph[now]:
        if order[nxt] == 0:
            child_count += 1
            child_low = dfs(nxt, False)
            low = min(low, child_low)

            if not is_root and child_low >= order[now]:
                is_cut[now] = True
        else:
            low = min(low, order[nxt])

    if is_root and child_count >= 2:
        is_cut[now] = True

    return low
```

초기화:

```python
order = [0] * (n + 1)
is_cut = [False] * (n + 1)
cnt = 0

for i in range(1, n + 1):
    if order[i] == 0:
        dfs(i, True)
```

## 6. 단절점 판정

루트가 아닌 정점:

```text
child_low >= order[now]
```

이면 `now`는 단절점이다.

루트 정점:

```text
DFS 자식이 2개 이상이면 단절점
```

## 7. 단절선 판정

간선 `now - nxt`에서:

```text
child_low > order[now]
```

이면 이 간선은 단절선이다.

단절점은 `>=`, 단절선은 `>`를 쓴다는 점을 구분한다.

## 8. 자주 하는 실수

### 루트 처리

루트는 다른 정점과 판정 조건이 다르다. 자식 수가 2개 이상이어야 단절점이다.

### 부모 간선 처리

무방향 그래프에서는 부모로 돌아가는 간선을 잘못 처리하지 않도록 주의한다. 간선 번호를 저장해야 하는 문제도 있다.

### SCC와 혼동

SCC는 방향 그래프, BCC/단절점/단절선은 주로 무방향 그래프에서 다룬다.

## 9. 정리

BCC 관련 문제의 핵심은 DFS 방문 순서와 `low` 값을 이용해 그래프가 끊어지는 지점을 찾는 것이다. 단절점과 단절선의 판정 부등호가 다르다는 점을 꼭 기억한다.
