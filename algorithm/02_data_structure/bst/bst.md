# Binary Search Tree

이진 탐색 트리(BST)는 왼쪽 자식은 현재 노드보다 작고, 오른쪽 자식은 현재 노드보다 큰 값을 가지는 이진 트리이다.

## 1. 핵심 규칙

모든 노드에서 다음 조건이 성립한다.

```text
left subtree < current node < right subtree
```

이 규칙 덕분에 탐색할 때 한쪽 서브트리를 버릴 수 있다.

## 2. 언제 쓰는가

- 정렬된 구조와 트리 탐색을 함께 이해할 때
- 삽입, 검색, 삭제가 있는 자료구조를 공부할 때
- 중위 순회 결과가 정렬된다는 성질을 사용할 때
- 균형 이진 탐색 트리의 기반 개념을 익힐 때

Python 표준 라이브러리에는 C++의 `set`, `map`처럼 균형 BST가 바로 제공되지는 않는다.

## 3. 노드 구조

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```

## 4. 탐색

```python
def search(node, target):
    if node is None:
        return False

    if node.value == target:
        return True

    if target < node.value:
        return search(node.left, target)

    return search(node.right, target)
```

## 5. 삽입

```python
def insert(node, value):
    if node is None:
        return Node(value)

    if value < node.value:
        node.left = insert(node.left, value)
    else:
        node.right = insert(node.right, value)

    return node
```

중복 값을 허용할지 말지는 문제 조건에 따라 정한다. 위 코드는 중복 값을 오른쪽에 넣는다.

## 6. 중위 순회

BST를 중위 순회하면 값이 오름차순으로 나온다.

```python
def inorder(node):
    if node is None:
        return

    inorder(node.left)
    print(node.value)
    inorder(node.right)
```

## 7. 최솟값과 최댓값

가장 왼쪽 노드가 최솟값이고, 가장 오른쪽 노드가 최댓값이다.

```python
def find_min(node):
    while node.left is not None:
        node = node.left
    return node.value


def find_max(node):
    while node.right is not None:
        node = node.right
    return node.value
```

## 8. 복잡도

| 상황 | 탐색/삽입 |
| --- | --- |
| 균형 잡힌 경우 | `O(log N)` |
| 한쪽으로 치우친 경우 | `O(N)` |

정렬된 데이터를 순서대로 삽입하면 트리가 한쪽으로 길어질 수 있다.

```text
1 -> 2 -> 3 -> 4 -> 5
```

이 경우 사실상 연결 리스트처럼 동작한다.

## 9. BST와 이분 탐색

BST는 트리 구조에서 이분 탐색과 비슷한 판단을 한다.

```text
target < current -> 왼쪽
target > current -> 오른쪽
```

하지만 배열 이분 탐색은 정렬된 배열이 필요하고, BST는 노드 연결 구조를 사용한다.

## 10. 자주 하는 실수

### 균형을 항상 보장한다고 생각하는 경우

일반 BST는 균형을 보장하지 않는다. 최악의 경우 `O(N)`이 된다.

### 중복 처리 기준 누락

중복 값을 허용하지 않을지, 왼쪽/오른쪽 어디에 둘지 정해야 한다.

### 삭제 구현의 복잡성

BST 삭제는 자식이 0개, 1개, 2개인 경우를 나누어야 해서 삽입보다 어렵다. 처음에는 탐색, 삽입, 순회부터 익히는 것이 좋다.

## 11. 정리

BST는 정렬 규칙을 가진 이진 트리이다. 중위 순회가 정렬 결과를 만든다는 점과, 균형이 깨지면 성능이 나빠진다는 점이 핵심이다.
