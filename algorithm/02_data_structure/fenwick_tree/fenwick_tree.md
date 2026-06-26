# Fenwick Tree

Fenwick Tree는 누적합을 빠르게 갱신하고 구하기 위한 자료구조이다. Binary Indexed Tree(BIT)라고도 부른다.

## 1. 언제 쓰는가

- 점 갱신과 구간 합 질의가 필요하다.
- prefix sum을 여러 번 구해야 한다.
- 세그먼트 트리보다 간단한 구간 합 구조가 필요하다.
- 좌표 압축과 함께 빈도 합을 구한다.

## 2. 핵심 연산

| 연산 | 의미 | 복잡도 |
| --- | --- | --- |
| `update(i, diff)` | i번째 값에 diff 더하기 | `O(log N)` |
| `prefix_sum(i)` | 1번부터 i번까지 합 | `O(log N)` |
| `range_sum(l, r)` | l번부터 r번까지 합 | `O(log N)` |

## 3. 기본 코드

Fenwick Tree는 보통 1-index로 구현한다.

```python
def update(i, diff):
    while i <= n:
        tree[i] += diff
        i += i & -i


def prefix_sum(i):
    result = 0

    while i > 0:
        result += tree[i]
        i -= i & -i

    return result


def range_sum(left, right):
    return prefix_sum(right) - prefix_sum(left - 1)
```

## 4. `i & -i` 의미

`i & -i`는 i의 마지막 1비트 값을 구한다.

Fenwick Tree에서는 이 값을 이용해 다음 담당 구간으로 이동한다.

```text
update: i += i & -i
query:  i -= i & -i
```

## 5. 초기화

```python
n = len(arr)
tree = [0] * (n + 1)

for i, value in enumerate(arr, start=1):
    update(i, value)
```

## 6. 세그먼트 트리와 비교

| 구분 | Fenwick Tree | Segment Tree |
| --- | --- | --- |
| 구현 | 간단 | 비교적 복잡 |
| 구간 합 | 가능 | 가능 |
| 구간 최솟값 | 어려움 | 가능 |
| 구간 갱신 | 응용 필요 | Lazy로 가능 |

## 7. 자주 하는 실수

- 0-index로 구현하려다 인덱스 이동이 꼬이는 경우
- `left - 1`을 빼지 않아 구간 합이 틀리는 경우
- 값 대입을 해야 하는데 차이값 `diff`를 계산하지 않는 경우

## 8. 정리

Fenwick Tree는 점 갱신과 prefix sum 질의에 특화된 자료구조이다. 구간 합만 필요하다면 세그먼트 트리보다 간단하게 사용할 수 있다.
