# JUNGOL 학습 메모

문제를 풀면서 헷갈렸던 문법, 구현 패턴, 시간/메모리 판단을 따로 모아두는 문서입니다.

## 목차

### 주제별 메모

| 번호 | 주제 | 관련 문제 |
| --- | --- | --- |
| 1 | [heapq에서 튜플 비교](#note-01-heapq-tuple) | [3337 쇼핑몰](gold/3337_ShoppingMall.py) |
| 2 | [정렬 기준에서 일부만 내림차순 처리](#note-02-sort-reverse-part) | [3337 쇼핑몰](gold/3337_ShoppingMall.py) |
| 3 | [enumerate(arr, start=1)](#note-03-enumerate-start) | [3337 쇼핑몰](gold/3337_ShoppingMall.py) |
| 4 | [`_`로 사용하지 않는 값 받기](#note-04-unused-underscore) | [3337 쇼핑몰](gold/3337_ShoppingMall.py) |
| 5 | [meet in the middle](#note-05-meet-in-the-middle) | [1357 합이 0이 되는 4개의 숫자들](gold/1357_FourNumbersSumZero.py) |
| 6 | [Counter와 defaultdict 차이](#note-06-counter-defaultdict) | [1357 합이 0이 되는 4개의 숫자들](gold/1357_FourNumbersSumZero.py) |
| 7 | [bisect와 이분 탐색](#note-07-bisect-binary-search) | [1357 합이 0이 되는 4개의 숫자들](gold/1357_FourNumbersSumZero.py) |
| 8 | [Python 시간/메모리 판단](#note-08-python-limits) | [1357 합이 0이 되는 4개의 숫자들](gold/1357_FourNumbersSumZero.py) |

### 문제별 메모

| 문제 | 배운 내용 |
| --- | --- |
| [3337 쇼핑몰](#problem-3337-shopping-mall) | heapq 튜플 비교, 정렬 기준, enumerate, `_` |
| [1357 합이 0이 되는 4개의 숫자들](#problem-1357-four-numbers-sum-zero) | meet in the middle, Counter, defaultdict, bisect |

## 주제별 메모

## note-01-heapq-tuple

### heapq에서 튜플 비교

`heapq`에 튜플을 넣으면 튜플의 앞쪽 값부터 차례대로 비교합니다.

```python
(계산 종료 시간, 계산대 번호)
```

우선순위:

```text
1. 계산 종료 시간이 작은 값
2. 종료 시간이 같으면 계산대 번호가 작은 값
```

## note-02-sort-reverse-part

### 정렬 기준에서 일부만 내림차순 처리

정렬 기준 중 일부만 내림차순으로 하고 싶으면 숫자에 `-`를 붙일 수 있습니다.

```python
finished.sort(key=lambda x: (x[0], -x[1]))
```

의미:

```text
1. x[0] = 종료 시간 오름차순
2. -x[1] = 계산대 번호 내림차순
```

## note-03-enumerate-start

### enumerate(arr, start=1)

`enumerate()`는 리스트를 반복하면서 순서 번호를 함께 꺼내는 함수입니다.

```python
for order, value in enumerate(arr, start=1):
    print(order, value)
```

`start=1`을 쓰면 번호가 `0`이 아니라 `1`부터 시작합니다.

## note-04-unused-underscore

### `_`로 사용하지 않는 값 받기

`_`는 값을 받기는 하지만 사용하지 않겠다는 표시로 자주 씁니다.

```python
_, _, customer_id = (10, 3, 123)
```

## note-05-meet-in-the-middle

### meet in the middle

`meet in the middle`은 전체를 한 번에 탐색하기 어려울 때, 문제를 두 묶음으로 나누어 각각의 결과를 만든 뒤 가운데에서 합치는 방식입니다.

1357 문제의 조건:

```text
A + B + C + D = 0
```

이걸 두 묶음으로 나눕니다.

```text
A + B = -(C + D)
```

4중 반복을 하면 `O(N^4)`이지만, 두 묶음으로 나누면 `O(N^2)`로 줄일 수 있습니다.

## note-06-counter-defaultdict

### Counter와 defaultdict 차이

`Counter`와 `defaultdict(int)`는 둘 다 값의 개수를 셀 때 사용할 수 있습니다.

개수를 늘릴 때는 둘 다 비슷합니다.

```python
from collections import Counter, defaultdict

counter_count = Counter()
default_count = defaultdict(int)

counter_count[10] += 1
default_count[10] += 1
```

하지만 **없는 key를 조회할 때** 차이가 큽니다.

`Counter`는 없는 key를 조회해도 key를 새로 만들지 않습니다.

```python
from collections import Counter

count = Counter()

print(count[100])  # 0
print(count)       # Counter()
```

`defaultdict(int)`는 없는 key를 `[]`로 조회하면 key를 새로 만듭니다.

```python
from collections import defaultdict

count = defaultdict(int)

print(count[100])  # 0
print(count)       # defaultdict(<class 'int'>, {100: 0})
```

1357에서 아래처럼 쓰면 문제가 됩니다.

```python
answer += sum_ab[target]
```

`target`이 `sum_ab`에 없을 때, `defaultdict(int)`는 `target: 0`을 새로 추가합니다.  
`C+D`를 탐색하는 동안 없는 target이 많이 나오면 key가 계속 늘어나서 메모리 초과가 날 수 있습니다.

`defaultdict(int)`를 꼭 쓰고 싶다면 `.get()`을 써야 합니다.

```python
answer += sum_ab.get(target, 0)
```

`.get()`은 없는 key를 조회해도 key를 새로 만들지 않습니다.

1357에서는 `Counter`가 더 안전합니다.

```python
sum_ab = Counter()

for a in A:
    for b in B:
        sum_ab[a + b] += 1

answer += sum_ab[target]
```

## note-07-bisect-binary-search

### bisect와 이분 탐색

`bisect`는 정렬된 리스트에서 어떤 값이 들어갈 위치를 빠르게 찾는 도구입니다.

```python
from bisect import bisect_left, bisect_right

arr = [1, 2, 2, 2, 4, 5]

left = bisect_left(arr, 2)
right = bisect_right(arr, 2)

print(right - left)  # 3
```

의미:

```text
bisect_left(arr, x): x가 처음 나올 수 있는 위치
bisect_right(arr, x): x보다 큰 값이 처음 나오는 위치
right - left: x의 개수
```

왜 빠른가:

```text
일반 탐색: 앞에서부터 하나씩 확인하므로 O(N)
bisect: 범위를 절반씩 줄이며 찾으므로 O(log N)
```

1357의 bisect 대안:

```python
cd_sums.sort()

for a in A:
    for b in B:
        target = -(a + b)
        answer += bisect_right(cd_sums, target) - bisect_left(cd_sums, target)
```

하지만 `N=4000`이면 `A+B` 경우가 16,000,000개라 `bisect_left/right` 호출이 너무 많아질 수 있습니다.  
그래서 이 문제는 평균 `O(1)` 해시 조회를 사용하는 Counter 풀이가 더 빠릅니다.

## note-08-python-limits

### Python 시간/메모리 판단

1357 문제는 `N=4000`이므로 `N^2 = 16,000,000`입니다.

풀이 선택:

| 방식 | 특징 |
| --- | --- |
| Counter/hash | 평균 `O(1)` 조회라 빠르지만, 서로 다른 합이 많으면 메모리를 많이 쓴다 |
| defaultdict(int) + `[]` 조회 | 없는 key를 새로 만들어 메모리 초과가 날 수 있다 |
| defaultdict(int) + `.get()` 조회 | 없는 key를 만들지 않아 Counter와 비슷하게 사용할 수 있다 |
| 리스트 + bisect | 메모리는 예측하기 쉽지만, `bisect` 호출이 많으면 시간 초과가 날 수 있다 |

정리:

```text
Counter가 빠른 이유는 Counter 자체의 마법이라기보다 해시 조회가 평균 O(1)이기 때문이다.
sys.stdin.buffer.read()는 입력을 빠르게 해주는 보조 최적화이다.
defaultdict는 조회 방식에 따라 메모리 사용량이 크게 달라질 수 있다.
```

## 문제별 메모

## problem-3337-shopping-mall

### 3337 쇼핑몰

문제 파일: [3337_ShoppingMall.py](gold/3337_ShoppingMall.py)

배운 내용:

| 주제 | 이유 |
| --- | --- |
| [heapq에서 튜플 비교](#note-01-heapq-tuple) | 계산대를 종료 시간 기준으로 빠르게 배정하기 위해 사용 |
| [정렬 기준에서 일부만 내림차순 처리](#note-02-sort-reverse-part) | 종료 시간이 같을 때 계산대 번호가 큰 손님을 먼저 내보내기 위해 사용 |
| [enumerate(arr, start=1)](#note-03-enumerate-start) | 퇴장 순서를 1부터 계산하기 위해 사용 |
| [`_`로 사용하지 않는 값 받기](#note-04-unused-underscore) | 답 계산에 필요 없는 종료 시간과 계산대 번호를 무시하기 위해 사용 |

## problem-1357-four-numbers-sum-zero

### 1357 합이 0이 되는 4개의 숫자들

문제 파일: [1357_FourNumbersSumZero.py](gold/1357_FourNumbersSumZero.py)

배운 내용:

| 주제 | 이유 |
| --- | --- |
| [meet in the middle](#note-05-meet-in-the-middle) | 4중 반복을 `A+B`, `C+D` 두 묶음으로 줄이기 위해 사용 |
| [Counter와 defaultdict 차이](#note-06-counter-defaultdict) | `defaultdict`가 없는 key를 추가해 메모리 초과를 만들 수 있음을 확인 |
| [bisect와 이분 탐색](#note-07-bisect-binary-search) | 정렬 리스트 기반 대안 풀이와 시간 차이를 이해하기 위해 정리 |
| [Python 시간/메모리 판단](#note-08-python-limits) | 해시, 입력 최적화, 자료구조 선택의 차이를 비교하기 위해 정리 |
