# Subset

부분집합은 각 원소를 선택하거나 선택하지 않는 모든 경우이다.

원소가 `N`개라면 각 원소마다 선택/미선택 두 가지가 있으므로 부분집합은 총 `2^N`개이다.

## 1. 언제 쓰는가

- 모든 선택 경우를 확인해야 할 때
- 원소 수가 작을 때
- 선택 여부가 중요할 때
- 비트마스크로 상태를 표현할 수 있을 때
- 어떤 집합의 가능한 모든 하위 집합을 봐야 할 때

문제에서 "고르거나 고르지 않는다", "모든 부분집합", "선택한 원소들의 합" 같은 표현이 나오면 부분집합을 떠올린다.

## 2. 재귀로 만들기

각 원소마다 선택하는 경우와 선택하지 않는 경우로 나눈다.

```python
def make_subset(idx, path):
    if idx == n:
        print(path)
        return

    path.append(arr[idx])
    make_subset(idx + 1, path)
    path.pop()

    make_subset(idx + 1, path)


arr = [1, 2, 3]
n = len(arr)
make_subset(0, [])
```

## 3. 재귀 흐름

```text
idx번째 원소를 선택한다.
다음 원소로 간다.
돌아온다.
idx번째 원소를 선택하지 않는다.
다음 원소로 간다.
```

즉, 각 단계에서 선택/미선택 두 갈래로 DFS를 하는 것이다.

## 4. 비트마스크로 만들기

정수의 각 비트를 원소의 선택 여부로 볼 수 있다.

```python
arr = [1, 2, 3]
n = len(arr)

for mask in range(1 << n):
    subset = []

    for i in range(n):
        if mask & (1 << i):
            subset.append(arr[i])

    print(subset)
```

예시:

```text
mask = 0b000 -> []
mask = 0b001 -> [1]
mask = 0b010 -> [2]
mask = 0b011 -> [1, 2]
```

## 5. 부분집합 합

```python
answer = []

for mask in range(1 << n):
    total = 0

    for i in range(n):
        if mask & (1 << i):
            total += arr[i]

    answer.append(total)
```

## 6. 크기가 정해진 부분집합

선택한 원소 개수가 `r`개인 부분집합만 필요하면 조합을 사용하는 것이 더 자연스럽다.

```python
from itertools import combinations

for case in combinations(arr, r):
    print(case)
```

비트마스크를 쓴다면 선택된 비트 개수를 확인한다.

```python
if mask.bit_count() == r:
    pass
```

## 7. 부분집합과 조합 비교

| 구분 | 부분집합 | 조합 |
| --- | --- | --- |
| 선택 개수 | 정해지지 않음 | 보통 `r`개로 정해짐 |
| 경우의 수 | `2^N` | `NCr` |
| 구현 | 선택/미선택 | start 인덱스 |

## 8. 복잡도

부분집합은 총 `2^N`개이다.

각 부분집합마다 원소를 확인하면 `O(N * 2^N)`이 된다.

## 9. 자주 하는 실수

### N이 너무 큰 경우

`2^N`은 빠르게 커진다.

```text
N = 20 -> 약 100만
N = 30 -> 약 10억
```

입력 크기를 보고 가능한지 판단해야 한다.

### 상태 복구 누락

재귀 방식에서는 선택 후 반드시 `pop()`으로 되돌린다.

### 비트 위치 혼동

`i`번째 원소 선택 여부는 다음처럼 확인한다.

```python
mask & (1 << i)
```

## 10. 정리

부분집합은 모든 선택/미선택 경우를 확인하는 방법이다. 원소 수가 작으면 완전 탐색에 유용하고, 비트마스크 DP의 기본 표현으로도 자주 사용된다.
