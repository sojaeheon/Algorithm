# Circular Queue

원형 큐는 고정 크기 배열을 원처럼 사용해서 큐를 구현하는 자료구조이다.

배열의 끝에 도달하면 다시 처음 위치로 돌아가며, 인덱스는 나머지 연산으로 순환시킨다.

## 1. 왜 원형 큐를 쓰는가

일반 배열 큐에서 앞쪽 원소를 계속 제거하면 앞 공간이 비지만 재사용하기 어렵다.

원형 큐는 `front`와 `rear`를 순환시켜 빈 공간을 다시 사용할 수 있게 한다.

## 2. 핵심 변수

| 변수 | 의미 |
| --- | --- |
| `front` | 값을 꺼낼 위치 |
| `rear` | 값을 넣을 위치 |
| `size` | 배열 크기 |

인덱스 이동:

```python
rear = (rear + 1) % size
front = (front + 1) % size
```

## 3. 한 칸 비워두는 방식

원형 큐에서는 보통 한 칸을 비워두어 empty와 full을 구분한다.

```python
def is_empty():
    return front == rear


def is_full():
    return (rear + 1) % size == front
```

## 4. 클래스 구현

```python
class CircularQueue:
    def __init__(self, capacity):
        self.size = capacity + 1
        self.queue = [None] * self.size
        self.front = 0
        self.rear = 0

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def push(self, value):
        if self.is_full():
            raise IndexError("queue is full")

        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % self.size

    def pop(self):
        if self.is_empty():
            raise IndexError("queue is empty")

        value = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.size
        return value
```

## 5. 동작 예시

```text
size = 5
front = 0, rear = 0

push A -> rear = 1
push B -> rear = 2
pop    -> front = 1
push C -> rear = 3
```

배열 끝에 도달하면 `% size`로 다시 0부터 사용한다.

## 6. deque와 비교

Python 문제 풀이에서는 직접 원형 큐를 구현하기보다 `collections.deque`를 쓰는 경우가 많다.

```python
from collections import deque

q = deque()
q.append(1)
q.popleft()
```

원형 큐는 자료구조 구현 원리를 공부할 때 중요하다.

## 7. 자주 하는 실수

### full과 empty 조건이 같아지는 경우

한 칸을 비워두지 않으면 `front == rear`가 empty인지 full인지 구분하기 어렵다.

### 나머지 연산 누락

```python
rear = (rear + 1) % size
```

### 실제 저장 가능 크기

한 칸을 비워두는 방식에서는 배열 크기가 `size`이면 실제 저장 가능 개수는 `size - 1`개이다.

## 8. 정리

원형 큐는 고정 크기 배열을 효율적으로 재사용하는 큐 구현 방식이다. 핵심은 `front`, `rear`, `% size`, 그리고 full/empty 조건을 정확히 구분하는 것이다.
