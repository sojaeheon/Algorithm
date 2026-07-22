# JUNGOL

JUNGOL 문제 풀이를 정리하는 폴더입니다.

## 바로가기

- [학습 메모](learning_notes.md)
- [프로그래머스식 풀이 템플릿](programmers_style_template.py)

## 파일 이름 규칙

```text
난이도/문제번호_문제이름.py
```

예시:

```text
silver/1997_TigerEatingRiceCakes.py
gold/1183_CoinVendingMachine.py
gold/1809_Tower.py
gold/1459_NumberSelection.py
gold/2468_Password.py
gold/3337_ShoppingMall.py
platinum/1357_FourNumbersSumZero.py
platinum/1545_HamiltonianCycle2.py
platinum/1214_Histogram.py
platinum/2587_Running.py
silver/1681_HamiltonianCycle.py
```

## 템플릿

먼저 문제 풀이용 뼈대를 잡고, 이후 `solution()` 안에 풀이 로직을 작성합니다.

- [programmers_style_template.py](programmers_style_template.py)

기본 구조:

```python
def solution():
    pass
```

정올에 제출할 때는 `solution()`의 로직과 `input()` 기반 실행부를 연결합니다.

## 문제 파일 상단 기록

```python
# JUNGOL 0000 문제이름
# 난이도:
# 분류:
# 핵심:
# 시간 복잡도:
# 공간 복잡도:
```

## 분류 예시

```text
sorting
binary_search
two_pointer
meet_in_the_middle
coordinate_compression
fenwick_tree
segment_tree
hash
counter
greedy
heap
priority_queue
stack
queue
deque
bfs
dfs
backtracking
dp
graph
tsp
string
geometry
brute_force
bitmask
math
cycle
monotone_stack
```

## 풀이 기록

| 문제 | 난이도 | 분류 | 핵심 |
| --- | --- | --- | --- |
| [1997 떡 먹는 호랑이](silver/1997_TigerEatingRiceCakes.py) | silver | dp, brute_force, fibonacci | D일째 떡 개수를 `x*A + y*B`로 표현하고, A를 대입해 B를 찾는다 |
| [1183 동전 자판기](gold/1183_CoinVendingMachine.py) | gold | greedy | 사용하는 동전 수 최대화 문제를 남기는 동전 수 최소화 문제로 바꾼다 |
| [1809 탑](gold/1809_Tower.py) | gold | stack, monotone_stack | 현재 탑보다 낮은 왼쪽 탑을 제거하고, 남은 stack top을 수신 탑으로 사용한다 |
| [1357 합이 0이 되는 4개의 숫자들](platinum/1357_FourNumbersSumZero.py) | platinum | meet_in_the_middle, hash, counter | `A+B = -(C+D)`로 나누고, `A+B` 합의 빈도수를 Counter에 저장해 센다 |
| [1459 숫자고르기](gold/1459_NumberSelection.py) | gold | dfs, graph, cycle | `i -> numbers[i]` 형태의 함수형 그래프로 보고, 시작점으로 다시 돌아오는 숫자를 고른다 |
| [2468 비밀번호](gold/2468_Password.py) | gold | math, bitmask, greedy | 이진수에서 1의 개수가 같은 가장 가까운 작은 수와 큰 수를 비트 패턴 재배치로 찾는다 |
| [3337 쇼핑몰](gold/3337_ShoppingMall.py) | gold | priority_queue, heap, sorting | 계산대 배정은 heap으로 처리하고, 퇴장 순서는 종료 시간과 계산대 번호로 정렬한다 |
| [1214 히스토그램](platinum/1214_Histogram.py) | platinum | stack, monotone_stack | 현재 막대가 stack top보다 낮아지는 순간 top 막대의 최대 직사각형 넓이를 계산한다 |
| [2587 달리기](platinum/2587_Running.py) | platinum | coordinate_compression, fenwick_tree | 앞선 선수 중 현재 선수보다 실력이 좋은 선수 수를 Fenwick Tree로 구한다 |
| [1681 해밀턴 순환회로](silver/1681_HamiltonianCycle.py) | silver1 | dfs, backtracking, graph, tsp | 1번 정점에서 출발해 모든 정점을 한 번씩 방문하고 다시 1번 정점으로 돌아오는 최소 비용을 찾는다 |
| [1545 해밀턴 순환회로 2](platinum/1545_HamiltonianCycle2.py) | platinum5 | bitmask, dp, graph, tsp | 방문 상태를 비트마스크로 표현하고 `dp[mask][current]`로 최소 비용을 저장한다 |

## 오늘 푼 문제

### 1809 탑

- 핵심 관찰: 현재 탑의 신호를 받을 수 있는 탑은 왼쪽에 있는 탑 중 현재 탑보다 높거나 같은 가장 가까운 탑이다.
- 접근 방향: stack에 오른쪽 탑의 신호를 받을 가능성이 있는 탑만 남긴다.
- 제거 조건: stack top의 높이가 현재 탑보다 낮으면 현재 탑에 가려지므로 pop한다.
- 정답 계산: 낮은 탑을 제거한 뒤 stack이 남아 있으면 `stack[-1][0]`이 수신 탑 번호이고, 비어 있으면 `0`이다.
- 현재 탑 저장: 이후 오른쪽 탑들의 후보가 될 수 있으므로 `(tower_number, height)`를 stack에 넣는다.
- 복잡도: 각 탑은 한 번 push되고 최대 한 번 pop되므로 시간 `O(N)`, 공간 `O(N)`이다.

### 1545 해밀턴 순환회로 2

- 핵심 관찰: `N <= 19`라 DFS 백트래킹 `O(N!)`은 어렵고, 비트마스크 DP로 같은 상태를 재사용해야 한다.
- DP 상태: `dp[mask][current]`는 `mask`에 포함된 장소들을 방문했고 현재 `current`에 있을 때의 최소 비용이다.
- 시작 상태: `dp[1][0] = 0`이다. `1`은 비트로 `000...001`이므로 0번 장소, 즉 회사만 방문한 상태이다.
- 방문 확인: `mask & (1 << next_node)`가 0이 아니면 `next_node`는 이미 방문한 장소이다.
- 상태 전이: `next_mask = mask | (1 << next_node)`로 다음 장소를 방문 목록에 추가한다.
- 마지막 처리: 모든 장소를 방문한 `full` 상태에서 마지막 장소가 `current`일 때, `cost[current][0]`을 더해 회사로 돌아온다.
- 복잡도: 시간 `O(N^2 * 2^N)`, 공간 `O(N * 2^N)`이다. Python 제출은 PyPy3가 더 유리하다.

### 1681 해밀턴 순환회로

- 핵심 관찰: 순환회로는 모든 정점을 정확히 한 번씩 방문한 뒤 다시 시작점으로 돌아오는 경로이다.
- 접근 방향: 시작점을 1번 정점으로 고정하고 DFS 백트래킹으로 방문 순서를 만든다.
- DFS 상태: `current`는 현재 정점, `count`는 방문한 정점 수, `total_cost`는 지금까지의 비용이다.
- 종료 조건: `count == N`이면 모든 정점을 방문한 상태이므로, 현재 정점에서 시작점으로 돌아갈 수 있을 때만 정답을 갱신한다.
- 가지치기: 이미 `total_cost >= answer`이면 더 탐색해도 최소 비용이 될 수 없으므로 중단한다.
- 복잡도: 최악의 경우 가능한 방문 순서를 모두 보므로 시간 `O(N!)`, 방문 배열과 재귀 깊이 때문에 공간 `O(N)`이다.

### 2587 달리기

- 핵심 관찰: 현재 선수의 최고 등수는 `앞에 있는 선수 중 현재 선수보다 실력이 좋은 선수 수 + 1`이다.
- 접근 방향: 실력 값을 좌표 압축한 뒤, Fenwick Tree에 지금까지 등장한 실력 개수를 저장한다.
- 현재 선수의 압축 실력이 `rank`라면 나보다 실력이 좋은 선수는 `rank + 1 ~ max_rank` 구간에 있다.
- 계산식: `better_count = query(max_rank) - query(rank)`
- 복잡도: 좌표 압축과 각 선수의 update/query를 포함해 시간 `O(N log N)`, 공간 `O(N)`이다.

### 1214 히스토그램

- 핵심 관찰: 어떤 막대를 높이로 삼으면, 그 막대보다 낮은 막대가 나오기 전까지 좌우로 확장할 수 있다.
- 접근 방향: stack에 높이가 오름차순이 되도록 인덱스를 저장한다.
- 넓이 계산 시점: 현재 막대가 stack top보다 낮아지면 top 막대의 오른쪽 경계가 현재 위치 바로 전으로 확정된다.
- 너비 계산:
  - stack이 남아 있으면 `i - stack[-1] - 1`
  - stack이 비면 `i`
- 복잡도: 각 막대는 한 번 push되고 한 번 pop되므로 시간 `O(N)`, 공간 `O(N)`이다.

### 1459 숫자고르기

- 핵심 관찰: 위쪽 숫자 `i`에서 아래쪽 숫자 `numbers[i]`로 이동하는 그래프로 볼 수 있다.
- 접근 방향: 각 숫자를 시작점으로 두고, 아래쪽 숫자를 따라가다가 다시 시작점으로 돌아오면 정답에 포함한다.
- 복잡도: `N <= 100`이라 시작점마다 탐색하는 `O(N^2)` 풀이로 충분하다.

### 2468 비밀번호

- 핵심 관찰: 이진수에서 `1`의 개수가 같은 수 중 가장 가까운 작은 수와 큰 수를 찾는다.
- 큰 수 찾기: 오른쪽부터 `01`을 찾아 `10`으로 바꾸고, 오른쪽 비트의 `1`을 최대한 오른쪽으로 모은다.
- 작은 수 찾기: 오른쪽부터 `10`을 찾아 `01`로 바꾸고, 오른쪽 비트의 `1`을 최대한 왼쪽으로 모은다.
- 주의점: 큰 수를 찾을 때 `7 = 111` 같은 경우를 처리하려면 앞에 `0`을 붙여 생각한다.

### 1357 합이 0이 되는 4개의 숫자들

- 핵심 관찰: `A+B+C+D=0`을 `A+B=-(C+D)`로 나눈다.
- 접근 방향: `A+B`의 합을 해시에 빈도수로 저장하고, `C+D`를 돌면서 반대값 개수를 더한다.
- 주의점: `defaultdict(int)`는 없는 key를 `[]`로 조회하면 key를 새로 만들기 때문에 메모리 초과가 날 수 있다. 이 문제는 `Counter`가 더 안전하다.

## 복습 표시

| 표시 | 의미 |
| --- | --- |
| `review` | 다시 풀기 |
| `wrong` | 틀렸던 문제 |
| `hard` | 아이디어가 어려웠던 문제 |

## 학습 메모 기록

| 주제 | 연결 |
| --- | --- |
| heapq 튜플 비교 | [학습 메모](learning_notes.md#note-01-heapq-tuple) |
| 정렬 기준에서 일부만 내림차순 처리 | [학습 메모](learning_notes.md#note-02-sort-reverse-part) |
| enumerate와 start 옵션 | [학습 메모](learning_notes.md#note-03-enumerate-start) |
| `_`로 사용하지 않는 값 받기 | [학습 메모](learning_notes.md#note-04-unused-underscore) |
| meet in the middle | [학습 메모](learning_notes.md#note-05-meet-in-the-middle) |
| Counter와 defaultdict 차이 | [학습 메모](learning_notes.md#note-06-counter-defaultdict) |
| bisect와 이분 탐색 | [학습 메모](learning_notes.md#note-07-bisect-binary-search) |
| Python 시간/메모리 판단 | [학습 메모](learning_notes.md#note-08-python-limits) |
| 좌표 압축 | [학습 메모](learning_notes.md#note-09-coordinate-compression) |
| Fenwick Tree | [학습 메모](learning_notes.md#note-10-fenwick-tree) |
| Segment Tree | [학습 메모](learning_notes.md#note-11-segment-tree) |
| Fenwick Tree와 Segment Tree 차이 | [학습 메모](learning_notes.md#note-12-fenwick-vs-segment) |
| DFS 백트래킹 | [학습 메모](learning_notes.md#note-13-dfs-backtracking) |
| 해밀턴 순환회로 | [학습 메모](learning_notes.md#note-14-hamiltonian-cycle) |
| nonlocal | [학습 메모](learning_notes.md#note-15-nonlocal) |
| 비트마스크 DP | [학습 메모](learning_notes.md#note-16-bitmask-dp) |
| 단조 스택 | [학습 메모](learning_notes.md#note-17-monotone-stack) |
