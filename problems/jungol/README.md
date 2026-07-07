# JUNGOL

JUNGOL 문제 풀이를 정리하는 폴더입니다.

## 파일 이름 규칙

```text
티어/문제번호_문제이름.py
```

예시:

```text
silver/1997_TigerEatingRiceCakes.py
gold/1183_CoinVendingMachine.py
gold/1459_NumberSelection.py
gold/2468_Password.py
```

## 템플릿

먼저 문제 풀이용 뼈대를 잡고, 이후 `solution()` 안에 풀이 로직을 작성합니다.

- [programmers_style_template.py](programmers_style_template.py)

기본 구조:

```python
def solution():
    pass
```

정올에 제출할 때는 `solution()` 안의 로직과 `input()` 기반 실행부를 연결합니다.

## 문제 파일 상단 기록

```python
# JUNGOL 0000 문제이름
# 티어:
# 분류:
# 핵심:
# 시간 복잡도:
# 공간 복잡도:
```

## 분류 예시

```text
sorting
binary_search
greedy
stack
queue
deque
bfs
dfs
dp
graph
string
geometry
brute_force
bitmask
math
cycle
```

## 풀이 기록

| 문제 | 티어 | 분류 | 핵심 |
| --- | --- | --- | --- |
| [1997 떡 먹는 호랑이](silver/1997_TigerEatingRiceCakes.py) | silver | dp, brute_force, fibonacci | D일째 떡 개수를 `x*A + y*B`로 표현하고, A를 대입해 B를 찾는다. |
| [1183 동전 자판기](gold/1183_CoinVendingMachine.py) | gold | greedy | 사용하는 동전 수 최대화 문제를 남기는 동전 수 최소화 문제로 바꾼다. |
| [1459 숫자고르기](gold/1459_NumberSelection.py) | gold | dfs, graph, cycle | `i -> numbers[i]` 형태의 함수형 그래프로 보고, 시작점으로 다시 돌아오는 숫자를 고른다. |
| [2468 비밀번호](gold/2468_Password.py) | gold | math, bitmask, greedy | 이진수에서 1의 개수가 같은 가장 가까운 작은 수와 큰 수를 비트 패턴 재배치로 찾는다. |

## 오늘 푼 문제

### 1459 숫자고르기

- 핵심 관찰: 위칸 숫자 `i`에서 아래칸 숫자 `numbers[i]`로 이동하는 그래프로 볼 수 있다.
- 풀이 방향: 각 숫자를 시작점으로 두고, 아래칸 숫자를 따라가다가 다시 시작점으로 돌아오면 정답에 포함한다.
- 복잡도: `N <= 100`이라 시작점마다 탐색하는 `O(N^2)` 풀이로 충분하다.

### 2468 비밀번호

- 핵심 관찰: 이진수에서 `1`의 개수가 같은 수 중 가장 가까운 작은 수와 큰 수를 찾아야 한다.
- 큰 수 찾기: 오른쪽부터 `01`을 찾아 `10`으로 바꾸고, 오른쪽 비트의 `1`을 최대한 오른쪽으로 몰아 `000...111` 형태로 만든다.
- 작은 수 찾기: 오른쪽부터 `10`을 찾아 `01`로 바꾸고, 오른쪽 비트의 `1`을 최대한 왼쪽으로 몰아 `111...000` 형태로 만든다.
- 주의점: 큰 수를 찾을 때 `7 = 111` 같은 경우를 처리하려면 앞에 `0`을 붙여서 생각한다.

## 복습 표시

| 표시 | 의미 |
| --- | --- |
| `review` | 다시 풀기 |
| `wrong` | 틀렸던 문제 |
| `hard` | 아이디어가 어려웠던 문제 |
