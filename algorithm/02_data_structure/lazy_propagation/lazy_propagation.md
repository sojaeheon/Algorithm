# Lazy Propagation

Lazy Propagation은 세그먼트 트리에서 **구간 갱신**과 **구간 질의**를 빠르게 처리하기 위한 기법이다.

일반 세그먼트 트리는 점 하나를 바꾸는 갱신에는 강하지만, 구간 전체를 바꾸는 연산이 많으면 느려진다. Lazy Propagation은 갱신을 필요한 순간까지 미뤄서 이 문제를 해결한다.

## 1. 언제 쓰는가

- 구간 전체에 값을 더한다.
- 구간 전체를 어떤 값으로 바꾼다.
- 구간 갱신과 구간 질의가 모두 많다.
- 일반 세그먼트 트리로 매 원소를 갱신하면 시간 초과가 난다.

예:

```text
1번부터 100000번까지 모두 3을 더하라.
10번부터 500번까지의 합을 구하라.
```

## 2. 핵심 아이디어

구간 전체에 갱신이 들어왔을 때, 자식 노드까지 즉시 모두 내려가지 않는다.

대신 현재 노드에만 반영하고, 자식에게 전달할 값은 `lazy` 배열에 저장한다.

```text
tree[node] = 현재 구간의 값
lazy[node] = 자식에게 아직 전달하지 않은 갱신값
```

## 3. push

`push`는 미뤄둔 lazy 값을 현재 노드에 반영하고, 필요하면 자식에게 넘긴다.

구간 덧셈 + 구간 합에서는 구간 길이만큼 더해야 한다.

```python
def push(node, start, end):
    if lazy[node] == 0:
        return

    tree[node] += (end - start + 1) * lazy[node]

    if start != end:
        lazy[node * 2] += lazy[node]
        lazy[node * 2 + 1] += lazy[node]

    lazy[node] = 0
```

## 4. 구간 덧셈 갱신

```python
def update_range(node, start, end, left, right, value):
    push(node, start, end)

    if right < start or end < left:
        return

    if left <= start and end <= right:
        lazy[node] += value
        push(node, start, end)
        return

    mid = (start + end) // 2
    update_range(node * 2, start, mid, left, right, value)
    update_range(node * 2 + 1, mid + 1, end, left, right, value)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]
```

## 5. 구간 합 질의

질의할 때도 먼저 `push`를 해야 한다.

```python
def query(node, start, end, left, right):
    push(node, start, end)

    if right < start or end < left:
        return 0

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    return query(node * 2, start, mid, left, right) + query(node * 2 + 1, mid + 1, end, left, right)
```

## 6. 복잡도

| 작업 | 복잡도 |
| --- | --- |
| 구간 갱신 | `O(log N)` |
| 구간 질의 | `O(log N)` |
| 메모리 | `O(N)` |

## 7. 일반 세그먼트 트리와 비교

| 상황 | 사용 |
| --- | --- |
| 점 갱신 + 구간 질의 | 일반 세그먼트 트리 |
| 구간 갱신 + 구간 질의 | Lazy Propagation |

## 8. 대입 lazy 주의

구간에 값을 더하는 연산과 구간을 어떤 값으로 바꾸는 연산은 lazy 처리 방식이 다르다.

```text
구간 덧셈: lazy 값을 누적한다.
구간 대입: 이전 lazy를 덮어쓸 수 있다.
```

처음 공부할 때는 구간 덧셈 + 구간 합부터 확실히 익히는 것이 좋다.

## 9. 자주 하는 실수

### push를 빼먹는 경우

갱신이나 질의로 노드에 접근할 때 lazy가 남아 있으면 먼저 반영해야 한다.

### 구간 길이를 곱하지 않는 경우

구간 합에서 어떤 구간 전체에 `value`를 더하면 합은 다음만큼 증가한다.

```python
(end - start + 1) * value
```

### lazy 초기값 혼동

덧셈 lazy는 보통 `0`을 초기값으로 둔다. 대입 lazy는 별도의 표시값이 필요할 수 있다.

## 10. 정리

Lazy Propagation은 "지금 당장 자식까지 내려가지 말고, 나중에 필요할 때 처리하자"는 전략이다. 구간 갱신이 많은 문제에서 세그먼트 트리를 한 단계 더 강하게 만들어준다.
