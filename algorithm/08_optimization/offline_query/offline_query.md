# Offline Query

오프라인 쿼리는 쿼리를 입력받은 순서대로 바로 처리하지 않고, 정렬하거나 묶어서 더 효율적인 순서로 처리하는 기법이다.

처리가 끝난 뒤에는 각 쿼리의 원래 번호를 이용해 답을 원래 순서대로 복원한다.

## 1. 온라인과 오프라인

| 방식 | 의미 |
| --- | --- |
| 온라인 처리 | 쿼리를 입력 순서대로 즉시 처리 |
| 오프라인 처리 | 쿼리를 모두 모은 뒤 정렬하거나 재배치해서 처리 |

오프라인 쿼리는 쿼리의 순서를 바꿔도 최종 답에 문제가 없을 때 사용할 수 있다.

## 2. 언제 쓰는가

다음 조건이 보이면 오프라인 처리를 생각해볼 수 있다.

- 쿼리가 매우 많다.
- 매번 처음부터 계산하면 느리다.
- 쿼리를 정렬하면 상태를 조금씩만 바꾸며 처리할 수 있다.
- 답은 각 쿼리별로 독립적이다.
- 원래 순서대로 출력만 하면 된다.

## 3. 기본 구조

쿼리를 저장할 때 원래 인덱스를 함께 저장한다.

```python
queries = []

for idx in range(q):
    left, right = map(int, input().split())
    queries.append((left, right, idx))

queries.sort()

answer = [0] * q

for left, right, idx in queries:
    result = 0
    answer[idx] = result

for x in answer:
    print(x)
```

## 4. 정렬 후 처리

예를 들어 `x` 이하의 값만 고려해서 쿼리에 답해야 하는 문제가 있다고 하자.

배열 값과 쿼리를 모두 정렬하면, 현재 기준 이하의 값만 자료구조에 추가하면서 처리할 수 있다.

```python
arr_items.sort()       # (value, position)
queries.sort()         # (limit, left, right, idx)

p = 0
answer = [0] * q

for limit, left, right, idx in queries:
    while p < n and arr_items[p][0] <= limit:
        value, position = arr_items[p]
        # 자료구조에 position 반영
        p += 1

    # 현재 자료구조로 [left, right] 질의 처리
    answer[idx] = 0
```

이 방식은 펜윅 트리나 세그먼트 트리와 자주 연결된다.

## 5. Mo's Algorithm

Mo's algorithm은 구간 쿼리를 특정 순서로 정렬해서, 현재 구간을 조금씩 움직이며 답을 구하는 오프라인 기법이다.

```python
block = int(n ** 0.5)

queries.sort(key=lambda x: (x[0] // block, x[1]))
```

기본 아이디어:

```text
현재 구간 [cur_l, cur_r]을 유지한다.
다음 쿼리 구간에 맞게 왼쪽/오른쪽 포인터를 움직인다.
원소가 추가되거나 제거될 때 현재 답을 갱신한다.
```

뼈대:

```python
cur_l = 0
cur_r = -1
answer = [0] * q

for left, right, idx in queries:
    while cur_l > left:
        cur_l -= 1
        add(cur_l)

    while cur_r < right:
        cur_r += 1
        add(cur_r)

    while cur_l < left:
        remove(cur_l)
        cur_l += 1

    while cur_r > right:
        remove(cur_r)
        cur_r -= 1

    answer[idx] = current_answer
```

## 6. 병렬 이분 탐색

병렬 이분 탐색은 여러 쿼리의 답을 동시에 이분 탐색하는 오프라인 기법이다.

보통 다음 조건에서 사용한다.

- 쿼리마다 최소로 만족하는 시점이나 값을 찾아야 한다.
- 이벤트를 시간순으로 적용할 수 있다.
- 각 쿼리의 판정을 자료구조로 빠르게 할 수 있다.

처음 공부할 때는 이름만 알아두고, 정렬 + 펜윅 트리 방식과 Mo's algorithm을 먼저 익히는 편이 좋다.

## 7. 오프라인 쿼리에서 자주 쓰는 자료구조

| 자료구조 | 사용 이유 |
| --- | --- |
| Fenwick Tree | 점 갱신, 구간 합 |
| Segment Tree | 구간 질의와 갱신 |
| Disjoint Set | 시간 역순 처리, 연결성 |
| Heap | 우선순위 유지 |
| Counter | 현재 구간의 개수 관리 |

## 8. 주의할 점

### 쿼리 순서가 의미 있는 문제

이전 쿼리의 결과가 다음 쿼리에 영향을 주면 오프라인 처리가 불가능할 수 있다.

### 원래 인덱스 저장

쿼리를 정렬하면 출력 순서가 바뀐다. 반드시 원래 인덱스를 저장해야 한다.

```python
queries.append((condition, left, right, idx))
```

### 구간 기준 통일

Mo's algorithm에서는 `[left, right]`인지 `[left, right)`인지 처음부터 정해야 한다.

## 9. 관련 알고리즘

- 정렬
- 스위핑
- 좌표 압축
- 펜윅 트리
- 세그먼트 트리
- Mo's algorithm

## 10. 정리

오프라인 쿼리는 쿼리를 더 좋은 순서로 바꿔 처리하는 전략이다.

핵심은 쿼리를 정렬해도 되는 문제인지 확인하고, 정렬 후에도 답을 원래 순서대로 복원할 수 있게 인덱스를 저장하는 것이다.
