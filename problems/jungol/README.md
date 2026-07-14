# JUNGOL

JUNGOL 문제 풀이를 저장하는 폴더입니다.

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
gold/3337_ShoppingMall.py
gold/1357_FourNumbersSumZero.py
```

## 풀이 파일 상단 기록

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
dp
graph
string
geometry
brute_force
```

## 풀이 기록

| 문제 | 난이도 | 분류 | 핵심 |
| --- | --- | --- | --- |
| [1997 떡 먹는 호랑이](silver/1997_TigerEatingRiceCakes.py) | silver | dp, brute_force, fibonacci | D일째 떡 개수를 `x*A + y*B`로 표현하고, A를 대입해 B를 찾는다 |
| [1183 동전 자판기](gold/1183_CoinVendingMachine.py) | gold | greedy | 사용하는 동전 수 최대화 문제를 남기는 동전 수 최소화 문제로 바꾼다 |
| [3337 쇼핑몰](gold/3337_ShoppingMall.py) | gold | priority_queue, heap, sorting | 계산대 배정은 heap으로 처리하고, 퇴장 순서는 종료 시간과 계산대 번호로 정렬한다 |
| [1357 합이 0이 되는 4개의 숫자들](gold/1357_FourNumbersSumZero.py) | gold | meet_in_the_middle, hash, counter | `A+B = -(C+D)`로 나누고, `A+B` 합의 빈도수를 Counter에 저장해 센다 |

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
