# Disjoint Set

서로소 집합은 여러 원소가 같은 집합에 속하는지 빠르게 확인하고, 두 집합을 합치는 자료구조이다. Union-Find라고도 부른다.

## 1. 언제 쓰는가

- 두 원소가 같은 그룹인지 확인해야 한다.
- 그룹을 합치는 연산이 반복된다.
- 연결 여부를 빠르게 판별해야 한다.
- Kruskal 최소 신장 트리를 구현한다.
- 무방향 그래프에서 사이클을 판별한다.

## 2. 핵심 연산

| 연산 | 의미 |
| --- | --- |
| `find(x)` | `x`가 속한 집합의 대표를 찾는다 |
| `union(a, b)` | `a`가 속한 집합과 `b`가 속한 집합을 합친다 |

각 집합은 대표 원소를 가진다. 같은 집합에 속한 원소들은 `find` 결과가 같다.

## 3. 기본 코드

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

    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b

    return True


n = 5
parent = [i for i in range(n + 1)]
```

## 4. find

`find`는 원소의 대표 노드를 찾는다.

```python
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
```

이때 `parent[x] = find(parent[x])`는 경로 압축이다. 한 번 대표를 찾은 뒤에는 바로 대표를 가리키게 만들어 다음 탐색을 빠르게 한다.

## 5. union

`union`은 두 집합을 합친다.

```python
def union(a, b):
    root_a = find(a)
    root_b = find(b)

    if root_a == root_b:
        return False

    parent[root_b] = root_a
    return True
```

이미 같은 집합이면 합칠 수 없으므로 `False`를 반환하게 만들면 사이클 판별에 유용하다.

## 6. rank 사용

트리가 한쪽으로 길어지는 것을 막기 위해 rank 또는 size를 사용할 수 있다.

```python
parent = [i for i in range(n + 1)]
rank = [0] * (n + 1)

def union(a, b):
    root_a = find(a)
    root_b = find(b)

    if root_a == root_b:
        return False

    if rank[root_a] < rank[root_b]:
        parent[root_a] = root_b
    elif rank[root_a] > rank[root_b]:
        parent[root_b] = root_a
    else:
        parent[root_b] = root_a
        rank[root_a] += 1

    return True
```

## 7. 사이클 판별

무방향 그래프에서 간선을 하나씩 보며 이미 같은 집합이면 사이클이 생긴다.

```python
has_cycle = False

for a, b in edges:
    if not union(a, b):
        has_cycle = True
        break
```

## 8. Kruskal에서 사용

간선을 비용 순으로 정렬한 뒤, 사이클이 생기지 않는 간선만 선택한다.

```python
edges.sort()
total = 0

for cost, a, b in edges:
    if union(a, b):
        total += cost
```

## 9. 복잡도

경로 압축과 rank를 사용하면 `find`, `union`은 거의 `O(1)`에 가깝게 동작한다.

정확히는 아주 느리게 증가하는 역 아커만 함수가 붙지만, 문제 풀이에서는 거의 상수 시간으로 생각해도 된다.

## 10. 자주 하는 실수

### 대표끼리 비교하지 않는 경우

```python
if find(a) == find(b):
    print("same")
```

원래 값 `a`, `b`를 직접 비교하면 안 된다.

### parent 배열 크기

정점 번호가 1부터 시작하면 `n + 1` 크기로 만든다.

```python
parent = [i for i in range(n + 1)]
```

### 방향 그래프에 잘못 적용

서로소 집합은 주로 무방향 연결성 문제에 사용한다. 방향 그래프의 도달 가능성은 보통 DFS, BFS, SCC 등을 사용한다.

## 11. 정리

서로소 집합은 "같은 그룹인가?"와 "두 그룹을 합쳐라"가 반복되는 문제의 기본 도구이다. 특히 Kruskal과 무방향 사이클 판별에서 거의 필수로 등장한다.
