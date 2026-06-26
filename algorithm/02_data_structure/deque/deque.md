# Deque

덱(deque)은 양쪽 끝에서 삽입과 삭제가 모두 가능한 자료구조이다. Double-ended queue의 줄임말이다.

## 1. 언제 쓰는가

- 앞과 뒤에서 모두 값을 넣거나 빼야 한다.
- 슬라이딩 윈도우 최솟값/최댓값을 구한다.
- 0-1 BFS를 구현한다.
- 큐와 스택 기능이 모두 필요하다.

## 2. Python 사용법

```python
from collections import deque

dq = deque()

dq.append(1)
dq.appendleft(0)
dq.append(2)

print(dq.popleft())  # 0
print(dq.pop())      # 2
```

## 3. 기본 연산

| 연산 | Python |
| --- | --- |
| 오른쪽 삽입 | `dq.append(x)` |
| 왼쪽 삽입 | `dq.appendleft(x)` |
| 오른쪽 삭제 | `dq.pop()` |
| 왼쪽 삭제 | `dq.popleft()` |
| 회전 | `dq.rotate(k)` |

## 4. 슬라이딩 윈도우 최솟값

덱에는 값이 아니라 인덱스를 저장한다.

```python
from collections import deque

def sliding_min(arr, k):
    dq = deque()
    result = []

    for i, x in enumerate(arr):
        while dq and dq[0] <= i - k:
            dq.popleft()

        while dq and arr[dq[-1]] >= x:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(arr[dq[0]])

    return result
```

## 5. 0-1 BFS

간선 비용이 0 또는 1일 때 사용할 수 있다.

```python
from collections import deque

dist[start] = 0
dq = deque([start])

while dq:
    now = dq.popleft()

    for nxt, cost in graph[now]:
        if dist[nxt] > dist[now] + cost:
            dist[nxt] = dist[now] + cost

            if cost == 0:
                dq.appendleft(nxt)
            else:
                dq.append(nxt)
```

## 6. 자주 하는 실수

- 슬라이딩 윈도우에서 오래된 인덱스를 제거하지 않는 경우
- 덱에 값만 저장해 위치를 알 수 없게 되는 경우
- 0-1 BFS를 일반 BFS처럼 처리하는 경우

## 7. 정리

덱은 양쪽 끝을 모두 빠르게 다룰 수 있는 자료구조이다. 슬라이딩 윈도우와 0-1 BFS에서 특히 강하다.
