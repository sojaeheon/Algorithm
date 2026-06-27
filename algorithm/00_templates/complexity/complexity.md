# Complexity

시간복잡도는 입력 크기가 커질 때 실행 시간이 얼마나 빠르게 증가하는지 나타낸다. 공간복잡도는 입력 크기가 커질 때 추가로 사용하는 메모리가 얼마나 증가하는지 나타낸다.

알고리즘 문제를 풀 때는 먼저 입력 크기를 보고 가능한 시간복잡도를 예상해야 한다.

## 1. Big-O

Big-O는 가장 큰 증가율만 남겨서 표현한다.

```text
3N + 10      -> O(N)
N^2 + 5N     -> O(N^2)
N log N + N  -> O(N log N)
```

상수와 낮은 차수 항은 보통 생략한다.

## 2. 자주 나오는 복잡도

| 복잡도 | 느낌 | 예시 |
| --- | --- | --- |
| `O(1)` | 입력 크기와 무관 | 인덱스 접근 |
| `O(log N)` | 매우 빠름 | 이분 탐색 |
| `O(N)` | 한 번 순회 | 배열 순회 |
| `O(N log N)` | 정렬 수준 | 정렬, 힙 기반 알고리즘 |
| `O(N^2)` | 모든 쌍 확인 | 이중 반복문 |
| `O(N^3)` | 모든 삼중 조합 | Floyd-Warshall |
| `O(2^N)` | 모든 부분집합 | 부분집합 탐색 |
| `O(N!)` | 모든 순열 | 순열 완전 탐색 |

## 3. 반복문 계산

### 한 번 순회

```python
for i in range(n):
    print(i)
```

`n`번 실행되므로 `O(N)`이다.

### 중첩 반복문

```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

`n * n`번 실행되므로 `O(N^2)`이다.

### 범위가 다른 중첩 반복문

```python
for i in range(n):
    for j in range(m):
        print(i, j)
```

`n * m`번 실행되므로 `O(NM)`이다.

## 4. 삼각형 반복문

```python
for i in range(n):
    for j in range(i):
        print(i, j)
```

실행 횟수는 다음과 같다.

```text
0 + 1 + 2 + ... + (N - 1) = N(N - 1) / 2
```

따라서 `O(N^2)`이다.

상수 `1/2`은 Big-O에서 생략한다.

## 5. 반씩 줄어드는 반복문

```python
while n > 1:
    n //= 2
```

입력이 매번 절반으로 줄어드므로 `O(log N)`이다.

이분 탐색도 같은 이유로 `O(log N)`이다.

## 6. 정렬

Python의 `sort()`와 `sorted()`는 보통 `O(N log N)`으로 생각한다.

```python
arr.sort()
```

정렬 후 한 번 순회하면:

```python
arr.sort()

for x in arr:
    print(x)
```

전체는 `O(N log N + N)`이고, 큰 항만 남기면 `O(N log N)`이다.

## 7. 자료구조 연산 포함

반복문 안에서 자료구조 연산을 사용하면 그 연산 비용도 곱해진다.

```python
for x in arr:
    heapq.heappush(heap, x)
```

`heappush`가 `O(log N)`이고 `N`번 실행되므로 `O(N log N)`이다.

```python
for x in arr:
    if x in seen:
        pass
```

`seen`이 `set`이면 평균 `O(1)` 검색이므로 전체 `O(N)`이다.

하지만 `seen`이 `list`이면 `x in seen`이 `O(N)`이라 전체 `O(N^2)`이 될 수 있다.

## 8. 재귀 복잡도

재귀는 호출 횟수와 각 호출에서 하는 일을 곱해서 생각한다.

### 피보나치 단순 재귀

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

같은 계산이 반복되어 대략 `O(2^N)`이다.

### 메모이제이션

```python
memo = [-1] * (n + 1)

def fib(n):
    if n <= 1:
        return n
    if memo[n] != -1:
        return memo[n]
    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]
```

각 상태를 한 번만 계산하므로 `O(N)`이다.

## 9. 그래프 복잡도

그래프에서는 보통 정점 수를 `V`, 간선 수를 `E`로 표현한다.

| 알고리즘 | 복잡도 |
| --- | --- |
| BFS | `O(V + E)` |
| DFS | `O(V + E)` |
| Dijkstra | `O(E log V)` |
| Bellman-Ford | `O(VE)` |
| Floyd-Warshall | `O(V^3)` |
| Kruskal | `O(E log E)` |

## 10. 공간복잡도

공간복잡도는 추가로 사용하는 메모리를 계산한다.

### 배열 하나

```python
arr = [0] * n
```

`O(N)` 공간을 사용한다.

### 2차원 배열

```python
dp = [[0] * m for _ in range(n)]
```

`O(NM)` 공간을 사용한다.

### 그래프 인접 리스트

```python
graph = [[] for _ in range(n + 1)]
```

정점과 간선을 저장하므로 `O(V + E)` 공간을 사용한다.

## 11. 재귀의 공간복잡도

재귀 호출은 콜 스택을 사용한다.

```python
def dfs(now):
    for nxt in graph[now]:
        dfs(nxt)
```

최대 재귀 깊이가 `N`이면 콜 스택 공간은 `O(N)`이다.

## 12. 입력 크기별 대략 가능한 복잡도

일반적으로 1초에 Python은 대략 수천만 단위 연산보다 훨씬 여유 있게 잡는 것이 안전하다. 문제마다 다르지만 다음 표를 기준으로 판단한다.

| 입력 크기 | 보통 가능한 복잡도 |
| --- | --- |
| `N <= 10` | `O(N!)`, `O(2^N)` 가능 |
| `N <= 20` | `O(2^N)`, `O(N * 2^N)` 가능할 수 있음 |
| `N <= 500` | `O(N^3)` 가능할 수 있음 |
| `N <= 2,000` | `O(N^2)` 가능할 수 있음 |
| `N <= 100,000` | `O(N log N)`, `O(N)` 필요 |
| `N >= 1,000,000` | 거의 `O(N)` 또는 `O(log N)` 필요 |

## 13. 문제 풀이에서 계산하는 순서

1. 입력 크기 `N`, `M`, `V`, `E`를 확인한다.
2. 제한 시간과 메모리 제한을 확인한다.
3. 완전 탐색이 가능한지 먼저 계산한다.
4. 정렬, 이분 탐색, DP, 그래프 알고리즘 중 가능한 복잡도를 고른다.
5. 코드 작성 후 반복문과 자료구조 연산을 다시 확인한다.

## 14. 자주 하는 실수

### 중첩 반복문 안의 `in`

```python
for x in arr:
    if x in other_list:
        pass
```

`other_list`가 리스트면 검색이 `O(N)`이라 전체가 `O(N^2)`이 될 수 있다. `set`으로 바꾸면 평균 `O(N)`이 된다.

### 슬라이싱 비용 무시

```python
for i in range(n):
    part = arr[i:i + k]
```

슬라이싱은 길이만큼 복사하므로 `O(K)`이다.

### sort를 반복문 안에서 사용

```python
for _ in range(n):
    arr.sort()
```

`O(N * N log N)`이 될 수 있다.

### 공간복잡도 누락

시간은 맞아도 `N * M` 크기의 2차원 배열이 너무 크면 메모리 초과가 날 수 있다.

## 15. 정리

복잡도 계산은 코드가 입력 크기에 따라 얼마나 커지는지 보는 과정이다. 반복문 횟수, 자료구조 연산 비용, 재귀 호출 수, 추가 배열 크기를 각각 확인하면 대부분의 문제에서 시간복잡도와 공간복잡도를 계산할 수 있다.
