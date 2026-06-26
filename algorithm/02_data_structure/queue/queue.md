# Queue

큐는 먼저 들어간 데이터가 먼저 나오는 자료구조이다. FIFO(First In, First Out) 구조라고 한다.

## 1. 언제 쓰는가

- 먼저 들어온 순서대로 처리해야 한다.
- BFS를 구현한다.
- 대기열, 작업 처리 순서, 시뮬레이션 문제가 나온다.
- 현재 단계의 원소를 처리하고 다음 단계로 확장한다.

## 2. Python 구현

Python에서는 `collections.deque`를 큐로 사용한다.

```python
from collections import deque

q = deque()

q.append(1)
q.append(2)

print(q.popleft())  # 1
print(q.popleft())  # 2
```

## 3. 기본 연산

| 연산 | Python |
| --- | --- |
| 삽입 | `q.append(x)` |
| 삭제 | `q.popleft()` |
| 맨 앞 확인 | `q[0]` |
| 비었는지 확인 | `not q` |
| 크기 | `len(q)` |

## 4. 리스트를 큐로 쓰면 안 되는 이유

```python
arr.pop(0)
```

리스트의 앞에서 값을 빼면 뒤 원소들을 모두 앞으로 당겨야 하므로 `O(N)`이다.

`deque.popleft()`는 `O(1)`이다.

## 5. BFS 기본 형태

```python
from collections import deque

def bfs(start):
    q = deque([start])
    visited[start] = True

    while q:
        now = q.popleft()

        for nxt in graph[now]:
            if visited[nxt]:
                continue

            visited[nxt] = True
            q.append(nxt)
```

## 6. 복잡도

| 연산 | 복잡도 |
| --- | --- |
| `append` | `O(1)` |
| `popleft` | `O(1)` |
| `q[0]` | `O(1)` |

## 7. 자주 하는 실수

- `list.pop(0)`을 큐처럼 사용하는 경우
- 빈 큐에서 `popleft()`를 호출하는 경우
- BFS에서 큐에 넣을 때 방문 처리를 하지 않아 중복 삽입되는 경우

## 8. 정리

큐는 먼저 들어온 것을 먼저 처리하는 자료구조이다. BFS와 시뮬레이션 문제에서 가장 자주 사용한다.
