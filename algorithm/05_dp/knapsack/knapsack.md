# Knapsack

배낭 DP는 제한된 용량 안에서 물건을 선택해 최대 가치나 가능한 상태를 구하는 DP이다.

가장 대표적인 형태는 **0/1 배낭**이다.

## 1. 언제 쓰는가

- 여러 물건 중 일부를 선택한다.
- 각 물건에는 무게와 가치가 있다.
- 전체 무게 제한이 있다.
- 제한 안에서 최대 가치를 구해야 한다.
- 같은 물건을 한 번만 쓸 수 있거나, 여러 번 쓸 수 있다.

## 2. 0/1 배낭

각 물건을 최대 한 번만 선택할 수 있다.

```python
n, capacity = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(n)]

dp = [0] * (capacity + 1)

for weight, value in items:
    for w in range(capacity, weight - 1, -1):
        dp[w] = max(dp[w], dp[w - weight] + value)

print(dp[capacity])
```

## 3. dp 의미

```text
dp[w] = 현재까지 본 물건들로 무게 w 이하를 사용할 때의 최대 가치
```

## 4. 왜 뒤에서 앞으로 도는가

0/1 배낭에서는 한 물건을 한 번만 써야 한다.

만약 앞에서부터 돌면 같은 물건을 여러 번 사용하는 효과가 생긴다.

```python
for w in range(capacity, weight - 1, -1):
    dp[w] = max(dp[w], dp[w - weight] + value)
```

뒤에서 앞으로 돌면 `dp[w - weight]`가 현재 물건을 사용하기 전 상태를 유지한다.

## 5. 무한 배낭

같은 물건을 여러 번 사용할 수 있는 경우이다.

```python
for weight, value in items:
    for w in range(weight, capacity + 1):
        dp[w] = max(dp[w], dp[w - weight] + value)
```

앞에서부터 돌면 방금 갱신한 값을 다시 사용해 같은 물건을 여러 번 선택할 수 있다.

## 6. 2차원 DP 형태

처음 공부할 때는 2차원 DP가 더 이해하기 쉽다.

```python
dp = [[0] * (capacity + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    weight, value = items[i - 1]

    for w in range(capacity + 1):
        dp[i][w] = dp[i - 1][w]

        if w >= weight:
            dp[i][w] = max(dp[i][w], dp[i - 1][w - weight] + value)
```

의미:

```text
dp[i][w] = i번째 물건까지 고려했고, 용량이 w일 때의 최대 가치
```

## 7. 0/1 배낭과 무한 배낭 비교

| 구분 | 순회 방향 | 의미 |
| --- | --- | --- |
| 0/1 배낭 | 뒤에서 앞으로 | 각 물건 한 번만 사용 |
| 무한 배낭 | 앞에서 뒤로 | 같은 물건 여러 번 사용 가능 |

## 8. 자주 하는 실수

### 순회 방향 실수

0/1 배낭인데 앞에서부터 돌면 같은 물건을 여러 번 쓴다.

### weight와 value 순서 혼동

입력이 `무게 가치`인지 `가치 무게`인지 확인한다.

### dp 의미 불명확

`dp[w]`가 정확히 무엇인지 먼저 정하고 시작한다.

## 9. 정리

배낭 DP의 핵심은 "이 물건을 선택할 것인가, 선택하지 않을 것인가"이다. 0/1 배낭은 뒤에서 앞으로, 무한 배낭은 앞에서 뒤로 갱신한다.
