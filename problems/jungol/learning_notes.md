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
| 5 | [meet in the middle](#note-05-meet-in-the-middle) | [1357 합이 0이 되는 4개의 숫자들](platinum/1357_FourNumbersSumZero.py) |
| 6 | [Counter와 defaultdict 차이](#note-06-counter-defaultdict) | [1357 합이 0이 되는 4개의 숫자들](platinum/1357_FourNumbersSumZero.py) |
| 7 | [bisect와 이분 탐색](#note-07-bisect-binary-search) | [1357 합이 0이 되는 4개의 숫자들](platinum/1357_FourNumbersSumZero.py) |
| 8 | [Python 시간/메모리 판단](#note-08-python-limits) | [1357 합이 0이 되는 4개의 숫자들](platinum/1357_FourNumbersSumZero.py) |
| 9 | [좌표 압축](#note-09-coordinate-compression) | [2587 달리기](platinum/2587_Running.py) |
| 10 | [Fenwick Tree](#note-10-fenwick-tree) | [2587 달리기](platinum/2587_Running.py) |
| 11 | [Segment Tree](#note-11-segment-tree) | [2587 달리기](platinum/2587_Running.py) |
| 12 | [Fenwick Tree와 Segment Tree 차이](#note-12-fenwick-vs-segment) | [2587 달리기](platinum/2587_Running.py) |
| 13 | [DFS 백트래킹](#note-13-dfs-backtracking) | [1681 해밀턴 순환회로](silver/1681_HamiltonianCycle.py) |
| 14 | [해밀턴 순환회로](#note-14-hamiltonian-cycle) | [1681 해밀턴 순환회로](silver/1681_HamiltonianCycle.py) |
| 15 | [nonlocal](#note-15-nonlocal) | [1681 해밀턴 순환회로](silver/1681_HamiltonianCycle.py) |
| 16 | [비트마스크 DP](#note-16-bitmask-dp) | [1545 해밀턴 순환회로 2](platinum/1545_HamiltonianCycle2.py) |
| 17 | [단조 스택](#note-17-monotone-stack) | [1809 탑](gold/1809_Tower.py), [1214 히스토그램](platinum/1214_Histogram.py) |
| 18 | [회의실 배정 그리디](#note-18-meeting-room-greedy) | [1370 회의실 배정](silver/1370_MeetingRoomAssignment.py) |
| 19 | [매개변수 탐색](#note-19-parametric-search) | [2581 예산](silver/2581_Budget.py) |
| 20 | [투 포인터](#note-20-two-pointer) | [2300 용액](gold/2300_Solution.py) |
| 21 | [누적합과 해시](#note-21-prefix-sum-hash) | [3706 합이 0이 되는 연속구간 세기](silver/3706_CountZeroSumSubarrays.py) |
| 22 | [반복 DFS와 stack](#note-22-iterative-dfs-stack) | [1912 미로 탐색](gold/1912_MazeSearch.py) |
| 23 | [multi-source BFS](#note-23-multi-source-bfs) | [2613 토마토(고)](gold/2613_Tomato.py) |
| 24 | [불/사람 동시 이동 BFS](#note-24-fire-escape-bfs) | [1082 화염에서탈출](gold/1082_EscapeFromFire.py) |
| 25 | [바깥 공기 BFS](#note-25-outside-air-bfs) | [1840 치즈](gold/1840_Cheese.py) |
| 26 | [DP 문제 접근법](#note-26-dp-approach) | [1411 두 줄로 타일 깔기](silver/1411_TilingTwoRows.py), [1520 계단 오르기](silver/1520_ClimbingStairs.py), [2000 동전교환](silver/2000_CoinChange.py) |
| 27 | [타일링 DP](#note-27-tiling-dp) | [1411 두 줄로 타일 깔기](silver/1411_TilingTwoRows.py) |
| 28 | [계단 DP](#note-28-stair-dp) | [1520 계단 오르기](silver/1520_ClimbingStairs.py) |
| 29 | [동전교환 DP](#note-29-coin-change-dp) | [2000 동전교환](silver/2000_CoinChange.py) |
| 26 | [백트래킹에서 마지막 부분만 검사하기](#note-26-backtracking-suffix-check) | [1027 좋은수열](gold/1027_GoodSequence.py) |
| 28 | [완전 배낭과 순회 방향](#note-28-unbounded-knapsack-order) | [1077 배낭채우기1](silver/1077_FillKnapsack1.py) |
| 29 | [LIS와 최소 이동 횟수](#note-29-lis-minimum-moves) | [1871 줄세우기](gold/1871_LineUp.py) |

### 문제별 메모

| 문제 | 배운 내용 |
| --- | --- |
| [3337 쇼핑몰](#problem-3337-shopping-mall) | heapq 튜플 비교, 정렬 기준, enumerate, `_` |
| [1357 합이 0이 되는 4개의 숫자들](#problem-1357-four-numbers-sum-zero) | meet in the middle, Counter, defaultdict, bisect |
| [2587 달리기](#problem-2587-running) | 좌표 압축, Fenwick Tree, Segment Tree와의 차이 |
| [1681 해밀턴 순환회로](#problem-1681-hamiltonian-cycle) | DFS 백트래킹, 순환회로, `nonlocal` |
| [1545 해밀턴 순환회로 2](#problem-1545-hamiltonian-cycle-2) | 비트마스크 DP, 방문 상태 표현, TSP |
| [1809 탑](#problem-1809-tower) | 단조 스택, 가까운 큰 값 찾기 |
| [1370 회의실 배정](#problem-1370-meeting-room-assignment) | 종료 시간 기준 그리디, 선택 조건 |
| [2581 예산](#problem-2581-budget) | 이분 탐색, 매개변수 탐색, 가능/불가능 판단 |
| [2300 용액](#problem-2300-solution) | 정렬, 투 포인터, 합의 부호에 따른 이동 |
| [3706 합이 0이 되는 연속구간 세기](#problem-3706-count-zero-sum-subarrays) | 누적합, Counter, 같은 누적합 쌍 |
| [1912 미로 탐색](#problem-1912-maze-search) | 반복 DFS, stack, 인접 리스트 정렬 |
| [2613 토마토(고)](#problem-2613-tomato) | multi-source BFS, 날짜 기록, 불가능 판단 |
| [1082 화염에서탈출](#problem-1082-escape-from-fire) | 불 BFS, 사람 BFS, 동시 도착 금지 |
| [1840 치즈](#problem-1840-cheese) | 바깥 공기 BFS, 시뮬레이션, 마지막 치즈 수 |
| [1411 두 줄로 타일 깔기](#problem-1411-tiling-two-rows) | DP 점화식, MOD 처리, 공간 최적화 |
| [1520 계단 오르기](#problem-1520-climbing-stairs) | 마지막 계단 기준 DP, 연속 세 계단 제한 |
| [2000 동전교환](#problem-2000-coin-change) | 최소 동전 수 DP, unbounded knapsack |
| [1027 좋은수열](#problem-1027-good-sequence) | 백트래킹, 접미부 비교, 사전순 탐색 |
| [1077 배낭채우기1](#problem-1077-fill-knapsack-1) | 완전 배낭, 1차원 DP, 정방향 용량 순회 |
| [1871 줄세우기](#problem-1871-line-up) | LIS, 최소 이동 횟수, `N - LIS 길이` |

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

하지만 없는 key를 조회할 때 차이가 큽니다.

```python
from collections import Counter, defaultdict

c = Counter()
d = defaultdict(int)

print(c[100])  # 0, key 추가 안 됨
print(d[100])  # 0, key 추가됨
```

`defaultdict(int)`를 쓰면서 없는 key를 만들고 싶지 않다면 `.get()`을 씁니다.

```python
answer += d.get(target, 0)
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

일반 탐색은 `O(N)`이지만, 이분 탐색은 범위를 절반씩 줄이므로 `O(log N)`입니다.

## note-08-python-limits

### Python 시간/메모리 판단

큰 입력에서는 알고리즘의 시간복잡도뿐 아니라 Python 자료구조의 메모리 사용량도 봐야 합니다.

1357에서 비교한 방식:

| 방식 | 특징 |
| --- | --- |
| Counter/hash | 평균 `O(1)` 조회라 빠르지만 서로 다른 합이 많으면 메모리를 많이 쓴다 |
| defaultdict(int) + `[]` 조회 | 없는 key를 새로 만들어 메모리 초과가 날 수 있다 |
| defaultdict(int) + `.get()` 조회 | 없는 key를 만들지 않는다 |
| 리스트 + bisect | 메모리는 예측하기 쉽지만 호출이 많으면 시간 초과가 날 수 있다 |

## note-09-coordinate-compression

### 좌표 압축

좌표 압축은 값의 실제 크기는 중요하지 않고, 값들의 순서만 중요할 때 큰 값을 작은 번호로 바꾸는 기법입니다.

예시:

```python
abilities = [100, 20, 50, 20]
```

중복 제거 후 정렬:

```python
sorted_values = [20, 50, 100]
```

작은 값부터 번호를 붙입니다.

```text
20  -> 1
50  -> 2
100 -> 3
```

코드:

```python
sorted_values = sorted(set(abilities))
compressed = {
    value: index
    for index, value in enumerate(sorted_values, start=1)
}
```

2587 달리기에서는 실력 값이 클 수 있으므로, Fenwick Tree의 인덱스로 쓰기 위해 좌표 압축을 합니다.

## note-10-fenwick-tree

### Fenwick Tree

Fenwick Tree는 특정 위치에 값을 더하고, `1번부터 i번까지의 누적합`을 빠르게 구하는 자료구조입니다.

주요 연산:

```text
update(index, value): index 위치에 value 더하기
query(index): 1부터 index까지의 합 구하기
```

기본 코드:

```python
tree = [0] * (size + 1)

def update(index, value):
    while index <= size:
        tree[index] += value
        index += index & -index

def query(index):
    total = 0

    while index > 0:
        total += tree[index]
        index -= index & -index

    return total
```

`index & -index`는 Fenwick Tree에서 다음으로 이동할 구간 크기를 구하는 값입니다.

2587에서 쓰는 방식:

```python
total_runner_count = query(size)
not_better_count = query(rank)
better_count = total_runner_count - not_better_count
```

의미:

```text
query(size): 앞에 나온 전체 선수 수
query(rank): 앞에 나온 선수 중 현재 선수보다 실력이 낮거나 같은 선수 수
차이: 앞에 나온 선수 중 현재 선수보다 실력이 좋은 선수 수
```

## note-11-segment-tree

### Segment Tree

Segment Tree는 배열의 구간 정보를 트리로 저장해서 구간 질의와 값 갱신을 빠르게 처리하는 자료구조입니다.

할 수 있는 일:

```text
구간 합
구간 최솟값
구간 최댓값
구간 gcd
구간 xor
```

기본 성능:

```text
값 갱신: O(log N)
구간 질의: O(log N)
공간: O(N)
```

Fenwick Tree보다 구현은 길지만, 더 다양한 구간 질의를 처리할 수 있습니다.

예를 들어 구간 최솟값이나 최댓값을 자주 물어보는 문제라면 Fenwick Tree보다 Segment Tree가 더 적합합니다.

## note-12-fenwick-vs-segment

### Fenwick Tree와 Segment Tree 차이

| 비교 | Fenwick Tree | Segment Tree |
| --- | --- | --- |
| 주요 목적 | prefix sum, 빈도수 누적 | 다양한 구간 질의 |
| 구간 합 | 가능 | 가능 |
| 구간 최솟값/최댓값 | 일반적으로 부적합 | 적합 |
| 구현 난이도 | 비교적 짧고 쉬움 | 더 길고 복잡함 |
| 메모리 | 작음 | 보통 더 큼 |
| 확장성 | 제한적 | Lazy Propagation 등으로 확장 가능 |

2587에서 Fenwick Tree를 쓴 이유:

```text
필요한 연산이 "특정 실력 등장 + prefix sum"뿐이기 때문이다.
```

현재 선수보다 실력이 좋은 앞선 선수 수는 이렇게 구합니다.

```python
better_count = query(max_rank) - query(rank)
```

즉, 복잡한 구간 최솟값/최댓값이 필요하지 않으므로 Segment Tree보다 Fenwick Tree가 간단하고 충분합니다.

## note-13-dfs-backtracking

### DFS 백트래킹

DFS 백트래킹은 가능한 선택을 하나씩 해 보면서, 조건에 맞지 않거나 더 볼 필요가 없는 경우 되돌아가는 방식입니다.

1681에서는 방문 순서를 하나씩 만든다고 생각하면 됩니다.

```text
1번에서 시작
아직 방문하지 않은 정점으로 이동
모든 정점을 방문하면 다시 1번으로 돌아갈 수 있는지 확인
```

백트래킹의 핵심은 방문 처리와 되돌리기입니다.

```python
visited[next_node] = True
dfs(next_node, count + 1, total_cost + cost[current][next_node])
visited[next_node] = False
```

`visited[next_node] = False`를 하지 않으면 다음 경우의 수에서 그 정점을 다시 사용할 수 없으므로 탐색이 망가집니다.

가지치기도 중요합니다.

```python
if total_cost >= answer:
    return
```

이미 지금 비용이 지금까지 찾은 최소 비용 이상이라면, 뒤에 어떤 경로를 더 붙여도 최소 답이 될 수 없습니다.

## note-14-hamiltonian-cycle

### 해밀턴 순환회로

해밀턴 순환회로는 모든 정점을 정확히 한 번씩 방문한 뒤 시작 정점으로 돌아오는 경로입니다.

1681에서 순환회로라고 판단하는 기준:

```text
1. 1번 정점에서 시작한다.
2. 모든 정점을 한 번씩 방문한다.
3. 마지막 정점에서 다시 1번 정점으로 돌아온다.
```

그래서 DFS 종료 조건은 단순히 모든 정점을 방문했는지가 아니라, 시작점으로 돌아갈 수 있는지도 같이 봐야 합니다.

```python
if count == N:
    if cost[current][0] != 0:
        answer = min(answer, total_cost + cost[current][0])
    return
```

여기서 `cost[current][0] != 0`은 현재 정점에서 시작점으로 돌아가는 길이 있다는 뜻입니다.

## note-15-nonlocal

### nonlocal

`nonlocal`은 안쪽 함수에서 바깥 함수의 지역 변수를 수정할 때 사용합니다.

1681 코드에서는 `solution()` 안에 `answer`가 있고, 그 안쪽 함수인 `dfs()`에서 `answer`를 갱신합니다.

```python
def solution(N, cost):
    answer = 10**18

    def dfs(current, count, total_cost):
        nonlocal answer
        answer = min(answer, total_cost)
```

`nonlocal answer`가 없으면 Python은 `dfs()` 안의 `answer`를 새로운 지역 변수로 보려고 해서 오류가 납니다.

`global`과의 차이:

| 키워드 | 의미 |
| --- | --- |
| `nonlocal` | 바로 바깥 함수 쪽 변수를 사용 |
| `global` | 파일 전체 범위의 전역 변수를 사용 |

이 문제처럼 `solution()` 안에서만 쓰는 답 변수는 `global`보다 `nonlocal`이 더 깔끔합니다.

## note-16-bitmask-dp

### 비트마스크 DP

비트마스크 DP는 여러 개의 선택 여부를 정수 하나의 비트로 저장하고, 그 상태를 DP 인덱스로 사용하는 방식입니다.

1545에서는 장소 방문 여부를 `mask`로 표현합니다.

```text
0001 = 0번 장소만 방문
0011 = 0번, 1번 장소 방문
0101 = 0번, 2번 장소 방문
1111 = 모든 장소 방문
```

DP 상태는 이렇게 잡습니다.

```python
dp[mask][current]
```

의미:

```text
mask에 포함된 장소들을 방문했고,
현재 current 장소에 있을 때의 최소 비용
```

방문 여부 확인:

```python
if mask & (1 << next_node):
    continue
```

`1 << next_node`는 `next_node`번 장소만 켜진 비트입니다. `mask`와 AND 했을 때 0이 아니면 이미 방문한 장소입니다.

방문 추가:

```python
next_mask = mask | (1 << next_node)
```

`|` 연산은 기존 방문 상태에 `next_node` 방문 표시를 추가합니다.

DP 갱신:

```python
next_cost = dp[mask][current] + cost[current][next_node]

if next_cost < dp[next_mask][next_node]:
    dp[next_mask][next_node] = next_cost
```

뜻:

```text
현재 상태에서 next_node로 이동했을 때,
더 싼 비용으로 도착할 수 있으면 최소 비용을 갱신한다.
```

해밀턴 순환회로 2에서는 DFS 백트래킹이 `O(N!)`이라 어렵고, 비트마스크 DP로 `O(N^2 * 2^N)`까지 줄입니다.

## note-17-monotone-stack

### 단조 스택

단조 스택은 stack 안의 값이 일정한 방향으로 정렬된 상태를 유지하는 기법입니다.

1809 탑에서는 stack에 높이가 큰 탑들이 남도록 관리합니다.

```python
while stack and stack[-1][1] < height:
    stack.pop()
```

의미:

```text
stack top 탑이 현재 탑보다 낮으면
현재 탑의 신호를 받을 수 없으므로 제거한다.
```

낮은 탑을 제거한 뒤 stack top이 남아 있다면, 그 탑이 현재 탑의 신호를 받을 수 있는 가장 가까운 탑입니다.

```python
if stack:
    answer.append(stack[-1][0])
else:
    answer.append(0)
```

현재 탑도 이후 오른쪽 탑들의 후보가 될 수 있으므로 stack에 넣습니다.

```python
stack.append((tower_number, height))
```

각 탑은 stack에 한 번 들어가고 최대 한 번 나오므로 전체 시간복잡도는 `O(N)`입니다.

## note-18-meeting-room-greedy

### 회의실 배정 그리디

회의실 배정 문제는 한 회의실에서 겹치지 않게 최대한 많은 회의를 고르는 문제입니다.

가장 중요한 선택 기준은 종료 시간입니다.

```python
meetings.sort(key=lambda x: (x[2], x[1]))
```

의미:

```text
1. 종료 시간이 빠른 회의 먼저
2. 종료 시간이 같으면 시작 시간이 빠른 회의 먼저
```

종료 시간이 빠른 회의를 먼저 선택하면 뒤에 남는 시간이 많아져서 더 많은 회의를 넣을 가능성이 커집니다.

선택 조건:

```python
if start_time >= last_end_time:
    selected.append(meeting_number)
    last_end_time = end_time
```

`>=`를 쓰는 이유는 회의가 끝나는 시간과 다음 회의가 시작하는 시간이 같으면 겹치지 않기 때문입니다.

1370은 선택한 회의 번호도 출력해야 하므로, 회의 정보를 `(회의 번호, 시작 시간, 종료 시간)`으로 저장합니다.

## note-19-parametric-search

### 매개변수 탐색

매개변수 탐색은 정답 후보 `x`를 정했을 때 가능한지 판단하고, 가능한 값 중 최댓값이나 최솟값을 이분 탐색으로 찾는 방식입니다.

2581 예산에서는 정답 후보가 상한액 `cap`입니다.

```python
used_budget = 0
for request in requests:
    used_budget += min(request, cap)
```

`cap`이 작으면 총 배정액도 작아서 가능하고, `cap`이 커지면 총 배정액도 커져서 언젠가 불가능해집니다.

```text
가능 가능 가능 가능 불가능 불가능 불가능
```

2581은 가능한 `cap` 중 가장 큰 값을 찾아야 합니다.

```python
if used_budget <= total_budget:
    answer = cap
    left = cap + 1
else:
    right = cap - 1
```

의미:

```text
가능하면 현재 cap을 저장하고 더 큰 값을 탐색한다.
불가능하면 cap이 너무 큰 것이므로 더 작은 값을 탐색한다.
```

매개변수 탐색을 의심할 수 있는 표현:

```text
가능한 최댓값
필요한 최솟값
최대값을 최소화
최소값을 최대화
상한액
정해진 조건 안에서 가장 큰 값
```

## note-20-two-pointer

### 투 포인터

투 포인터는 정렬된 배열이나 연속 구간에서 두 인덱스를 움직이며 답을 찾는 기법입니다.

2300 용액에서는 정렬된 배열의 양끝에서 시작합니다.

```python
left = 0
right = N - 1
```

현재 합을 확인합니다.

```python
current_sum = values[left] + values[right]
```

합이 0에 더 가까워지면 정답 후보를 갱신합니다.

```python
if abs(current_sum) < best_sum:
    best_sum = abs(current_sum)
    answer = [values[left], values[right]]
```

포인터 이동 기준은 합의 부호입니다.

```python
if current_sum < 0:
    left += 1
else:
    right -= 1
```

의미:

```text
합이 음수이면 더 큰 값이 필요하므로 left를 오른쪽으로 옮긴다.
합이 양수이면 더 작은 값이 필요하므로 right를 왼쪽으로 옮긴다.
```

정렬 후 한 번만 훑으므로 투 포인터 부분은 `O(N)`입니다.

## note-21-prefix-sum-hash

### 누적합과 해시

연속 구간 합은 누적합의 차이로 표현할 수 있습니다.

```text
구간 합 i+1 ~ j = prefix[j] - prefix[i]
```

구간 합이 0이 되려면 두 누적합이 같아야 합니다.

```text
prefix[j] - prefix[i] = 0
prefix[j] = prefix[i]
```

그래서 현재 누적합이 이전에 몇 번 나왔는지 세면, 현재 위치에서 끝나는 합 0 구간의 개수를 알 수 있습니다.

```python
answer += prefix_count[prefix_sum]
prefix_count[prefix_sum] += 1
```

초기값도 중요합니다.

```python
prefix_count[0] = 1
```

시작 전 누적합 0을 한 번 기록해두면, 처음부터 현재 위치까지의 합이 0인 구간도 셀 수 있습니다.

예시:

```text
numbers = [1, -1, 2, -2]
누적합: 시작 전 0, 1, 0, 2, 0
```

마지막 누적합 0을 볼 때 이전에 0이 두 번 있었으므로, 현재 위치에서 끝나는 합 0 구간이 두 개 생깁니다.

## note-22-iterative-dfs-stack

### 반복 DFS와 stack

재귀 DFS는 코드가 짧지만, 깊이가 큰 그래프에서는 재귀 제한 때문에 위험할 수 있습니다.

```python
def dfs(node):
    visited[node] = True
    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node)
```

1912처럼 `N`이 최대 100000이면 한 방향으로 길게 이어진 그래프에서 재귀 깊이가 커질 수 있습니다.

이럴 때는 `stack`으로 DFS를 직접 구현합니다.

```python
stack = [1]
visited[1] = True

while stack:
    current = stack[-1]
```

`stack[-1]`은 현재 위치입니다. 더 갈 수 있는 방이 있으면 그 방을 `append()`하고, 더 갈 방이 없으면 `pop()`해서 이전 방으로 돌아갑니다.

1912에서는 각 방의 인접 방을 번호가 작은 순서대로 봐야 하므로 정렬이 필요합니다.

```python
for room in range(1, N + 1):
    graph[room].sort()
```

또한 되돌아온 뒤 같은 인접 방들을 처음부터 다시 검사하면 느려질 수 있으므로, 방마다 다음에 볼 위치를 저장합니다.

```python
next_index = [0] * (N + 1)
```

의미:

```text
next_index[room] = graph[room]에서 다음에 확인할 인덱스
```

이 패턴은 "재귀 DFS는 깊이 때문에 위험하지만, DFS 순서는 유지해야 하는 문제"에서 유용합니다.

## note-23-multi-source-bfs

### multi-source BFS

multi-source BFS는 시작점이 여러 개인 BFS입니다.

일반 BFS는 시작점 하나를 큐에 넣고 시작합니다.

```python
queue.append(start)
```

하지만 2613 토마토처럼 처음부터 익은 토마토가 여러 개라면, 모든 익은 토마토를 동시에 시작점으로 넣어야 합니다.

```python
for row in range(N):
    for col in range(M):
        if box[row][col] == 1:
            queue.append((row, col))
```

이렇게 하면 여러 위치에서 동시에 퍼지는 상황을 자연스럽게 처리할 수 있습니다.

2613에서는 칸의 값을 날짜처럼 사용합니다.

```python
box[next_row][next_col] = box[row][col] + 1
days = box[next_row][next_col] - 1
```

의미:

```text
1 = 처음부터 익은 토마토, 0일
2 = 1일 뒤 익은 토마토
3 = 2일 뒤 익은 토마토
```

불가능 여부는 익지 않은 토마토 개수를 세면 편합니다.

```python
unripe_count -= 1
```

BFS가 끝난 뒤 `unripe_count`가 남아 있으면, 빈 칸이나 벽 때문에 끝까지 익지 못하는 토마토가 있다는 뜻입니다.

## note-24-fire-escape-bfs

### 불/사람 동시 이동 BFS

불과 사람이 동시에 움직이는 문제에서는 사람을 먼저 움직이면 위험한 칸을 잘못 밟을 수 있습니다.

그래서 보통 두 단계로 나눕니다.

```text
1. 불이 각 칸에 언제 도착하는지 먼저 BFS로 계산한다.
2. 사람이 이동할 때 불보다 먼저 도착할 수 있는 칸만 이동한다.
```

불 도착 시간 배열은 이렇게 둡니다.

```python
INF = 10**9
fire_time = [[INF] * C for _ in range(R)]
```

`INF`는 아직 불이 도착하지 않았다는 뜻입니다.

불 BFS에서 이미 시간이 기록된 칸은 다시 볼 필요가 없습니다.

```python
if fire_time[next_row][next_col] != INF:
    continue
```

BFS는 가까운 시간부터 퍼지기 때문에 처음 기록된 시간이 가장 빠른 도착 시간입니다.

사람 BFS에서는 다음 칸에 도착하는 시간을 먼저 구합니다.

```python
next_time = person_time[row][col] + 1
```

그리고 불이 같은 시간 또는 더 먼저 도착하는 칸은 이동하지 않습니다.

```python
if fire_time[next_row][next_col] <= next_time:
    continue
```

의미:

```text
불 도착 시간 <= 사람 도착 시간
=> 사람이 도착했을 때 이미 불이 있거나 동시에 불이 붙는 칸
=> 이동 불가
```

이 패턴은 "불", "물", "독가스"처럼 위험 요소가 퍼지고, 사람이 그 위험을 피해 이동하는 문제에서 자주 나옵니다.

## note-25-outside-air-bfs

### 바깥 공기 BFS

격자에서 `0`이 모두 같은 의미가 아닐 때가 있습니다.

1840 치즈에서는 `0`이 두 종류입니다.

```text
1. 바깥 공기와 연결된 0
2. 치즈 내부 구멍에 있는 0
```

치즈는 바깥 공기와 닿아야 녹습니다. 그래서 내부 구멍의 `0`은 아직 공기처럼 처리하면 안 됩니다.

이럴 때는 가장자리의 빈 칸에서 BFS를 시작합니다.

```python
queue.append((0, 0))
visited[0][0] = True
```

문제에서 판의 가장자리에는 치즈가 없다고 했으므로 `(0, 0)`은 항상 바깥 공기입니다.

BFS 중 치즈를 만나면 큐에 넣지 않고 녹일 목록에 저장합니다.

```python
if board[next_row][next_col] == 1:
    melt.append((next_row, next_col))
else:
    queue.append((next_row, next_col))
```

치즈를 바로 `0`으로 바꾸지 않는 이유가 중요합니다.

```text
같은 시간에 녹는 치즈를 바로 0으로 만들면,
그 시간 안에 안쪽 치즈까지 공기가 들어간 것처럼 탐색될 수 있다.
```

그래서 이번 시간에 녹을 치즈를 `melt`에 모아두었다가 BFS가 끝난 뒤 한꺼번에 녹입니다.

```python
for row, col in melt:
    board[row][col] = 0
```

시간복잡도에서 `T`는 전체 치즈가 녹는 데 걸리는 시간입니다.

```text
시간복잡도: O(T * N * M)
```

`N, M <= 100`이고 한 시간마다 바깥쪽 치즈가 한 겹씩 녹으므로 `T`는 보통 최대 약 `min(N, M) / 2` 수준입니다.

## note-26-dp-approach

### DP 문제 접근법

DP는 큰 문제의 답을 작은 문제의 답으로 만드는 방식입니다.

DP를 의심할 수 있는 표현:

```text
경우의 수
최댓값 / 최솟값
몇 가지 방법
완전탐색하면 너무 많다
앞의 결과가 뒤에 영향을 준다
같은 계산이 반복된다
```

풀이 순서:

```text
1. dp[i]의 의미를 문장으로 정확히 정한다.
2. 작은 값 N=1, 2, 3 정도를 직접 구해본다.
3. 마지막 선택을 기준으로 경우를 나눈다.
4. 이전 상태를 이용해 점화식을 만든다.
5. 초기값을 정한다.
6. 작은 값부터 큰 값으로 계산한다.
7. 문제 조건에 따라 MOD, 최댓값, 최솟값, 불가능 처리를 한다.
```

가장 중요한 것은 `dp[i]`의 의미입니다.

```python
dp[i] = ?
```

이 정의가 선명해야 점화식도 선명해집니다.

## note-27-tiling-dp

### 타일링 DP

타일링 문제는 보통 마지막 부분을 어떻게 채우는지 기준으로 점화식을 세웁니다.

1411에서는 이렇게 정의합니다.

```python
dp[n] = 2 * n 판을 채우는 방법의 수
```

마지막을 채우는 방법:

```text
마지막 1칸을 세로 타일로 채우기: dp[n - 1]
마지막 2칸을 새로운 2가지 방식으로 채우기: 2 * dp[n - 2]
```

그래서 점화식은:

```python
dp[n] = dp[n - 1] + 2 * dp[n - 2]
```

문제에서 나머지를 출력하라고 하면 매 단계에서 MOD를 적용합니다.

```python
current = (previous_one + 2 * previous_two) % MOD
```

매번 MOD를 해도 되는 이유:

```text
(a + b) % MOD = ((a % MOD) + (b % MOD)) % MOD
```

## note-28-stair-dp

### 계단 DP

계단 오르기 문제는 보통 마지막 계단을 밟는 방법을 기준으로 생각합니다.

1520에서는 마지막 계단을 반드시 밟아야 하고, 연속 세 계단을 밟을 수 없습니다.

DP 정의:

```python
dp[i] = i번째 계단을 반드시 밟았을 때 얻을 수 있는 최대 점수
```

`i`번째 계단을 밟는 경우:

```text
1. i-2번째에서 두 칸 올라온다.
2. i-3번째에서 i-1번째를 거쳐 i번째로 온다.
```

점화식:

```python
dp[i] = max(
    dp[i - 2] + score[i],
    dp[i - 3] + score[i - 1] + score[i],
)
```

두 번째 경우에서 `i-2`를 건너뛰기 때문에 `i-2, i-1, i`를 모두 밟는 연속 세 계단이 생기지 않습니다.

## note-29-coin-change-dp

### 동전교환 DP

동전교환에서 최소 동전 수를 구할 때는 금액을 DP 상태로 잡습니다.

```python
dp[money] = money원을 만드는 데 필요한 최소 동전 개수
```

초기값:

```python
INF = 10**9
dp = [INF] * (W + 1)
dp[0] = 0
```

`dp[0] = 0`은 0원을 만드는 데 동전이 0개 필요하다는 뜻입니다.

점화식:

```python
dp[money] = min(dp[money], dp[money - coin] + 1)
```

의미:

```text
money - coin원을 만든 뒤 coin 동전 하나를 추가하면 money원을 만들 수 있다.
```

모든 동전을 무제한 사용할 수 있으므로, 같은 동전을 여러 번 쓰는 갱신이 가능합니다.

만들 수 없는 금액은 끝까지 `INF`로 남습니다.

## note-26-backtracking-suffix-check

### 백트래킹에서 마지막 부분만 검사하기

백트래킹으로 조건을 만족하는 수열을 한 글자씩 만들 때, 새 글자를 붙이기 전의 수열은 이미 조건을 만족한다.
따라서 새로 조건을 위반할 수 있는 부분에는 반드시 방금 붙인 마지막 글자가 포함된다.

1027 좋은수열에서는 수열 전체의 모든 구간을 다시 검사하지 않고, 맨 뒤에 붙어 있는 같은 길이의 두 덩어리만 비교한다.

```text
sequence = [기존 부분 | 왼쪽 덩어리 | 오른쪽 덩어리]
                         size개          size개
```

두 덩어리의 범위는 다음과 같다.

```python
left_part = sequence[length - 2 * size : length - size]
right_part = sequence[length - size :]
```

예를 들어 `sequence = 1212`, `length = 4`, `size = 2`이면 다음처럼 비교된다.

```python
left_part = sequence[0:2]  # 12
right_part = sequence[2:]  # 12
```

두 부분이 같으므로 `1212`는 나쁜 수열이다.

`size`를 `length // 2`까지만 검사하는 이유는 길이 `size`인 덩어리 두 개를 만들려면 원소가 최소 `2 * size`개 필요하기 때문이다.

```python
for size in range(1, length // 2 + 1):
    if left_part == right_part:
        return False
```

또한 답이 가장 작은 수열이어야 할 때 후보를 `1`, `2`, `3` 순서로 탐색하면 DFS에서 처음 완성된 답이 곧 최솟값이다. 이처럼 탐색 순서를 정답의 정렬 순서와 맞추면 모든 정답을 저장해서 비교할 필요가 없다.

## note-28-unbounded-knapsack-order

### 완전 배낭과 순회 방향

완전 배낭은 각 물건을 원하는 만큼 반복해서 사용할 수 있는 배낭 문제이다.

1077 배낭채우기1에서는 다음과 같이 DP를 정의한다.

```python
dp[capacity] = capacity 이하에서 얻을 수 있는 최대 값어치
```

무게가 `weight`, 값어치가 `value`인 보석을 현재 용량에 하나 추가하는 점화식은 다음과 같다.

```python
dp[current_weight] = max(
    dp[current_weight],
    dp[current_weight - weight] + value,
)
```

첫 번째 값은 현재 보석을 담지 않는 경우이고, 두 번째 값은 현재 보석을 하나 더 담는 경우이다.

완전 배낭에서는 용량을 작은 값부터 큰 값으로 순회한다.

```python
for current_weight in range(weight, W + 1):
```

예를 들어 무게 2, 값어치 40인 보석을 처리하면 다음과 같이 현재 보석으로 갱신한 값을 다시 사용한다.

```text
dp[2] = dp[0] + 40 = 40
dp[4] = dp[2] + 40 = 80
dp[6] = dp[4] + 40 = 120
```

순회 방향에 따른 차이는 다음과 같다.

| 문제 종류 | 용량 순회 | 의미 |
| --- | --- | --- |
| 완전 배낭 | 작은 값 → 큰 값 | 갱신된 값을 재사용하여 같은 물건을 여러 번 사용 |
| 0/1 배낭 | 큰 값 → 작은 값 | 같은 반복의 갱신 값을 사용하지 않아 물건을 한 번만 사용 |

## note-29-lis-minimum-moves

### LIS와 최소 이동 횟수

수열을 오름차순으로 만들기 위해 옮겨야 하는 원소의 최소 개수를 묻는다면, 옮길 원소를 직접 선택하기보다 현재 위치를 유지할 원소를 최대한 많이 찾는 관점으로 바꿀 수 있다.

현재 위치를 유지하는 원소들은 원래 수열에서도 오름차순이어야 한다. 따라서 유지할 수 있는 최대 원소 수는 LIS, 즉 최장 증가 부분 수열의 길이이다.

```text
최소 이동 개수 = 전체 원소 수 - LIS 길이
```

1871 줄세우기의 예시는 다음과 같다.

```text
현재 줄: 3 7 5 2 6 1 4
유지 가능: 3 5 6
```

`3, 5, 6`은 현재 순서를 유지하면서 오름차순을 이루므로 움직이지 않아도 된다. 나머지 네 명을 옮기면 전체 줄을 번호순으로 만들 수 있다.

`O(N²)` DP에서는 다음과 같이 상태를 정의한다.

```python
dp[i] = i번째 원소를 마지막으로 하는 LIS의 최대 길이
```

모든 원소는 혼자서 길이 1의 증가 수열을 만들 수 있다.

```python
dp = [1] * N
```

앞의 원소가 현재 원소보다 작으면 앞의 증가 수열 뒤에 현재 원소를 붙일 수 있다.

```python
for i in range(N):
    for j in range(i):
        if children[j] < children[i]:
            dp[i] = max(dp[i], dp[j] + 1)
```

여기서 `dp[j] + 1`은 `j`번째 원소까지의 증가 수열 뒤에 `i`번째 원소 하나를 추가한다는 뜻이다.

```text
아이: 3 7 5 2 6 1 4
dp:   1 2 2 1 3 1 2
```

가장 큰 값은 3이므로 LIS 길이는 3이고, 옮겨야 하는 최소 인원은 `7 - 3 = 4`이다.

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

문제 파일: [1357_FourNumbersSumZero.py](platinum/1357_FourNumbersSumZero.py)

배운 내용:

| 주제 | 이유 |
| --- | --- |
| [meet in the middle](#note-05-meet-in-the-middle) | 4중 반복을 `A+B`, `C+D` 두 묶음으로 줄이기 위해 사용 |
| [Counter와 defaultdict 차이](#note-06-counter-defaultdict) | `defaultdict`가 없는 key를 추가해 메모리 초과를 만들 수 있음을 확인 |
| [bisect와 이분 탐색](#note-07-bisect-binary-search) | 정렬 리스트 기반 대안 풀이와 시간 차이를 이해하기 위해 정리 |
| [Python 시간/메모리 판단](#note-08-python-limits) | 해시, 입력 최적화, 자료구조 선택의 차이를 비교하기 위해 정리 |

## problem-2587-running

### 2587 달리기

문제 파일: [2587_Running.py](platinum/2587_Running.py)

배운 내용:

| 주제 | 이유 |
| --- | --- |
| [좌표 압축](#note-09-coordinate-compression) | 큰 실력 값을 Fenwick Tree 인덱스로 쓰기 위해 작은 번호로 바꿈 |
| [Fenwick Tree](#note-10-fenwick-tree) | 앞선 선수들의 실력 개수를 저장하고 prefix sum으로 등수를 계산 |
| [Segment Tree](#note-11-segment-tree) | 같은 문제를 풀 수 있는 더 범용적인 구간 자료구조로 비교 |
| [Fenwick Tree와 Segment Tree 차이](#note-12-fenwick-vs-segment) | 2587에서는 prefix sum만 필요하므로 Fenwick Tree가 더 간단함 |

## problem-1681-hamiltonian-cycle

### 1681 해밀턴 순환회로

문제 파일: [1681_HamiltonianCycle.py](silver/1681_HamiltonianCycle.py)

배운 내용:

| 주제 | 이유 |
| --- | --- |
| [DFS 백트래킹](#note-13-dfs-backtracking) | 가능한 방문 순서를 하나씩 만들고, 방문 처리를 되돌리며 모든 경우를 탐색 |
| [해밀턴 순환회로](#note-14-hamiltonian-cycle) | 모든 정점을 한 번씩 방문한 뒤 시작점으로 돌아와야 한다는 조건을 이해 |
| [nonlocal](#note-15-nonlocal) | `dfs()` 안에서 `solution()`의 `answer`를 갱신하기 위해 사용 |

## problem-1545-hamiltonian-cycle-2

### 1545 해밀턴 순환회로 2

문제 파일: [1545_HamiltonianCycle2.py](platinum/1545_HamiltonianCycle2.py)

배운 내용:

| 주제 | 이유 |
| --- | --- |
| [비트마스크 DP](#note-16-bitmask-dp) | `N <= 19`에서 모든 순서를 직접 보는 DFS 대신 방문 상태를 재사용하기 위해 사용 |
| [해밀턴 순환회로](#note-14-hamiltonian-cycle) | 모든 장소를 한 번씩 방문한 뒤 회사로 돌아와야 한다는 조건을 처리 |
| Python 제출 환경 | 반복문이 많은 비트마스크 DP라 PyPy3 제출이 더 유리함 |

## problem-1809-tower

### 1809 탑

문제 파일: [1809_Tower.py](gold/1809_Tower.py)

배운 내용:

| 주제 | 이유 |
| --- | --- |
| [단조 스택](#note-17-monotone-stack) | 현재 탑보다 낮은 왼쪽 탑을 제거하고 가까운 수신 탑을 빠르게 찾기 위해 사용 |
| stack에 인덱스와 높이 함께 저장 | 출력에는 탑 번호가 필요하고, 비교에는 높이가 필요하기 때문 |
| `while stack and stack[-1][1] < height` | 현재 탑보다 낮은 탑은 현재 탑의 신호를 받을 수 없으므로 제거 |

## problem-1370-meeting-room-assignment

### 1370 회의실 배정

문제 파일: [1370_MeetingRoomAssignment.py](silver/1370_MeetingRoomAssignment.py)

배운 내용:

| 주제 | 이유 |
| --- | --- |
| [회의실 배정 그리디](#note-18-meeting-room-greedy) | 종료 시간이 빠른 회의부터 선택하면 최대 개수를 만들 수 있기 때문 |
| `(종료 시간, 시작 시간)` 정렬 | greedy 선택 순서를 만들기 위해 사용 |
| `start_time >= last_end_time` | 종료 시간과 시작 시간이 같은 경우는 겹치지 않는다는 조건 처리 |

## problem-2581-budget

### 2581 예산

문제 파일: [2581_Budget.py](silver/2581_Budget.py)

배운 내용:

| 주제 | 이유 |
| --- | --- |
| [매개변수 탐색](#note-19-parametric-search) | 상한액 `cap`이 가능한지 판단하면서 가능한 최댓값을 찾기 위해 사용 |
| `sum(min(request, cap))` | 상한액을 적용했을 때 실제 배정되는 총 예산을 계산 |
| `used_budget <= total_budget` | 현재 상한액이 가능한지 판단하는 기준 |

## problem-2300-solution

### 2300 용액

문제 파일: [2300_Solution.py](gold/2300_Solution.py)

배운 내용:

| 주제 | 이유 |
| --- | --- |
| [투 포인터](#note-20-two-pointer) | 정렬된 배열의 양끝에서 합이 0에 가까운 두 값을 빠르게 찾기 위해 사용 |
| 합이 음수일 때 `left += 1` | 합을 키워 0에 가깝게 만들기 위해 사용 |
| 합이 양수일 때 `right -= 1` | 합을 줄여 0에 가깝게 만들기 위해 사용 |

## problem-3706-count-zero-sum-subarrays

### 3706 합이 0이 되는 연속구간 세기

문제 파일: [3706_CountZeroSumSubarrays.py](silver/3706_CountZeroSumSubarrays.py)

배운 내용:

| 주제 | 이유 |
| --- | --- |
| [누적합과 해시](#note-21-prefix-sum-hash) | 같은 누적합이 나온 두 지점 사이의 구간 합이 0이기 때문 |
| `prefix_count[0] = 1` | 시작 지점부터 합이 0인 구간을 세기 위해 필요 |
| `answer += prefix_count[prefix_sum]` | 현재 누적합과 같은 이전 누적합 개수만큼 합 0 구간이 생김 |

## problem-1912-maze-search

### 1912 미로 탐색

문제 파일: [1912_MazeSearch.py](gold/1912_MazeSearch.py)

배운 내용:

| 주제 | 이유 |
| --- | --- |
| [반복 DFS와 stack](#note-22-iterative-dfs-stack) | 재귀 깊이 제한 없이 DFS 탐색 순서를 구현하기 위해 사용 |
| 인접 리스트 정렬 | 방문하지 않은 인접 방 중 번호가 가장 작은 방을 먼저 가야 하기 때문 |
| `next_index` 배열 | 각 방에서 인접 방을 어디까지 확인했는지 저장해 불필요한 반복 탐색을 줄이기 위해 사용 |

## problem-2613-tomato

### 2613 토마토(고)

문제 파일: [2613_Tomato.py](gold/2613_Tomato.py)

배운 내용:

| 주제 | 이유 |
| --- | --- |
| [multi-source BFS](#note-23-multi-source-bfs) | 처음부터 익은 여러 토마토가 동시에 퍼지는 상황을 처리하기 위해 사용 |
| 칸 값으로 날짜 기록 | `box[row][col] + 1`로 다음 날 익은 토마토를 표시하기 위해 사용 |
| `unripe_count` | BFS 후 전체 배열을 다시 훑지 않고 익지 못한 토마토가 남았는지 판단하기 위해 사용 |

## problem-1082-escape-from-fire

### 1082 화염에서탈출

문제 파일: [1082_EscapeFromFire.py](gold/1082_EscapeFromFire.py)

배운 내용:

| 주제 | 이유 |
| --- | --- |
| [불/사람 동시 이동 BFS](#note-24-fire-escape-bfs) | 위험 요소가 퍼지는 시간을 먼저 계산하고 사람이 안전한 칸만 이동하기 위해 사용 |
| `fire_time` 배열 | 불이 각 칸에 가장 빨리 도착하는 시간을 저장하기 위해 사용 |
| `fire_time[next] <= next_time` | 불이 같거나 더 빠르게 도착하는 칸을 막기 위해 사용 |
| `INF` | 불이 도착하지 못한 칸과 아직 방문하지 않은 칸을 구분하기 위해 사용 |

## problem-1840-cheese

### 1840 치즈

문제 파일: [1840_Cheese.py](gold/1840_Cheese.py)

배운 내용:

| 주제 | 이유 |
| --- | --- |
| [바깥 공기 BFS](#note-25-outside-air-bfs) | 내부 구멍과 바깥 공기를 구분해 바깥 공기와 닿은 치즈만 녹이기 위해 사용 |
| `melt` 리스트 | 같은 시간에 녹을 치즈를 모아두었다가 한꺼번에 녹이기 위해 사용 |
| `last_cheese_count` | 모두 녹기 한 시간 전에 남아 있던 치즈 칸 수를 출력하기 위해 사용 |
| `O(TNM)` | `T`번의 시간 동안 매번 최대 `N*M`칸을 BFS로 확인하기 때문 |

## problem-1411-tiling-two-rows

### 1411 두 줄로 타일 깔기

문제 파일: [1411_TilingTwoRows.py](silver/1411_TilingTwoRows.py)

배운 내용:

| 주제 | 이유 |
| --- | --- |
| [DP 문제 접근법](#note-26-dp-approach) | 경우의 수 문제를 작은 판의 경우의 수로 나누기 위해 사용 |
| [타일링 DP](#note-27-tiling-dp) | 마지막 1칸/2칸을 기준으로 점화식을 만들기 위해 사용 |
| MOD 처리 | 경우의 수가 커지므로 매 단계에서 `20100529`로 나눈 나머지를 저장 |
| 공간 최적화 | `dp[n-1]`, `dp[n-2]`만 필요하므로 변수 2개로 계산 가능 |

## problem-1520-climbing-stairs

### 1520 계단 오르기

문제 파일: [1520_ClimbingStairs.py](silver/1520_ClimbingStairs.py)

배운 내용:

| 주제 | 이유 |
| --- | --- |
| [DP 문제 접근법](#note-26-dp-approach) | 마지막 계단을 밟는 이전 경우를 나누어 최댓값을 구하기 위해 사용 |
| [계단 DP](#note-28-stair-dp) | 연속 세 계단을 피하면서 마지막 계단을 반드시 밟기 위해 사용 |
| 작은 N 처리 | `N=1`, `N=2`는 점화식 전에 초기값으로 따로 처리 |

## problem-2000-coin-change

### 2000 동전교환

문제 파일: [2000_CoinChange.py](silver/2000_CoinChange.py)

배운 내용:

| 주제 | 이유 |
| --- | --- |
| [DP 문제 접근법](#note-26-dp-approach) | 금액별 최소 동전 개수를 작은 금액의 답으로 만들기 위해 사용 |
| [동전교환 DP](#note-29-coin-change-dp) | 마지막에 사용한 동전 하나를 기준으로 `dp[money]`를 갱신하기 위해 사용 |
| `INF` 초기화 | 만들 수 없는 금액을 구분하고 최솟값 갱신을 하기 위해 사용 |
| `"impossible"` 처리 | 목표 금액이 끝까지 `INF`이면 만들 수 없다는 뜻 |

## problem-1027-good-sequence

### 1027 좋은수열

문제 파일: [1027_GoodSequence.py](gold/1027_GoodSequence.py)

배운 내용:

| 주제 | 이유 |
| --- | --- |
| [백트래킹에서 마지막 부분만 검사하기](#note-26-backtracking-suffix-check) | 숫자를 하나 붙인 뒤 새롭게 생길 수 있는 나쁜 부분은 수열의 마지막에만 있기 때문 |
| `1 → 2 → 3` 순서의 DFS | 처음 완성된 좋은 수열이 숫자로 보았을 때 가장 작은 수열이 되도록 하기 위해 사용 |
| `sequence.append()`와 `sequence.pop()` | 후보 숫자를 선택하고, 실패하면 선택 전 상태로 되돌리기 위해 사용 |
| 성공 여부를 반환하는 DFS | 정답을 찾은 뒤 남은 탐색을 즉시 중단하기 위해 사용 |

## problem-1077-fill-knapsack-1

### 1077 배낭채우기1

문제 파일: [1077_FillKnapsack1.py](silver/1077_FillKnapsack1.py)

배운 내용:

| 주제 | 이유 |
| --- | --- |
| [완전 배낭과 순회 방향](#note-28-unbounded-knapsack-order) | 각 보석을 무제한 사용할 수 있으므로 현재 보석으로 갱신한 값을 다시 사용해야 함 |
| `dp[capacity]` | 해당 용량 이하에서 얻을 수 있는 최대 값어치를 저장 |
| `dp[current_weight - weight] + value` | 현재 보석을 하나 더 담았을 때의 값어치를 계산 |
| 정방향 용량 순회 | 같은 보석을 두 번 이상 담는 상태를 만들기 위해 사용 |
| `O(NW)` | 모든 보석에 대해 담을 수 있는 각 용량을 한 번씩 확인하기 때문 |

## problem-1871-line-up

### 1871 줄세우기

문제 파일: [1871_LineUp.py](gold/1871_LineUp.py)

배운 내용:

| 주제 | 이유 |
| --- | --- |
| [LIS와 최소 이동 횟수](#note-29-lis-minimum-moves) | 움직일 아이 대신 현재 위치를 유지할 수 있는 최대 인원을 찾기 위해 사용 |
| `dp[i]` | `i`번째 아이를 마지막으로 하는 LIS 길이를 저장 |
| `children[j] < children[i]` | `j`번째 아이 뒤에 `i`번째 아이를 붙여도 오름차순인지 판단 |
| `dp[i] = max(dp[i], dp[j] + 1)` | 가능한 앞쪽 증가 수열 중 가장 긴 수열 뒤에 현재 아이를 추가 |
| `N - max(dp)` | LIS에 속하지 않는 아이들만 옮기면 되므로 최소 이동 인원이 됨 |
| `O(N²)` | 각 아이마다 앞에 있는 모든 아이를 확인하며, `N ≤ 200`이라 충분함 |
