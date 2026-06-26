# Recursion

재귀는 함수가 자기 자신을 호출해서 문제를 더 작은 문제로 나누는 방법이다.

DFS, 백트래킹, 트리 순회, 순열/조합/부분집합, 메모이제이션의 기반이 된다.

## 1. 기본 구조

재귀 함수에는 반드시 멈추는 조건이 있어야 한다.

```python
def solve(x):
    if x == 0:
        return

    solve(x - 1)
```

## 2. 재귀의 필수 요소

| 요소 | 의미 |
| --- | --- |
| 기저 조건 | 재귀를 멈추는 조건 |
| 상태 변화 | 다음 호출에서 문제가 더 작아져야 함 |
| 반환 또는 복구 | 결과를 반환하거나 상태를 되돌림 |

## 3. 팩토리얼

```python
def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n - 1)
```

의미:

```text
factorial(n) = n * factorial(n - 1)
```

## 4. DFS

```python
def dfs(now):
    visited[now] = True

    for nxt in graph[now]:
        if visited[nxt]:
            continue
        dfs(nxt)
```

재귀 호출이 그래프를 깊게 탐색하는 역할을 한다.

## 5. 백트래킹

재귀 호출 후 상태를 원래대로 되돌리는 방식이다.

```python
def backtrack(depth):
    if depth == r:
        print(path)
        return

    for i in range(n):
        if used[i]:
            continue

        used[i] = True
        path.append(arr[i])
        backtrack(depth + 1)
        path.pop()
        used[i] = False
```

## 6. 상태 복구

백트래킹에서 가장 중요한 부분이다.

```python
path.append(x)
backtrack()
path.pop()
```

`append`로 바꾼 상태는 재귀 호출이 끝난 뒤 반드시 되돌려야 한다.

## 7. 재귀 깊이

Python은 재귀 깊이 제한이 있다. 깊은 DFS를 할 때는 제한을 늘릴 수 있다.

```python
import sys
sys.setrecursionlimit(10**6)
```

그래도 너무 깊은 재귀는 스택 메모리 문제가 생길 수 있으므로, 필요하면 반복문이나 직접 스택 구현을 고려한다.

## 8. 재귀를 떠올리는 상황

- 같은 구조가 반복된다.
- 트리나 그래프를 깊게 탐색한다.
- 선택하고 다음 단계로 넘어간다.
- 가능한 모든 경우를 만들어야 한다.
- 작은 문제의 답으로 큰 문제를 만든다.

## 9. 자주 하는 실수

### 기저 조건 누락

기저 조건이 없으면 무한 재귀가 된다.

### 상태가 줄어들지 않음

```python
solve(x)
```

처럼 같은 상태를 다시 호출하면 끝나지 않는다.

### 상태 복구 누락

백트래킹에서 `pop()`이나 `used[i] = False`를 빼먹으면 다음 경우가 망가진다.

### 반환값 누락

값을 계산하는 재귀에서는 `return`을 잊지 않는다.

## 10. 정리

재귀는 문제를 작은 문제로 나누어 해결하는 방식이다. 핵심은 기저 조건, 상태 변화, 상태 복구이다.
