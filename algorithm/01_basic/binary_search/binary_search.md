# Binary Search

이분 탐색은 정렬된 범위 또는 단조성을 가진 범위에서 답을 반씩 줄여가며 찾는 알고리즘이다.

이분 탐색은 크게 두 가지로 나뉜다.

```text
1. 배열에서 특정 값 찾기
2. 가능한 답의 범위에서 최적의 답 찾기
```

두 번째를 보통 **정답 이분 탐색** 또는 **파라메트릭 서치**라고 부른다.

## 1. 핵심 조건

이분 탐색을 쓰려면 다음 중 하나가 필요하다.

- 배열이 정렬되어 있다.
- 값이 커질수록 조건 결과가 일정한 방향으로 바뀐다.
- 어떤 답 `x`가 가능하면, 그보다 크거나 작은 값들도 일정하게 가능하다.

즉, 탐색 대상에 **단조성**이 있어야 한다.

## 2. 배열에서 값 찾기

정렬된 배열에서 원하는 값을 찾는 기본 이분 탐색이다.

```python
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

## 3. lower_bound

`target` 이상이 처음 나오는 위치를 찾는다.

```python
def lower_bound(arr, target):
    left = 0
    right = len(arr)

    while left < right:
        mid = (left + right) // 2

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left
```

예시:

```text
arr = [1, 3, 3, 5, 8]
lower_bound(arr, 3) -> 1
lower_bound(arr, 4) -> 3
```

## 4. upper_bound

`target`보다 큰 값이 처음 나오는 위치를 찾는다.

```python
def upper_bound(arr, target):
    left = 0
    right = len(arr)

    while left < right:
        mid = (left + right) // 2

        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid

    return left
```

예시:

```text
arr = [1, 3, 3, 5, 8]
upper_bound(arr, 3) -> 3
```

특정 값의 개수는 다음처럼 구할 수 있다.

```python
count = upper_bound(arr, x) - lower_bound(arr, x)
```

## 5. Python bisect

Python에서는 `bisect` 모듈을 사용할 수 있다.

```python
from bisect import bisect_left, bisect_right

left = bisect_left(arr, x)
right = bisect_right(arr, x)
count = right - left
```

| 함수 | 의미 |
| --- | --- |
| `bisect_left(arr, x)` | `x` 이상이 처음 나오는 위치 |
| `bisect_right(arr, x)` | `x`보다 큰 값이 처음 나오는 위치 |

## 6. 정답 이분 탐색

정답 이분 탐색은 답이 될 수 있는 범위를 정하고, `mid`가 가능한 답인지 검사하면서 범위를 줄인다.

예를 들어 "최소 시간", "최대 길이", "가능한 최소 비용" 같은 문제에 자주 사용한다.

```python
def can(x):
    # x가 가능한 답인지 검사
    return True


left = 0
right = 10**9
answer = right

while left <= right:
    mid = (left + right) // 2

    if can(mid):
        answer = mid
        right = mid - 1
    else:
        left = mid + 1
```

위 코드는 **가능한 값 중 최솟값**을 찾는 형태이다.

## 7. 가능한 값 중 최댓값 찾기

```python
def can(x):
    return True


left = 0
right = 10**9
answer = left

while left <= right:
    mid = (left + right) // 2

    if can(mid):
        answer = mid
        left = mid + 1
    else:
        right = mid - 1
```

## 8. 어떤 방향으로 줄일까

정답 이분 탐색에서 가장 중요한 것은 `can(mid)`가 참일 때 어느 쪽을 버릴지 정하는 것이다.

| 목표 | `can(mid) == True`일 때 |
| --- | --- |
| 가능한 최솟값 | 답 후보 저장 후 왼쪽 탐색 |
| 가능한 최댓값 | 답 후보 저장 후 오른쪽 탐색 |

## 9. 문제에서 보이는 신호

다음 표현이 나오면 정답 이분 탐색을 의심해볼 수 있다.

- 최대한 작게
- 최대한 크게
- 최소 시간
- 최대 길이
- 가능한가?
- 몇 개 이상 만들 수 있는가?
- 조건을 만족하는 가장 작은 값
- 조건을 만족하는 가장 큰 값

## 10. 예시: 랜선 자르기 형태

길이 `x`로 잘랐을 때 필요한 개수 이상 만들 수 있는지 검사한다.

```python
def can(length):
    count = 0

    for cable in cables:
        count += cable // length

    return count >= need


left = 1
right = max(cables)
answer = 0

while left <= right:
    mid = (left + right) // 2

    if can(mid):
        answer = mid
        left = mid + 1
    else:
        right = mid - 1
```

길이가 길수록 만들 수 있는 개수는 줄어든다. `mid` 길이로 만들 수 있다면 더 긴 길이도 시도한다.

## 11. 복잡도

| 종류 | 시간 복잡도 |
| --- | --- |
| 배열 이분 탐색 | `O(log N)` |
| 정답 이분 탐색 | `O(log 범위 * can 함수 복잡도)` |

## 12. 자주 하는 실수

### 정렬을 빼먹는 경우

배열에서 값을 찾는 이분 탐색은 정렬이 필수이다.

```python
arr.sort()
```

### `left`, `right` 범위를 잘못 잡는 경우

정답 이분 탐색에서는 답이 절대 범위 밖에 있으면 안 된다.

```python
left = 1
right = max(arr)
```

문제에 따라 `left = 0`이 맞을 수도 있고, 0으로 나누기 문제가 있으면 `left = 1`이어야 한다.

### 무한 반복

`while left <= right`를 쓸 때는 반드시 `left = mid + 1` 또는 `right = mid - 1`처럼 범위가 줄어야 한다.

### 최솟값/최댓값 방향 혼동

가능한 최솟값을 찾는지, 가능한 최댓값을 찾는지 먼저 적고 시작하면 실수가 줄어든다.

## 13. 정리

이분 탐색은 단순히 정렬된 배열에서 값을 찾는 도구가 아니라, 답의 범위를 빠르게 줄이는 강력한 방법이다.

핵심은 `mid`를 검사하는 함수 `can(mid)`를 만들 수 있는지, 그리고 그 결과가 단조적인지 확인하는 것이다.
