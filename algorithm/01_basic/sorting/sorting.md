# Sorting

정렬은 데이터를 특정 기준에 맞게 순서대로 배치하는 알고리즘이다. 문제 풀이에서는 정렬 자체가 목적이기보다는, 정렬 후에 탐색이나 비교를 쉽게 만들기 위해 사용한다.

## 1. 언제 정렬을 떠올리는가

다음 상황에서는 정렬을 먼저 생각해볼 수 있다.

- 작은 값부터 또는 큰 값부터 처리해야 한다.
- 같은 값끼리 묶어야 한다.
- 가장 가까운 두 값, 가장 큰 차이 등을 찾아야 한다.
- 회의실 배정처럼 기준에 따라 순서대로 선택해야 한다.
- 이분 탐색, 투 포인터, 스위핑의 전처리가 필요하다.
- 좌표나 이벤트를 순서대로 처리해야 한다.

## 2. Python 기본 정렬

```python
arr = [3, 1, 4, 2]

arr.sort()
print(arr)  # [1, 2, 3, 4]
```

`sort()`는 원본 리스트를 직접 바꾼다.

```python
arr = [3, 1, 4, 2]
new_arr = sorted(arr)

print(arr)     # [3, 1, 4, 2]
print(new_arr) # [1, 2, 3, 4]
```

`sorted()`는 정렬된 새 리스트를 반환한다.

## 3. 오름차순과 내림차순

```python
arr.sort()
arr.sort(reverse=True)
```

## 4. key 정렬

튜플이나 리스트를 특정 기준으로 정렬할 때 `key`를 사용한다.

```python
items = [('a', 3), ('b', 1), ('c', 2)]

items.sort(key=lambda x: x[1])
print(items)  # [('b', 1), ('c', 2), ('a', 3)]
```

## 5. 여러 기준 정렬

여러 기준을 적용하려면 튜플을 반환한다.

```python
students = [
    ('kim', 90),
    ('lee', 90),
    ('park', 80),
]

students.sort(key=lambda x: (-x[1], x[0]))
```

의미:

```text
1. 점수는 내림차순
2. 점수가 같으면 이름은 오름차순
```

숫자 내림차순은 음수로 바꾸면 된다.

```python
key=lambda x: -x[1]
```

문자열 내림차순은 단순히 음수로 바꿀 수 없으므로 `reverse=True`나 다른 방식을 고려해야 한다.

## 6. 안정 정렬

Python 정렬은 안정 정렬이다. 값이 같은 원소끼리는 기존 순서가 유지된다.

그래서 여러 번 나누어 정렬할 수 있다.

```python
students.sort(key=lambda x: x[0])
students.sort(key=lambda x: x[1], reverse=True)
```

먼저 이름으로 정렬하고, 그 다음 점수로 정렬한다. 점수가 같은 원소 사이에서는 이름 정렬이 유지된다.

## 7. 정렬 후 인접 비교

가장 가까운 두 값은 정렬 후 인접한 위치에 있다.

```python
arr.sort()
answer = 10**18

for i in range(1, len(arr)):
    answer = min(answer, arr[i] - arr[i - 1])
```

정렬하지 않으면 모든 쌍을 비교해야 해서 `O(N^2)`이 될 수 있다.

## 8. 정렬 후 그리디

정렬은 그리디 알고리즘의 전처리로 자주 사용된다.

예를 들어 회의실 배정에서는 끝나는 시간이 빠른 회의부터 선택한다.

```python
meetings.sort(key=lambda x: (x[1], x[0]))

end_time = 0
count = 0

for start, end in meetings:
    if start >= end_time:
        count += 1
        end_time = end
```

## 9. 정렬과 이분 탐색

이분 탐색은 정렬된 배열에서만 사용할 수 있다.

```python
arr.sort()

from bisect import bisect_left

idx = bisect_left(arr, target)
```

## 10. 정렬과 스위핑

이벤트를 좌표나 시간 순서대로 처리하려면 정렬이 필요하다.

```python
events.sort()

for position, event_type in events:
    pass
```

## 11. 복잡도

Python의 `sort()`와 `sorted()`는 Timsort를 사용한다.

| 연산 | 시간 복잡도 |
| --- | --- |
| 정렬 | `O(N log N)` |
| 이미 거의 정렬된 데이터 | 더 빠르게 동작할 수 있음 |

## 12. 자주 하는 실수

### 문자열 숫자 정렬

```python
arr = ['10', '2', '1']
arr.sort()
print(arr)  # ['1', '10', '2']
```

숫자 기준으로 정렬하려면 정수로 변환해야 한다.

```python
arr.sort(key=int)
```

### 원본 보존

원본이 필요하면 `sorted()`를 사용한다.

```python
new_arr = sorted(arr)
```

### 여러 기준 방향

오름차순과 내림차순이 섞이면 `key`를 신중하게 작성한다.

```python
items.sort(key=lambda x: (x[0], -x[1]))
```

## 13. 정리

정렬은 단독 알고리즘이면서 동시에 다른 알고리즘의 전처리이다. 정렬 후에는 인접 원소 비교, 이분 탐색, 투 포인터, 스위핑, 그리디를 적용할 수 있는지 확인한다.
