# Segment Tree

세그먼트 트리는 배열의 구간 질의와 값 갱신을 빠르게 처리하는 자료구조이다.

예를 들어 배열에서 특정 구간의 합을 여러 번 구해야 하고, 중간에 값이 바뀐다면 누적합만으로는 부족하다. 이때 세그먼트 트리를 사용한다.

## 1. 언제 쓰는가

- 구간 합을 여러 번 구해야 한다.
- 구간 최솟값 또는 최댓값을 여러 번 구해야 한다.
- 중간에 원소 값이 바뀐다.
- `N`, `Q`가 커서 매번 구간을 순회하면 시간 초과가 난다.

## 2. 세그먼트 트리가 해결하는 것

| 작업 | 단순 배열 | 누적합 | 세그먼트 트리 |
| --- | --- | --- | --- |
| 구간 합 질의 | `O(N)` | `O(1)` | `O(log N)` |
| 값 갱신 | `O(1)` | `O(N)` | `O(log N)` |

값이 바뀌지 않는다면 누적합이 더 간단하다. 값이 바뀐다면 세그먼트 트리가 유리하다.

## 3. 트리 구조

각 노드는 배열의 한 구간을 담당한다.

```text
node 1: [0, 7]
node 2: [0, 3]
node 3: [4, 7]
node 4: [0, 1]
node 5: [2, 3]
```

왼쪽 자식은 `node * 2`, 오른쪽 자식은 `node * 2 + 1`에 저장한다.

## 4. 배열 크기

보통 넉넉하게 `4 * N` 크기로 만든다.

```python
tree = [0] * (4 * n)
```

## 5. 구간 합 세그먼트 트리

### build

초기 배열을 바탕으로 트리를 만든다.

```python
def build(node, start, end):
    if start == end:
        tree[node] = arr[start]
        return

    mid = (start + end) // 2
    build(node * 2, start, mid)
    build(node * 2 + 1, mid + 1, end)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]
```

### query

`left`부터 `right`까지의 구간 합을 구한다.

```python
def query(node, start, end, left, right):
    if right < start or end < left:
        return 0

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    left_sum = query(node * 2, start, mid, left, right)
    right_sum = query(node * 2 + 1, mid + 1, end, left, right)
    return left_sum + right_sum
```

구간 관계는 세 가지로 나뉜다.

```text
1. 전혀 겹치지 않음 -> 0 반환
2. 완전히 포함됨 -> 현재 노드 값 반환
3. 일부만 겹침 -> 양쪽 자식으로 내려감
```

### update

특정 위치의 값을 바꾼다.

```python
def update(node, start, end, idx, value):
    if idx < start or end < idx:
        return

    if start == end:
        tree[node] = value
        return

    mid = (start + end) // 2
    update(node * 2, start, mid, idx, value)
    update(node * 2 + 1, mid + 1, end, idx, value)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]
```

## 6. 사용 예시

```python
arr = [1, 2, 3, 4, 5]
n = len(arr)
tree = [0] * (4 * n)

build(1, 0, n - 1)

print(query(1, 0, n - 1, 1, 3))  # 2 + 3 + 4 = 9

update(1, 0, n - 1, 2, 10)

print(query(1, 0, n - 1, 1, 3))  # 2 + 10 + 4 = 16
```

## 7. 최솟값 세그먼트 트리

구간 최솟값을 구하려면 합 대신 `min`을 사용한다.

```python
INF = 10**18

def query_min(node, start, end, left, right):
    if right < start or end < left:
        return INF

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    return min(
        query_min(node * 2, start, mid, left, right),
        query_min(node * 2 + 1, mid + 1, end, left, right),
    )
```

겹치지 않는 구간의 반환값은 연산에 맞는 항등원이어야 한다.

| 질의 | 겹치지 않을 때 반환 |
| --- | --- |
| 합 | `0` |
| 최솟값 | `INF` |
| 최댓값 | `-INF` |

## 8. 복잡도

| 작업 | 복잡도 |
| --- | --- |
| 트리 생성 | `O(N)` |
| 구간 질의 | `O(log N)` |
| 점 갱신 | `O(log N)` |
| 메모리 | `O(N)` |

## 9. 세그먼트 트리 vs 다른 방법

| 상황 | 추천 |
| --- | --- |
| 값이 안 바뀌는 구간 합 | 누적합 |
| 값이 바뀌는 구간 합 | 세그먼트 트리 |
| 구간 갱신 + 구간 질의 | Lazy Propagation |
| 정적 RMQ | Sparse Table |
| 점 갱신 + prefix 합 | Fenwick Tree |

## 10. 자주 하는 실수

### 인덱스 기준 혼동

입력은 1-index인데 배열은 0-index로 저장하는 경우가 많다.

```python
idx -= 1
left -= 1
right -= 1
```

### 반환값 실수

최솟값 질의에서 겹치지 않는 구간에 `0`을 반환하면 답이 망가진다.

```python
return INF
```

### 트리 크기 부족

처음에는 `4 * n`으로 넉넉하게 잡는 것이 안전하다.

### 갱신 후 부모 노드 재계산 누락

자식 값을 바꾼 뒤 부모 값을 다시 계산해야 한다.

```python
tree[node] = tree[node * 2] + tree[node * 2 + 1]
```

## 11. 정리

세그먼트 트리는 구간 질의와 값 갱신이 섞인 문제에서 강력하다. 핵심은 현재 노드가 담당하는 구간과, 질의 구간의 관계를 정확히 나누는 것이다.
