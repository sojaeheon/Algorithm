# Memoization

메모이제이션은 재귀 함수의 결과를 저장해 같은 상태를 다시 계산하지 않는 기법이다. Top-down DP라고도 한다.

## 1. 언제 쓰는가

- 재귀로 문제를 표현하는 것이 자연스럽다.
- 같은 인자로 함수가 반복 호출된다.
- 모든 상태를 미리 채우기보다 필요한 상태만 계산하고 싶다.
- 완전 탐색을 하되 중복 상태가 많다.

## 2. 기본 구조

```python
memo = {}

def solve(x):
    if x in memo:
        return memo[x]

    if x == 0:
        return 1

    memo[x] = solve(x - 1)
    return memo[x]
```

## 3. 피보나치 예시

메모이제이션이 없으면 같은 값이 계속 다시 계산된다.

```python
memo = [-1] * (n + 1)

def fib(x):
    if x <= 1:
        return x

    if memo[x] != -1:
        return memo[x]

    memo[x] = fib(x - 1) + fib(x - 2)
    return memo[x]
```

## 4. 배열 vs dict

| 방식 | 사용 상황 |
| --- | --- |
| 리스트 | 상태가 정수이고 범위가 작다 |
| dict | 상태가 튜플이거나 범위가 크지만 실제 방문 상태가 적다 |

튜플 상태 예시:

```python
memo = {}

def solve(i, j):
    if (i, j) in memo:
        return memo[(i, j)]

    memo[(i, j)] = solve(i - 1, j) + solve(i, j - 1)
    return memo[(i, j)]
```

## 5. functools.cache

Python에서는 데코레이터를 사용할 수도 있다.

```python
from functools import cache

@cache
def solve(x):
    if x <= 1:
        return x
    return solve(x - 1) + solve(x - 2)
```

## 6. 기저 조건

재귀가 끝나는 조건을 반드시 먼저 생각한다.

```python
if x <= 1:
    return x
```

상태에 따라 기저 조건과 메모 확인 순서는 달라질 수 있다. 인덱스 범위 밖으로 나갈 수 있다면 범위 확인을 먼저 한다.

## 7. 자주 하는 실수

### 저장하지 않고 반환

```python
return solve(x - 1) + solve(x - 2)
```

이렇게만 쓰면 같은 계산을 계속 반복한다.

### 상태가 여러 개인데 하나만 저장

`solve(i, j)`라면 `(i, j)`를 key로 저장해야 한다.

### 재귀 깊이 초과

상태가 깊게 이어지면 `sys.setrecursionlimit`이 필요할 수 있다.

## 8. 정리

메모이제이션은 재귀 풀이에 저장을 더한 것이다. 같은 상태가 반복된다면 결과를 저장해서 완전 탐색을 DP로 바꿀 수 있다.
