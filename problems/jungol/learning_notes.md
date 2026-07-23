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
