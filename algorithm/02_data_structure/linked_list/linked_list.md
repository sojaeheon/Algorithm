# Linked List

연결 리스트는 각 노드가 값과 다음 노드의 위치를 함께 저장하는 자료구조이다.

배열은 값들이 연속된 공간에 저장되지만, 연결 리스트는 노드들이 포인터 또는 참조로 이어져 있다.

## 1. 기본 구조

단일 연결 리스트의 노드는 보통 다음 두 정보를 가진다.

```text
value: 현재 노드의 값
next: 다음 노드
```

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
```

## 2. 언제 쓰는가

- 자료구조 구현 문제에서 노드 연결을 다룰 때
- 중간 삽입/삭제 원리를 이해해야 할 때
- 포인터, 참조 구조를 공부할 때
- 배열과 연결 구조의 차이를 비교할 때

Python 코딩 테스트에서는 직접 연결 리스트를 구현하는 경우보다 `list`, `deque`, 인덱스 배열로 해결하는 경우가 더 많다.

## 3. 노드 연결

```python
a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c

head = a
```

구조:

```text
1 -> 2 -> 3 -> None
```

## 4. 순회

```python
cur = head

while cur is not None:
    print(cur.value)
    cur = cur.next
```

## 5. 맨 앞 삽입

```python
new_node = Node(0)
new_node.next = head
head = new_node
```

구조:

```text
0 -> 1 -> 2 -> 3
```

## 6. 중간 삽입

`prev` 노드 뒤에 새 노드를 넣는다.

```python
new_node = Node(10)
new_node.next = prev.next
prev.next = new_node
```

순서가 중요하다. `prev.next`를 먼저 바꾸면 원래 뒤 노드를 잃어버릴 수 있다.

## 7. 삭제

`prev` 다음 노드를 삭제한다.

```python
target = prev.next
prev.next = target.next
```

## 8. 배열과 비교

| 구분 | 배열 | 연결 리스트 |
| --- | --- | --- |
| 인덱스 접근 | 빠름 `O(1)` | 느림 `O(N)` |
| 맨 뒤 삽입 | 보통 빠름 | tail 없으면 느림 |
| 중간 삽입/삭제 | 위치 찾은 뒤에도 이동 비용 있음 | 노드만 알면 연결 변경은 빠름 |
| 메모리 | 값 중심 | next 저장 공간 필요 |

## 9. 이중 연결 리스트

이중 연결 리스트는 이전 노드와 다음 노드를 모두 저장한다.

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
```

양방향 이동이 가능하지만 구현이 더 복잡하다.

## 10. 자주 하는 실수

### 연결 순서 실수

삽입할 때는 새 노드가 먼저 뒤쪽을 가리키게 한 뒤, 앞 노드가 새 노드를 가리키게 한다.

```python
new_node.next = prev.next
prev.next = new_node
```

### head 변경 누락

맨 앞에 삽입하거나 맨 앞을 삭제할 때는 `head`가 바뀔 수 있다.

### None 확인 누락

마지막 노드의 `next`는 `None`이다.

## 11. 정리

연결 리스트는 인덱스 접근보다 노드 간 연결 변경에 초점을 둔 자료구조이다. Python 문제 풀이에서는 직접 구현 빈도는 낮지만, 포인터와 자료구조의 기본 원리를 이해하는 데 중요하다.
