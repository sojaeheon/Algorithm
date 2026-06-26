# STL

STL(Standard Template Library)은 C++에서 자주 사용하는 자료구조와 알고리즘 라이브러리이다.

이 저장소의 풀이 언어는 주로 Python이지만, 알고리즘 개념을 공부할 때 C++ STL 이름도 함께 알아두면 다른 풀이를 읽기 쉽다.

## 1. 자주 쓰는 컨테이너

| C++ STL | Python 대응 | 설명 |
| --- | --- | --- |
| `vector` | `list` | 동적 배열 |
| `stack` | `list` | LIFO |
| `queue` | `deque` | FIFO |
| `deque` | `collections.deque` | 양쪽 삽입/삭제 |
| `priority_queue` | `heapq` | 우선순위 큐 |
| `set` | `set` | 중복 없는 집합 |
| `map` | `dict` | key-value |
| `unordered_set` | `set` | 해시 집합 |
| `unordered_map` | `dict` | 해시 맵 |

## 2. 자주 쓰는 알고리즘

| C++ STL | Python |
| --- | --- |
| `sort(v.begin(), v.end())` | `arr.sort()` |
| `lower_bound` | `bisect_left` |
| `upper_bound` | `bisect_right` |
| `next_permutation` | `itertools.permutations` 또는 직접 구현 |

## 3. Python에서 자주 쓰는 모듈

```python
from collections import deque, Counter, defaultdict
from itertools import permutations, combinations
from bisect import bisect_left, bisect_right
import heapq
```

## 4. 정리

C++ STL과 Python 표준 라이브러리는 이름은 다르지만 문제 풀이에서 맡는 역할은 비슷하다. 풀이를 읽을 때 자료구조의 역할을 기준으로 이해하면 된다.
