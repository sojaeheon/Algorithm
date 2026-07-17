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

### 문제별 메모

| 문제 | 배운 내용 |
| --- | --- |
| [3337 쇼핑몰](#problem-3337-shopping-mall) | heapq 튜플 비교, 정렬 기준, enumerate, `_` |
| [1357 합이 0이 되는 4개의 숫자들](#problem-1357-four-numbers-sum-zero) | meet in the middle, Counter, defaultdict, bisect |
| [2587 달리기](#problem-2587-running) | 좌표 압축, Fenwick Tree, Segment Tree와의 차이 |
| [1681 해밀턴 순환회로](#problem-1681-hamiltonian-cycle) | DFS 백트래킹, 순환회로, `nonlocal` |

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
