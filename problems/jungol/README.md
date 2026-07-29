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
silver/1370_MeetingRoomAssignment.py
silver/1411_TilingTwoRows.py
silver/1520_ClimbingStairs.py
silver/2581_Budget.py
silver/2000_CoinChange.py
gold/1912_MazeSearch.py
gold/1183_CoinVendingMachine.py
gold/1809_Tower.py
gold/2300_Solution.py
gold/2613_Tomato.py
gold/1082_EscapeFromFire.py
gold/1840_Cheese.py
gold/1027_GoodSequence.py
silver/3706_CountZeroSumSubarrays.py
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
| [3865 Ski Course Rating](platinum/3865_SkiCourseRating.py) | platinum1 | kruskal, union_find, offline_query | 높이 차가 작은 간선부터 컴포넌트를 합쳐 각 시작점이 `T`개 칸에 도달하는 최소 난이도를 결정한다 |
| [3924 Superbull](gold/3924_Superbull.py) | gold | graph, mst, prim, maximum_spanning_tree | XOR로 간선 비용을 계산하는 완전 그래프에서 배열 기반 Prim으로 최대 신장 트리를 구한다 |
| [1024 내리막 길](gold/1024_DownhillPath.py) | gold | dfs, dp, memoization | 현재 칸에서 도착점까지 가는 경로 수를 DFS로 계산하고 칸별 결과를 재사용한다 |
| [1220 최장 공통 부분서열](gold/1220_LongestCommonSubsequence.py) | gold | dp, string, lcs | 2차원 LCS 점화식에서 필요한 이전 행만 1차원 배열에 저장한다 |
| [1871 줄세우기](gold/1871_LineUp.py) | gold | dp, lis | 현재 순서를 유지할 수 있는 가장 긴 증가 부분 수열을 남기고 나머지 아이들만 옮긴다 |
| [1077 배낭채우기1](silver/1077_FillKnapsack1.py) | silver | dp, unbounded_knapsack | 용량을 작은 값부터 갱신해 같은 보석을 무제한으로 사용하는 완전 배낭 문제를 푼다 |
| [1027 좋은수열](gold/1027_GoodSequence.py) | gold | backtracking, dfs | `1, 2, 3`을 작은 순서로 붙이고 마지막에 생긴 인접 부분 수열만 검사한다 |
| [1997 떡 먹는 호랑이](silver/1997_TigerEatingRiceCakes.py) | silver | dp, brute_force, fibonacci | D일째 떡 개수를 `x*A + y*B`로 표현하고, A를 대입해 B를 찾는다 |
| [1411 두 줄로 타일 깔기](silver/1411_TilingTwoRows.py) | silver | dp | `2×N` 판의 마지막 1칸/2칸을 기준으로 `dp[n] = dp[n-1] + 2*dp[n-2]`를 세운다 |
| [1520 계단 오르기](silver/1520_ClimbingStairs.py) | silver | dp | 마지막 계단을 반드시 밟되, 연속 세 계단을 피하도록 이전 두 경우를 비교한다 |
| [1370 회의실 배정](silver/1370_MeetingRoomAssignment.py) | silver2 | greedy, sorting | 종료 시간이 빠른 회의부터 선택해 한 회의실에 배정 가능한 회의 수를 최대로 만든다 |
| [2581 예산](silver/2581_Budget.py) | silver | binary_search, parametric_search | 상한액 `cap`이 가능한지 판단하며 가능한 최대 상한액을 이분 탐색으로 찾는다 |
| [2000 동전교환](silver/2000_CoinChange.py) | silver | dp, unbounded_knapsack | `dp[money]`에 금액을 만드는 최소 동전 수를 저장하고 마지막에 쓴 동전을 기준으로 갱신한다 |
| [1912 미로 탐색](gold/1912_MazeSearch.py) | gold4 | graph, dfs, stack, sorting | 인접 방을 번호순으로 정렬하고 stack DFS로 처음 방문한 순서를 구한다 |
| [1183 동전 자판기](gold/1183_CoinVendingMachine.py) | gold | greedy | 사용하는 동전 수 최대화 문제를 남기는 동전 수 최소화 문제로 바꾼다 |
| [1809 탑](gold/1809_Tower.py) | gold | stack, monotone_stack | 현재 탑보다 낮은 왼쪽 탑을 제거하고, 남은 stack top을 수신 탑으로 사용한다 |
| [2300 용액](gold/2300_Solution.py) | gold | two_pointer, sorting | 정렬 후 양끝 포인터를 움직이며 합이 0에 가장 가까운 두 값을 찾는다 |
| [2613 토마토(고)](gold/2613_Tomato.py) | gold | bfs, queue, graph | 처음부터 익은 모든 토마토를 동시에 BFS 시작점으로 넣어 최소 날짜를 구한다 |
| [1082 화염에서탈출](gold/1082_EscapeFromFire.py) | gold2 | bfs, queue, simulation | 불의 도착 시간을 먼저 계산하고 사람이 불보다 먼저 도착할 수 있는 칸만 이동한다 |
| [1840 치즈](gold/1840_Cheese.py) | gold3 | bfs, queue, simulation | 매 시간 바깥 공기를 BFS로 찾고, 닿은 치즈를 한꺼번에 녹인다 |
| [3706 합이 0이 되는 연속구간 세기](silver/3706_CountZeroSumSubarrays.py) | silver1 | prefix_sum, hash, counter | 같은 누적합이 나온 두 지점 사이의 구간 합이 0이라는 점을 이용한다 |
| [1357 합이 0이 되는 4개의 숫자들](platinum/1357_FourNumbersSumZero.py) | platinum | meet_in_the_middle, hash, counter | `A+B = -(C+D)`로 나누고, `A+B` 합의 빈도수를 Counter에 저장해 센다 |
| [1459 숫자고르기](gold/1459_NumberSelection.py) | gold | dfs, graph, cycle | `i -> numbers[i]` 형태의 함수형 그래프로 보고, 시작점으로 다시 돌아오는 숫자를 고른다 |
| [2468 비밀번호](gold/2468_Password.py) | gold | math, bitmask, greedy | 이진수에서 1의 개수가 같은 가장 가까운 작은 수와 큰 수를 비트 패턴 재배치로 찾는다 |
| [3337 쇼핑몰](gold/3337_ShoppingMall.py) | gold | priority_queue, heap, sorting | 계산대 배정은 heap으로 처리하고, 퇴장 순서는 종료 시간과 계산대 번호로 정렬한다 |
| [1214 히스토그램](platinum/1214_Histogram.py) | platinum | stack, monotone_stack | 현재 막대가 stack top보다 낮아지는 순간 top 막대의 최대 직사각형 넓이를 계산한다 |
| [2587 달리기](platinum/2587_Running.py) | platinum | coordinate_compression, fenwick_tree | 앞선 선수 중 현재 선수보다 실력이 좋은 선수 수를 Fenwick Tree로 구한다 |
| [1681 해밀턴 순환회로](silver/1681_HamiltonianCycle.py) | silver1 | dfs, backtracking, graph, tsp | 1번 정점에서 출발해 모든 정점을 한 번씩 방문하고 다시 1번 정점으로 돌아오는 최소 비용을 찾는다 |
| [1545 해밀턴 순환회로 2](platinum/1545_HamiltonianCycle2.py) | platinum5 | bitmask, dp, graph, tsp | 방문 상태를 비트마스크로 표현하고 `dp[mask][current]`로 최소 비용을 저장한다 |

## 오늘 푼 문제

### 3865 Ski Course Rating

- 문제 목표: 각 출발점에서 상하좌우로 최소 `T`개 칸에 도달할 수 있게 하는 최소 허용 높이 차를 구하고 모두 더한다.
- 그래프 모델링: 격자 칸을 정점, 인접한 두 칸을 간선, 두 칸의 높이 차를 간선 가중치로 본다.
- 핵심 관찰: 가중치가 `D` 이하인 간선으로 연결된 컴포넌트는 난이도 `D`로 서로 이동할 수 있는 칸들의 집합이다.
- 접근 방향: 간선을 높이 차 오름차순으로 처리하는 크루스칼과 Union-Find를 사용한다.
- 난이도 확정: 시작점이 속한 컴포넌트 크기가 처음 `T` 이상이 되는 간선 가중치가 그 시작점의 최소 난이도이다.
- 간선 생성: 무방향 간선 중복을 피하기 위해 각 칸에서 오른쪽과 아래쪽 간선만 만든다.
- 좌표 변환: `(row, col)`을 `row * N + col`로 바꿔 Union-Find의 1차원 인덱스로 사용한다.
- `size[root]`: 현재 컴포넌트에 포함된 칸 수이다.
- `pending_starts[root]`: 현재 컴포넌트에서 아직 난이도가 확정되지 않은 시작점 수이다.
- 중복 방지: 컴포넌트 크기가 `T` 이상이면 `cost * pending_starts[root]`를 답에 더한 뒤 값을 `0`으로 만든다.
- 예외 처리: `T == 1`이면 출발한 칸 하나로 조건을 만족하므로 모든 시작점의 난이도는 `0`이다.
- 복잡도: 간선이 약 `2MN`개이므로 시간 `O(MN log(MN))`, 공간 `O(MN)`이다.

### 1024 내리막 길

- 문제 목표: 왼쪽 위에서 오른쪽 아래까지 상하좌우로 이동하되, 항상 현재보다 낮은 칸으로만 가는 경로의 수를 구한다.
- DP 정의: `dfs(row, col)`은 `(row, col)`에서 도착점까지 가는 내리막 경로의 수이다.
- Top-down DP: DFS로 필요한 하위 상태를 먼저 계산하고 결과를 `memo[row][col]`에 저장한다.
- 도착점: 도착점에 도달하면 완성된 경로 하나를 의미하는 `1`을 반환한다.
- 점화식: 현재 칸의 경로 수는 이동 가능한 모든 낮은 이웃 칸의 `dfs` 결과를 더한 값이다.
- 메모 상태: `-1`은 아직 계산하지 않음, `0`은 계산했지만 경로 없음, 양수는 도착점까지 가는 경로 수이다.
- 사이클이 없는 이유: 이동할 때마다 높이가 엄격히 낮아지므로 이전 칸으로 돌아갈 수 없다.
- 메모이제이션 효과: 여러 경로가 같은 칸에서 합쳐져도 그 칸 이후의 경로는 한 번만 계산한다.
- 재귀 제한: 높이가 최대 10,000이므로 최대 재귀 깊이도 10,000 이하이다. `1_000_000`처럼 과도한 값을 쓰면 메모리 초과가 생길 수 있다.
- 반복문 대안: 높은 칸에서 낮은 칸으로 간선을 만든 DAG로 보고 위상정렬 DP를 사용할 수 있다.
- 방식 선택: 이 문제에서는 DFS 메모이제이션이 간단하고 추가 배열이 적다. 재귀 깊이를 예측할 수 없거나 매우 크다면 반복 DFS·BFS·위상정렬을 고려한다.
- 복잡도: DFS 메모이제이션과 위상정렬 DP 모두 시간 `O(NM)`, 공간 `O(NM)`이다.

### 1220 최장 공통 부분서열

- 문제 목표: 두 문자열에 공통으로 포함되면서 문자 순서를 유지하는 가장 긴 부분서열의 길이를 구한다.
- 2차원 DP 정의: `dp[i][j]`는 `first[:i]`와 `second[:j]`의 LCS 길이이다.
- 문자가 같은 경우: 공통 문자 하나를 추가할 수 있으므로 `dp[i][j] = dp[i-1][j-1] + 1`이다.
- 문자가 다른 경우: 어느 한쪽의 현재 문자를 제외한 결과 중 큰 값을 선택하므로 `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`이다.
- 공간 최적화: 현재 행을 계산할 때 이전 행과 현재 행의 왼쪽 값만 필요하므로 하나의 1차원 배열을 재사용할 수 있다.
- 갱신 전 `dp[j]`: 2차원 표의 위쪽 값 `dp[i-1][j]`이다.
- 갱신된 `dp[j-1]`: 2차원 표의 왼쪽 값 `dp[i][j-1]`이다.
- `diagonal`: 덮어쓰면 사라지는 왼쪽 위 값 `dp[i-1][j-1]`을 저장한다.
- `diagonal` 갱신: 현재 칸의 갱신 전 `dp[j]`는 오른쪽 다음 칸에서 왼쪽 위 값이 되므로 `diagonal = previous_up`으로 옮긴다.
- 초기화 이유: 새로운 행의 첫 열에서 왼쪽 위는 `dp[i-1][0] = 0`이므로 행마다 `diagonal = 0`으로 시작한다.
- 복잡도: 시간 `O(NM)`, 공간 `O(min(N, M))`이다.

### 1871 줄세우기

- 문제 목표: 임의의 순서로 서 있는 아이들을 번호순으로 만들기 위해 위치를 옮겨야 하는 최소 인원을 구한다.
- 관점 바꾸기: 옮기는 아이를 직접 고르기보다, 현재 위치를 유지할 수 있는 아이를 최대한 많이 고른다.
- 그대로 둘 조건: 움직이지 않는 아이들은 최종 번호순에서도 상대적인 순서가 같아야 하므로 현재 줄에서 오름차순을 이루어야 한다.
- 핵심 연결: 그대로 둘 수 있는 최대 인원은 현재 수열의 LIS(최장 증가 부분 수열) 길이이다.
- 정답: `N - LIS 길이`이다.
- DP 정의: `dp[i]`는 `i`번째 아이를 마지막으로 선택하는 증가 부분 수열의 최대 길이이다.
- 초기값: 모든 아이는 혼자서 길이 1의 증가 수열을 만들 수 있으므로 `dp = [1] * N`이다.
- 전이 조건: `j < i`이고 `children[j] < children[i]`이면 `j`번째 아이 뒤에 `i`번째 아이를 붙일 수 있다.
- 점화식: `dp[i] = max(dp[i], dp[j] + 1)`이다.
- 복잡도: `N ≤ 200`이므로 이중 반복문을 사용해 시간 `O(N²)`, 공간 `O(N)`으로 해결한다.
- 더 빠른 방법: 각 길이의 증가 부분 수열이 가질 수 있는 가장 작은 마지막 값을 `lis`에 저장하면 이분 탐색으로 LIS 길이를 구할 수 있다.
- 이분 탐색 갱신: `bisect_left(lis, child)`로 현재 아이 이상인 첫 위치를 찾아 교체하고, 그런 위치가 없으면 끝에 추가한다.
- 교체 이유: 같은 길이의 증가 부분 수열이라면 마지막 값이 작을수록 이후 더 많은 값을 붙일 수 있다.
- 이분 탐색 복잡도: 아이마다 `O(log N)`으로 위치를 찾으므로 시간 `O(N log N)`, 공간 `O(N)`이다.
- 주의점: 교체로 만든 `lis` 배열은 실제 LIS 원소 목록과 다를 수 있지만, 배열의 길이는 정확한 LIS 길이이다.

### 1077 배낭채우기1

- 문제 목표: 각 보석을 무제한으로 사용할 수 있을 때, 무게가 배낭 용량 `W`를 넘지 않도록 담아 얻는 최대 값어치를 구한다.
- DP 정의: `dp[capacity]`는 용량이 `capacity` 이하인 배낭에서 얻을 수 있는 최대 값어치이다.
- 담지 않는 경우: 기존 값인 `dp[current_weight]`를 유지한다.
- 하나 더 담는 경우: `dp[current_weight - weight] + value`이다.
- 점화식: `dp[current_weight] = max(dp[current_weight], dp[current_weight - weight] + value)`이다.
- 순회 방향: 용량을 `weight`부터 `W`까지 정방향으로 확인한다. 현재 보석으로 앞에서 갱신한 값을 뒤에서 다시 사용할 수 있으므로 같은 보석을 여러 번 담을 수 있다.
- 0/1 배낭과 차이: 물건을 한 번만 사용할 수 있다면 같은 물건의 갱신 값을 재사용하지 않도록 용량을 역방향으로 확인한다.
- 정답: `dp[W]`에 용량 `W` 이하에서 얻을 수 있는 최대 값어치가 저장된다.
- 복잡도: 시간 `O(NW)`, 공간 `O(W)`이다.

### 1027 좋은수열

- 문제 목표: `1`, `2`, `3`으로 이루어진 길이 `N`의 좋은 수열 중 가장 작은 수열을 찾는다.
- 나쁜 수열: 임의의 길이로 잘랐을 때 같은 두 부분 수열이 서로 붙어 있는 수열이다. 예를 들어 `1212`는 `12 | 12`가 있으므로 나쁘다.
- 접근 방향: 현재 수열 뒤에 `1`, `2`, `3`을 차례로 붙이며 DFS 백트래킹을 한다.
- 최소값 보장: 숫자를 항상 `1 → 2 → 3` 순서로 시도하므로 처음 완성되는 길이 `N`의 수열이 가장 작은 답이다.
- 검사 범위: 숫자를 붙이기 전 수열은 이미 좋으므로, 새 숫자를 포함하는 수열의 마지막 부분만 검사하면 된다.
- 부분 수열 비교: 길이가 `size`인 마지막 두 덩어리
  `sequence[length - 2 * size : length - size]`와
  `sequence[length - size :]`를 비교한다.
- 검사 길이: 두 덩어리에는 `2 * size`개의 원소가 필요하므로 `size`는 `1`부터 `length // 2`까지만 확인한다.
- 가지치기: 마지막 두 부분 수열이 같으면 더 긴 좋은 수열로 만들 수 없으므로 즉시 이전 상태로 돌아간다.
- 복잡도: 최악의 탐색 경우의 수는 지수적이지만 가지치기가 강하게 적용된다. 재귀 호출과 현재 수열 저장 공간은 `O(N)`이다.

### 3706 합이 0이 되는 연속구간 세기

- 핵심 관찰: `prefix[j] - prefix[i] == 0`이면 `prefix[j] == prefix[i]`이다.
- 접근 방향: 지금까지 나온 누적합의 개수를 `Counter`에 저장한다.
- 초기값: 시작 전 누적합 `0`을 세기 위해 `prefix_count[0] = 1`로 시작한다.
- 정답 갱신: 현재 누적합이 이전에 `k`번 나왔다면, 현재 위치에서 끝나는 합 0 구간이 `k`개 생긴다.
- 갱신 순서: `answer += prefix_count[prefix_sum]`을 먼저 하고, 그 뒤 `prefix_count[prefix_sum] += 1`로 현재 누적합을 기록한다.
- 복잡도: 수열을 한 번만 보므로 시간 `O(N)`, 누적합 개수 저장 때문에 공간 `O(N)`이다.

### 1912 미로 탐색

- 핵심 관찰: 현재 방에서 방문하지 않은 인접 방이 여러 개라면 번호가 가장 작은 방을 먼저 방문해야 한다.
- 접근 방향: 방과 문을 양방향 그래프로 보고, 각 방의 인접 리스트를 오름차순 정렬한다.
- DFS 방식: 깊게 들어가다가 더 갈 방이 없으면 이전 방으로 되돌아가므로 DFS와 같다.
- 구현 선택: `N`이 최대 100000이라 재귀 DFS는 깊이 제한에 걸릴 수 있으므로 `stack`으로 반복 DFS를 구현한다.
- `next_index` 역할: 각 방에서 인접 리스트를 어디까지 확인했는지 저장해, 되돌아온 뒤 같은 인접 방을 처음부터 다시 훑지 않게 한다.
- 복잡도: 인접 리스트 정렬 때문에 시간 `O(M log M)` 수준, 탐색 자체는 `O(N + M)`, 공간은 `O(N + M)`이다.

### 2613 토마토(고)

- 핵심 관찰: 익은 토마토가 여러 개라면 모든 익은 토마토에서 동시에 익음이 퍼진다.
- 접근 방향: 처음부터 익은 토마토 위치를 모두 큐에 넣는 multi-source BFS를 사용한다.
- 날짜 계산: 처음 익은 토마토를 `1`로 두고, 새로 익은 칸에는 `이전 칸 값 + 1`을 저장한다. 실제 날짜는 `box 값 - 1`이다.
- 불가능 판단: `unripe_count`로 익지 않은 토마토 수를 관리하고, BFS가 끝난 뒤 남아 있으면 `-1`을 출력한다.
- 최적화: `unripe_count`를 쓰면 BFS 후 전체 상자를 다시 훑지 않아도 된다.
- 복잡도: 각 칸은 최대 한 번 큐에 들어가므로 시간 `O(NM)`, 상자와 큐 때문에 공간 `O(NM)`이다.

### 1082 화염에서탈출

- 핵심 관찰: 사람과 불이 동시에 움직이므로, 사람이 어떤 칸에 도착하는 시간보다 불이 먼저 또는 동시에 도착하면 그 칸은 갈 수 없다.
- 접근 방향: 불의 도착 시간을 먼저 BFS로 계산하고, 이후 사람 BFS에서 안전한 칸만 이동한다.
- `fire_time` 의미: `fire_time[r][c]`는 불이 `(r, c)` 칸에 처음 도착하는 시간이다. `INF`면 불이 도착하지 못하는 칸이다.
- 방문 체크: `fire_time[next_row][next_col] != INF`는 이미 불 도착 시간이 기록된 칸이므로 다시 큐에 넣지 않겠다는 뜻이다.
- 이동 조건: `fire_time[next_row][next_col] <= next_time`이면 불이 같거나 더 빠르게 도착하므로 이동할 수 없다.
- 목적지 처리: 목적지 `D`는 불이 번지지 않는 칸으로 보고, 사람 BFS에서 도착하면 즉시 최소 시간을 반환한다.
- 복잡도: 불 BFS와 사람 BFS 모두 각 칸을 최대 한 번씩 보므로 시간 `O(RC)`, `fire_time`, `person_time`, 큐 때문에 공간 `O(RC)`이다.

### 1840 치즈

- 핵심 관찰: 치즈 내부 구멍은 바깥 공기와 연결되기 전까지 공기가 아니므로, 내부 구멍과 닿은 치즈는 바로 녹지 않는다.
- 접근 방향: 매 시간 `(0, 0)`에서 BFS를 시작해 바깥 공기만 탐색한다.
- 녹일 치즈 찾기: 바깥 공기 BFS 중 치즈 `1`을 만나면 그 칸은 이번 시간에 녹을 치즈이므로 `melt`에 저장한다.
- 한꺼번에 녹이는 이유: BFS 도중 바로 `0`으로 바꾸면 같은 시간 안에 치즈 안쪽까지 공기가 들어간 것처럼 처리될 수 있다.
- 마지막 치즈 수: 각 시간이 시작될 때 `last_cheese_count = cheese_count`로 저장하면, 마지막 반복에서 모두 녹기 한 시간 전 치즈 수가 된다.
- `T` 의미: `T`는 치즈가 모두 녹는 데 걸리는 시간이다. `N, M <= 100`이라 보통 최대 약 `min(N, M) / 2` 수준이고, 넉넉히 잡아도 100 안쪽으로 볼 수 있다.
- 복잡도: 매 시간 BFS가 `N*M` 칸을 볼 수 있으므로 시간 `O(TNM)`, 방문 배열과 큐 때문에 공간 `O(NM)`이다.

### 1411 두 줄로 타일 깔기

- 핵심 관찰: `2×N` 판의 오른쪽 끝을 어떻게 채우는지에 따라 이전 상태가 결정된다.
- DP 정의: `dp[n] = 2×n 판을 채우는 방법의 수`
- 초기값: `dp[1] = 1`, `dp[2] = 3`
- 점화식: `dp[n] = dp[n - 1] + 2 * dp[n - 2]`
- `2 * dp[n - 2]` 이유: 마지막 `2×2`를 채우는 3가지 중 세로 타일 2개는 `dp[n-1]` 쪽에서 이미 세므로, 남은 2가지 경우만 곱한다.
- MOD 처리: 경우의 수가 매우 커지므로 매 단계에서 `20100529`로 나눈 나머지를 저장한다.
- 복잡도: 한 번의 반복으로 계산하므로 시간 `O(N)`, 이전 두 값만 저장하면 공간 `O(1)`이다.

### 1520 계단 오르기

- 핵심 관찰: 마지막 계단은 반드시 밟아야 하고, 연속 세 계단은 밟을 수 없다.
- DP 정의: `dp[i] = i번째 계단을 반드시 밟았을 때 얻을 수 있는 최대 점수`
- 경우 1: `i-2`번째에서 두 칸 올라와 `i`번째를 밟는다.
- 경우 2: `i-3`번째에서 `i-1`번째를 밟고, 다시 `i`번째를 밟는다.
- 점화식: `dp[i] = max(dp[i-2] + score[i], dp[i-3] + score[i-1] + score[i])`
- 복잡도: 계단을 한 번씩 계산하므로 시간 `O(N)`, DP 배열 때문에 공간 `O(N)`이다.

### 2000 동전교환

- 핵심 관찰: 어떤 금액을 만들 때 마지막에 사용한 동전을 하나 정하면 이전 금액이 결정된다.
- DP 정의: `dp[money] = money원을 만드는 데 필요한 최소 동전 개수`
- 초기값: `dp[0] = 0`, 나머지는 만들 수 없다는 뜻으로 `INF`로 둔다.
- 점화식: `dp[money] = min(dp[money], dp[money - coin] + 1)`
- 의미: `money - coin`원을 만든 뒤 `coin` 하나를 추가하면 `money`원을 만들 수 있다.
- 불가능 처리: 마지막에 `dp[W]`가 아직 `INF`이면 `"impossible"`을 출력한다.
- 복잡도: 목표 금액마다 모든 동전을 확인하므로 시간 `O(NW)`, 금액별 최소 개수 배열 때문에 공간 `O(W)`이다.

### 2300 용액

- 핵심 관찰: 두 용액의 합이 0에 가까워야 하므로, 정렬 후 가장 작은 값과 가장 큰 값부터 비교한다.
- 접근 방향: `left = 0`, `right = N - 1`에서 시작하는 투 포인터를 사용한다.
- 정답 갱신: `abs(values[left] + values[right])`가 더 작으면 현재 두 값을 정답 후보로 저장한다.
- 이동 기준: 합이 음수이면 값을 키워야 하므로 `left += 1`, 합이 양수이면 값을 줄여야 하므로 `right -= 1` 한다.
- 조기 종료: 합의 절댓값이 `0`이면 더 좋은 답이 없으므로 바로 끝낼 수 있다.
- 복잡도: 정렬 때문에 시간 `O(N log N)`, 투 포인터 탐색은 `O(N)`이다.

### 2581 예산

- 핵심 관찰: 상한액 `cap`을 정하면 실제 배정 예산은 `sum(min(request, cap))`으로 계산할 수 있다.
- 접근 방향: 가능한 상한액 중 최댓값을 찾는 문제이므로 이분 탐색을 사용한다.
- 가능 조건: `used_budget <= total_budget`이면 현재 `cap`은 가능하다.
- 가능할 때: 현재 `cap`을 정답 후보로 저장하고, 더 큰 상한액을 찾기 위해 `left = cap + 1`로 이동한다.
- 불가능할 때: 예산을 초과했으므로 상한액을 줄이기 위해 `right = cap - 1`로 이동한다.
- 복잡도: 이분 탐색이 `log M`번 돌고, 매번 `N`개 요청을 확인하므로 시간 `O(N log M)`, 공간 `O(N)`이다.

### 1370 회의실 배정

- 핵심 관찰: 끝나는 시간이 빠른 회의를 먼저 선택하면 남은 시간에 더 많은 회의를 넣을 수 있다.
- 정렬 기준: `(종료 시간, 시작 시간)` 기준으로 오름차순 정렬한다.
- 선택 조건: 현재 회의의 시작 시간이 마지막 선택 회의의 종료 시간 이상이면 선택한다.
- `start_time >= last_end_time`을 쓰는 이유: 문제에서 종료 시간과 시작 시간이 같은 경우는 겹치지 않는다고 했기 때문이다.
- 출력: 선택한 회의 개수를 먼저 출력하고, 다음 줄에 선택한 회의 번호를 시간대순으로 출력한다.
- 복잡도: 정렬 때문에 시간 `O(N log N)`, 선택 결과 저장 때문에 공간 `O(N)`이다.

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
| 회의실 배정 그리디 | [학습 메모](learning_notes.md#note-18-meeting-room-greedy) |
| 매개변수 탐색 | [학습 메모](learning_notes.md#note-19-parametric-search) |
| 투 포인터 | [학습 메모](learning_notes.md#note-20-two-pointer) |
| 누적합과 해시 | [학습 메모](learning_notes.md#note-21-prefix-sum-hash) |
