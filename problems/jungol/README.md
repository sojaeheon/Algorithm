# JUNGOL

JUNGOL 문제 풀이를 저장하는 폴더입니다.

## 파일 이름 규칙

```text
난이도/문제번호_문제이름.py
```

예시:

```text
silver/1997_TigerEatingRiceCakes.py
```

## 템플릿

프로그래머스식으로 먼저 연습할 때는 아래 템플릿을 사용합니다.

- [programmers_style_template.py](programmers_style_template.py)

기본 구조:

```python
def solution():
    pass
```

정올에 제출할 때는 `solution()` 안의 풀이 로직을 `input()` 기반 실행부와 연결합니다.

## 풀이 파일 상단 기록

```python
# JUNGOL 0000 문제이름
# 분류:
# 핵심:
# 시간 복잡도:
# 공간 복잡도:
```

## 분류 예시

```text
sorting
binary_search
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

| 문제 | 분류 | 핵심 |
| --- | --- | --- |
| [1997 떡 먹는 호랑이](silver/1997_TigerEatingRiceCakes.py) | dp, brute_force, fibonacci | D일째 떡 개수를 `x*A + y*B`로 표현하고, A를 대입해 B를 찾는다 |

## 복습 표시

| 표시 | 의미 |
| --- | --- |
| `review` | 다시 풀기 |
| `wrong` | 틀렸던 문제 |
| `hard` | 아이디어가 어려웠던 문제 |
