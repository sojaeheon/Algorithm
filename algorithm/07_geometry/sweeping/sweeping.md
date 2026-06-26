# Sweeping

스위핑은 좌표, 시간, 이벤트를 한 기준으로 정렬한 뒤 한 방향으로 훑으면서 상태를 갱신하는 기법이다.

말 그대로 왼쪽에서 오른쪽으로 빗자루로 쓸듯이 처리한다고 생각하면 된다.

## 1. 언제 쓰는가

다음 상황에서 스위핑을 떠올릴 수 있다.

- 구간이 많이 주어진다.
- 시작점과 끝점이 있다.
- 어느 시점에 몇 개가 겹치는지 구해야 한다.
- 전체 덮인 길이를 구해야 한다.
- 직사각형, 선분, 점 이벤트를 좌표 순서대로 처리해야 한다.
- 현재 상태를 유지하면서 다음 사건으로 이동할 수 있다.

## 2. 핵심 아이디어

스위핑은 보통 다음 순서로 푼다.

1. 사건을 만든다.
2. 사건을 정렬한다.
3. 왼쪽에서 오른쪽으로 순회한다.
4. 현재 상태를 갱신한다.
5. 상태를 이용해 답을 갱신한다.

## 3. 구간 겹침 개수

구간 `[start, end)`가 여러 개 있을 때 동시에 겹치는 최대 개수를 구한다.

```python
events = []

for start, end in intervals:
    events.append((start, 1))
    events.append((end, -1))

events.sort()

cur = 0
answer = 0

for _, delta in events:
    cur += delta
    answer = max(answer, cur)
```

## 4. 시작과 끝이 같은 경우

스위핑에서 가장 중요한 디테일은 같은 좌표에서 어떤 이벤트를 먼저 처리할지이다.

예를 들어 구간을 `[start, end)`로 보면 끝점은 포함하지 않는다.

```text
[1, 3), [3, 5)
```

이 두 구간은 겹치지 않는다. 따라서 같은 좌표에서는 끝 이벤트를 먼저 처리해야 한다.

```python
events.append((start, 1))
events.append((end, -1))
events.sort()
```

Python 튜플 정렬에서는 좌표가 같으면 두 번째 값이 작은 순서가 먼저 온다. `-1`이 `1`보다 작으므로 끝 이벤트가 먼저 처리된다.

반대로 닫힌 구간 `[start, end]`로 보고 끝점도 겹친다고 처리해야 하면 시작 이벤트를 먼저 처리하도록 이벤트 값을 조정한다.

## 5. 덮인 총 길이 구하기

여러 구간이 덮는 전체 길이를 구할 수 있다.

```python
events = []

for start, end in intervals:
    events.append((start, 1))
    events.append((end, -1))

events.sort()

cur = 0
prev = events[0][0]
total = 0

for x, delta in events:
    if cur > 0:
        total += x - prev

    cur += delta
    prev = x
```

`cur > 0`이면 이전 좌표부터 현재 좌표까지는 하나 이상의 구간이 덮고 있다는 뜻이다.

## 6. 좌표 압축과 함께 쓰기

좌표가 매우 크지만 등장하는 좌표 수가 적으면 좌표 압축을 사용할 수 있다.

```python
points = []

for start, end in intervals:
    points.append(start)
    points.append(end)

points = sorted(set(points))
idx = {x: i for i, x in enumerate(points)}
```

좌표 압축을 사용할 때 실제 길이가 필요하면 압축된 인덱스 차이가 아니라 원래 좌표 차이를 사용해야 한다.

## 7. 우선순위 큐와 함께 쓰기

회의실 개수처럼 현재 진행 중인 구간의 종료 시간을 관리할 때 힙을 함께 쓸 수 있다.

```python
import heapq

intervals.sort()
heap = []

for start, end in intervals:
    while heap and heap[0] <= start:
        heapq.heappop(heap)

    heapq.heappush(heap, end)
    answer = max(answer, len(heap))
```

## 8. 복잡도

이벤트를 정렬하므로 보통 `O(N log N)`이다.

상태 갱신에 세그먼트 트리나 힙을 사용하면 추가로 `log N`이 붙을 수 있다.

## 9. 자주 하는 실수

### 이벤트 순서 처리 실수

같은 좌표에서 시작을 먼저 처리할지, 끝을 먼저 처리할지는 문제 조건에 따라 달라진다.

### 좌표 압축 후 길이 계산 실수

```python
# 잘못된 생각
length = compressed_right - compressed_left
```

압축 인덱스 차이는 실제 길이가 아니다. 실제 좌표 배열을 따로 사용해야 한다.

### 닫힌 구간과 반열린 구간 혼동

```text
[start, end]  끝 포함
[start, end)  끝 미포함
```

문제에서 겹침 기준을 정확히 읽어야 한다.

## 10. 관련 알고리즘

- 정렬
- 좌표 압축
- 힙
- 세그먼트 트리
- 오프라인 쿼리

## 11. 정리

스위핑은 모든 것을 한 번에 보지 않고, 사건이 일어나는 순서대로 상태를 갱신하는 기법이다.

핵심은 "무엇을 이벤트로 만들 것인가"와 "같은 위치의 이벤트 순서를 어떻게 정할 것인가"이다.
