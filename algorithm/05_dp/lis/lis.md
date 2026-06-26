# LIS

LIS(Longest Increasing Subsequence)는 가장 긴 증가하는 부분 수열이다.

부분 수열은 원래 순서를 유지하되, 일부 원소를 지울 수 있는 수열이다.

```text
arr = [10, 20, 10, 30, 20, 50]
LIS = [10, 20, 30, 50]
길이 = 4
```

## 1. 언제 쓰는가

- 증가하는 순서를 최대한 길게 고를 때
- 순서를 유지하면서 일부를 선택해야 할 때
- 가장 긴 상승 흐름을 찾을 때
- 전깃줄, 순서 정렬, 부분 수열 문제가 나올 때

## 2. O(N^2) DP

가장 이해하기 쉬운 방식이다.

```python
n = int(input())
arr = list(map(int, input().split()))

dp = [1] * n

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
```

의미:

```text
dp[i] = arr[i]를 마지막 원소로 하는 LIS 길이
```

## 3. O(N^2) 흐름

현재 원소 `arr[i]` 앞에 올 수 있는 원소 `arr[j]`를 찾는다.

```python
if arr[j] < arr[i]:
    dp[i] = max(dp[i], dp[j] + 1)
```

## 4. O(N log N)

길이만 필요하면 이분 탐색을 사용해 더 빠르게 구할 수 있다.

```python
from bisect import bisect_left

lis = []

for x in arr:
    idx = bisect_left(lis, x)

    if idx == len(lis):
        lis.append(x)
    else:
        lis[idx] = x

print(len(lis))
```

## 5. lis 배열의 의미

`O(N log N)` 방식의 `lis` 배열은 실제 LIS 자체가 아니다.

```text
lis[length - 1] = 해당 길이의 증가 부분 수열이 가질 수 있는 마지막 값의 최솟값
```

마지막 값이 작을수록 뒤에 더 많은 값을 붙일 가능성이 커진다.

## 6. strictly increasing vs non-decreasing

엄격하게 증가:

```python
idx = bisect_left(lis, x)
```

같은 값도 허용하는 비감소 수열:

```python
from bisect import bisect_right

idx = bisect_right(lis, x)
```

문제에서 "증가"인지 "감소하지 않는"인지 꼭 확인한다.

## 7. 실제 LIS 복원

길이뿐 아니라 실제 수열이 필요하면 이전 위치를 저장한다.

```python
dp = [1] * n
prev = [-1] * n

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            prev[i] = j

idx = max(range(n), key=lambda i: dp[i])
result = []

while idx != -1:
    result.append(arr[idx])
    idx = prev[idx]

result.reverse()
```

## 8. 복잡도

| 방법 | 복잡도 | 특징 |
| --- | --- | --- |
| DP | `O(N^2)` | 이해와 복원이 쉬움 |
| 이분 탐색 | `O(N log N)` | 길이만 빠르게 구하기 좋음 |

## 9. 자주 하는 실수

### 부분 배열과 부분 수열 혼동

부분 배열은 연속해야 하지만, 부분 수열은 연속하지 않아도 된다.

### 같은 값 처리

`<`인지 `<=`인지 문제 조건을 확인한다.

### O(N log N)의 lis를 실제 답으로 착각

`lis`는 길이를 구하기 위한 보조 배열이다.

## 10. 정리

LIS는 순서를 유지하면서 가장 긴 증가 흐름을 찾는 DP 문제이다. 처음에는 `O(N^2)`로 의미를 이해하고, 입력이 크면 이분 탐색 방식으로 최적화한다.
