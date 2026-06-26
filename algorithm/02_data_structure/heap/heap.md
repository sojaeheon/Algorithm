# Heap

힙은 최솟값 또는 최댓값을 빠르게 꺼내기 위한 자료구조이다. Python의 `heapq`는 기본적으로 **최소 힙**이다.

## 1. 언제 쓰는가

- 매번 가장 작은 값 또는 큰 값을 꺼내야 한다.
- 우선순위가 있는 작업을 처리해야 한다.
- 현재 후보 중 가장 비용이 작은 것을 골라야 한다.
- Dijkstra 알고리즘을 구현한다.
- Prim 알고리즘을 구현한다.
- 여러 리스트나 정렬된 데이터를 합친다.

문제에서 "가장 작은 값을 반복해서 꺼낸다", "우선순위", "최소 비용 후보" 같은 표현이 나오면 힙을 떠올린다.

## 2. 기본 사용법

```python
import heapq

heap = []

heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)

print(heapq.heappop(heap))  # 1
print(heapq.heappop(heap))  # 2
```

`heappop`은 항상 현재 힙에서 가장 작은 값을 꺼낸다.

## 3. 최댓값 꺼내기

Python은 최소 힙만 제공하므로, 최댓값을 꺼내고 싶으면 음수로 넣는다.

```python
heap = []

for x in arr:
    heapq.heappush(heap, -x)

max_value = -heapq.heappop(heap)
```

## 4. 튜플 힙

튜플을 넣으면 앞 원소부터 비교한다.

```python
heapq.heappush(heap, (cost, node))
```

이 경우 `cost`가 작은 순서대로 꺼내진다. 비용이 같으면 `node`를 비교한다.

## 5. 여러 기준 우선순위

```python
heapq.heappush(heap, (priority, time, value))
```

비교 순서:

```text
1. priority
2. time
3. value
```

## 6. 리스트를 힙으로 만들기

이미 값이 들어 있는 리스트를 힙으로 바꿀 수 있다.

```python
heapq.heapify(arr)
```

`heapify`는 `O(N)`이다.

## 7. 복잡도

| 연산 | 복잡도 |
| --- | --- |
| `heappush` | `O(log N)` |
| `heappop` | `O(log N)` |
| `heap[0]` | `O(1)` |
| `heapify` | `O(N)` |

## 8. 대표 패턴: Dijkstra

```python
heap = [(0, start)]

while heap:
    cost, now = heapq.heappop(heap)

    if dist[now] < cost:
        continue

    for nxt, weight in graph[now]:
        new_cost = cost + weight
        if new_cost < dist[nxt]:
            dist[nxt] = new_cost
            heapq.heappush(heap, (new_cost, nxt))
```

가장 비용이 작은 후보부터 처리해야 하므로 힙을 사용한다.

## 9. 자주 하는 실수

### 그냥 리스트에 append만 하는 경우

```python
heap.append(x)  # 힙 구조가 유지되지 않음
```

힙에 넣을 때는 `heappush`를 사용한다.

### 정렬과 혼동

힙 내부 리스트가 완전히 정렬되어 보장되는 것은 아니다. 최솟값은 `heap[0]`에 있다는 것만 보장된다.

### 빈 힙에서 pop

```python
if heap:
    value = heapq.heappop(heap)
```

### 최댓값 힙에서 부호 복구 누락

```python
value = -heapq.heappop(heap)
```

## 10. 정리

힙은 매 순간 가장 우선순위가 높은 값을 빠르게 꺼내는 자료구조이다. 정렬을 매번 다시 하면 느린 문제에서 힙을 사용하면 `O(log N)`으로 후보를 관리할 수 있다.
