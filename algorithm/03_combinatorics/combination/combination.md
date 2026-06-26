# Combination

조합은 여러 원소 중 일부를 **순서를 고려하지 않고** 고르는 것이다.

```text
[1, 2]와 [2, 1]은 같은 조합이다.
```

## 1. 언제 쓰는가

- 팀을 나눌 때
- 재료를 고를 때
- 여러 원소 중 `R`개를 선택할 때
- 선택 순서가 결과에 영향을 주지 않을 때
- 부분집합 중 크기가 정해진 경우를 볼 때

문제에서 "몇 개를 고른다", "선택한다", "순서는 상관없다"는 느낌이면 조합을 생각한다.

## 2. 경우의 수

`N`개 중 `R`개를 순서 없이 고르면:

```text
NCr = N! / (R! * (N - R)!)
```

예를 들어 5개 중 3개를 고르면:

```text
5C3 = 10
```

## 3. itertools 사용

```python
from itertools import combinations

arr = [1, 2, 3]

for case in combinations(arr, 2):
    print(case)
```

출력:

```text
(1, 2)
(1, 3)
(2, 3)
```

## 4. 직접 구현

조합에서는 다음에 고를 원소의 시작 위치를 넘겨준다.

```python
def make_comb(start, path):
    if len(path) == r:
        print(path)
        return

    for i in range(start, n):
        path.append(arr[i])
        make_comb(i + 1, path)
        path.pop()


arr = [1, 2, 3]
n = len(arr)
r = 2
make_comb(0, [])
```

## 5. 왜 `i + 1`인가

조합은 이미 고른 원소보다 뒤에 있는 원소만 선택하면 된다.

```text
[1, 2]를 만들었다면 [2, 1]은 다시 만들 필요가 없다.
```

그래서 재귀 호출을 할 때 다음 시작 위치를 `i + 1`로 넘긴다.

## 6. 가지치기

남은 원소 수가 부족하면 더 탐색할 필요가 없다.

```python
def make_comb(start, path):
    if len(path) == r:
        print(path)
        return

    need = r - len(path)

    for i in range(start, n - need + 1):
        path.append(arr[i])
        make_comb(i + 1, path)
        path.pop()
```

## 7. 중복 원소가 있는 조합

중복된 값으로 같은 조합이 여러 번 나오는 것을 막으려면 정렬 후 같은 깊이에서 같은 값을 건너뛴다.

```python
arr.sort()

def make_comb(start, path):
    if len(path) == r:
        print(path)
        return

    prev = None

    for i in range(start, n):
        if prev == arr[i]:
            continue

        prev = arr[i]
        path.append(arr[i])
        make_comb(i + 1, path)
        path.pop()
```

## 8. 순열과 비교

| 구분 | 순열 | 조합 |
| --- | --- | --- |
| 순서 | 중요 | 중요하지 않음 |
| 예시 | `[1, 2]`, `[2, 1]` 다름 | `[1, 2]`, `[2, 1]` 같음 |
| 구현 핵심 | `used` 배열 | `start` 인덱스 |

## 9. 자주 하는 실수

### `i + 1` 대신 `start + 1` 사용

```python
make_comb(i + 1, path)
```

선택한 위치 다음부터 봐야 하므로 `i + 1`이 맞다.

### 순서가 필요한 문제를 조합으로 푸는 경우

순서에 따라 결과가 달라지면 조합이 아니라 순열이다.

### 상태 복구 누락

```python
path.append(arr[i])
make_comb(i + 1, path)
path.pop()
```

## 10. 정리

조합은 순서가 중요하지 않은 선택 문제에 사용한다. 핵심은 `start` 인덱스를 이용해 이미 본 원소를 다시 보지 않게 만드는 것이다.
