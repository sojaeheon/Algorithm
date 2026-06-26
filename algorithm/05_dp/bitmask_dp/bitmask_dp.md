# Bitmask DP

비트마스크 DP는 선택한 원소 집합이나 방문한 정점 집합을 정수의 비트로 표현하는 DP이다.

## 1. 언제 쓰는가

- 원소 개수가 작다.
- 방문한 집합이 상태에 포함된다.
- 모든 부분집합을 상태로 다뤄야 한다.
- 외판원 순회(TSP)처럼 현재 위치와 방문 집합이 모두 중요하다.
- `N <= 20` 정도의 조건이 보인다.

## 2. 비트마스크 기본

`mask`의 i번째 비트가 1이면 i번 원소를 선택했다는 뜻으로 볼 수 있다.

```python
if mask & (1 << i):
    print("i is selected")
```

선택 추가:

```python
next_mask = mask | (1 << i)
```

선택 제거:

```python
next_mask = mask & ~(1 << i)
```

## 3. 기본 상태

가장 자주 쓰는 형태:

```python
dp[mask][i]
```

의미 예시:

```text
mask = 방문한 정점 집합
i = 현재 위치
dp[mask][i] = mask만큼 방문했고 현재 i에 있을 때의 최소 비용
```

## 4. TSP 형태

```python
INF = 10**18
dp = [[INF] * n for _ in range(1 << n)]
dp[1][0] = 0

for mask in range(1 << n):
    for now in range(n):
        if dp[mask][now] == INF:
            continue

        for nxt in range(n):
            if mask & (1 << nxt):
                continue
            if cost[now][nxt] == 0:
                continue

            next_mask = mask | (1 << nxt)
            dp[next_mask][nxt] = min(
                dp[next_mask][nxt],
                dp[mask][now] + cost[now][nxt],
            )
```

## 5. 모든 부분집합 순회

```python
for mask in range(1 << n):
    for i in range(n):
        if mask & (1 << i):
            pass
```

## 6. 부분집합의 부분집합 순회

어떤 `mask`의 부분집합만 순회할 수도 있다.

```python
sub = mask

while sub:
    # sub는 mask의 부분집합
    sub = (sub - 1) & mask
```

빈 집합까지 포함하려면 마지막에 따로 처리하거나 `while True` 형태를 사용한다.

## 7. 복잡도

상태 수가 `2^N`이므로 입력 크기를 반드시 확인해야 한다.

| 형태 | 복잡도 |
| --- | --- |
| `dp[mask]` | `O(2^N)` |
| `dp[mask][i]` | `O(N * 2^N)` |
| TSP 전이 | `O(N^2 * 2^N)` |

## 8. 자주 하는 실수

### N이 너무 큰 경우

`2^N`은 빠르게 커진다.

```text
N = 20 -> 약 1,048,576
N = 25 -> 약 33,000,000
```

### 시작 mask 설정

0번에서 시작하면 보통 다음처럼 시작한다.

```python
dp[1 << 0][0] = 0
```

### 방문 확인 반대

이미 방문한 곳은 건너뛴다.

```python
if mask & (1 << nxt):
    continue
```

## 9. 정리

비트마스크 DP는 집합 상태를 정수 하나로 압축해서 다루는 DP이다. 강력하지만 상태 수가 `2^N`이므로, 항상 입력 크기부터 확인해야 한다.
