# Stack

스택은 데이터를 한쪽 끝에서만 넣고 빼는 선형 자료구조이다. 가장 나중에 들어간 데이터가 가장 먼저 나오기 때문에 **LIFO(Last In, First Out)** 구조라고 한다.

쉽게 말하면 접시를 쌓아두는 방식과 비슷하다. 마지막에 올린 접시를 가장 먼저 꺼낼 수 있다.

## 1. 핵심 개념

스택에서 데이터를 넣는 연산을 `push`, 데이터를 꺼내는 연산을 `pop`이라고 한다. 스택의 가장 위에 있는 값을 `top`이라고 부른다.

```text
push(1)  -> [1]
push(2)  -> [1, 2]
push(3)  -> [1, 2, 3]
pop()    -> [1, 2]      꺼낸 값: 3
pop()    -> [1]         꺼낸 값: 2
```

가장 최근에 들어온 값부터 처리해야 한다면 스택을 떠올리면 된다.

## 2. Python에서 스택 사용하기

Python에서는 보통 `list`를 스택처럼 사용한다.

| 연산 | 설명 | Python |
| --- | --- | --- |
| push | 값 넣기 | `stack.append(x)` |
| pop | 마지막 값 꺼내기 | `stack.pop()` |
| top | 마지막 값 확인 | `stack[-1]` |
| empty | 비었는지 확인 | `not stack` |
| size | 크기 확인 | `len(stack)` |

```python
stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print(stack[-1])   # 30
print(stack.pop()) # 30
print(stack.pop()) # 20
print(stack)       # [10]
```

## 3. 시간 복잡도

Python 리스트의 끝에서 삽입하고 삭제하는 연산은 평균적으로 빠르다.

| 연산 | 시간 복잡도 |
| --- | --- |
| `append` | `O(1)` |
| `pop` | `O(1)` |
| `stack[-1]` | `O(1)` |
| `len(stack)` | `O(1)` |

주의할 점은 리스트의 앞에서 값을 빼는 `pop(0)`은 `O(N)`이다. 큐가 필요하면 `collections.deque`를 사용한다.

## 4. 스택을 떠올리는 신호

문제에서 다음 표현이나 상황이 나오면 스택을 의심해볼 수 있다.

- 가장 최근에 나온 값을 먼저 처리해야 한다.
- 괄호, 태그, 블록처럼 열고 닫는 구조가 있다.
- 이전 값들 중 아직 처리되지 않은 후보를 보관해야 한다.
- 현재 값이 나오면서 이전 값들의 답이 결정된다.
- 되돌아가기, 취소, 역순 처리 같은 흐름이 있다.
- DFS를 재귀 없이 구현해야 한다.

## 5. 대표 패턴 1: 괄호 검사

괄호 문제는 스택의 가장 기본적인 사용 예시이다.

여는 괄호가 나오면 스택에 넣고, 닫는 괄호가 나오면 스택의 맨 위와 짝이 맞는지 확인한다.

```python
def is_valid_parentheses(s):
    stack = []
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{',
    }

    for ch in s:
        if ch in '([{':
            stack.append(ch)
        else:
            if not stack:
                return False
            if stack[-1] != pairs[ch]:
                return False
            stack.pop()

    return not stack
```

### 예시

```text
s = "([])"

'(' -> push       stack: ['(']
'[' -> push       stack: ['(', '[']
']' -> '[' pop    stack: ['(']
')' -> '(' pop    stack: []
```

마지막에 스택이 비어 있으면 모든 괄호가 올바르게 닫힌 것이다.

## 6. 대표 패턴 2: 단조 스택

단조 스택은 스택 안의 값들이 증가하거나 감소하는 형태를 유지하도록 관리하는 기법이다.

주로 다음 문제에서 사용한다.

- 오른쪽에 있는 첫 번째 큰 값 찾기
- 오른쪽에 있는 첫 번째 작은 값 찾기
- 이전보다 큰 값 또는 작은 값 찾기
- 아직 답이 정해지지 않은 후보 관리

## 7. 오큰수 패턴

오큰수는 어떤 수의 오른쪽에 있으면서 그 수보다 큰 첫 번째 수를 의미한다.

```text
arr = [3, 5, 2, 7]

3의 오큰수: 5
5의 오큰수: 7
2의 오큰수: 7
7의 오큰수: 없음 -> -1
```

스택에는 **아직 오큰수를 찾지 못한 인덱스**를 저장한다.

```python
def next_greater(arr):
    n = len(arr)
    result = [-1] * n
    stack = []

    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            idx = stack.pop()
            result[idx] = arr[i]

        stack.append(i)

    return result
```

### 왜 인덱스를 저장하는가

결과 배열의 정확한 위치에 답을 넣어야 하기 때문이다.

값만 저장하면 어떤 위치의 답인지 알기 어렵다.

```python
result[idx] = arr[i]
```

이 코드를 쓰려면 `idx`가 필요하므로 스택에 인덱스를 저장한다.

### 동작 추적

```text
arr = [3, 5, 2, 7]

i = 0, arr[i] = 3
stack = []
push 0
stack = [0]

i = 1, arr[i] = 5
arr[0] = 3 < 5 이므로 result[0] = 5
pop 0
push 1
stack = [1]

i = 2, arr[i] = 2
arr[1] = 5 < 2 가 아니므로 push 2
stack = [1, 2]

i = 3, arr[i] = 7
arr[2] = 2 < 7 이므로 result[2] = 7
arr[1] = 5 < 7 이므로 result[1] = 7
push 3
stack = [3]

result = [5, 7, 7, -1]
```

## 8. 단조 스택의 시간 복잡도

겉으로 보면 `for` 안에 `while`이 있어서 `O(N^2)`처럼 보일 수 있다.

하지만 각 인덱스는 스택에 한 번 들어가고, 한 번만 나온다.

```text
push 최대 N번
pop 최대 N번
```

따라서 전체 시간 복잡도는 `O(N)`이다.

## 9. 대표 패턴 3: 스택으로 DFS 구현

재귀 DFS 대신 스택을 직접 사용할 수 있다.

```python
def dfs(start):
    stack = [start]
    visited = [False] * (n + 1)

    while stack:
        now = stack.pop()

        if visited[now]:
            continue

        visited[now] = True

        for nxt in graph[now]:
            if not visited[nxt]:
                stack.append(nxt)
```

재귀 깊이가 너무 깊어질 수 있는 문제에서는 직접 스택을 사용하는 방식이 도움이 된다.

## 10. 스택 문제 풀이 흐름

스택 문제가 의심되면 다음 순서로 생각한다.

1. 스택에 무엇을 저장할지 정한다.
2. 값 자체를 저장할지, 인덱스를 저장할지 결정한다.
3. 언제 `push`할지 정한다.
4. 언제 `pop`할지 정한다.
5. 스택에 남은 값들이 어떤 의미인지 확인한다.

특히 결과 배열에 위치별 답을 넣어야 하면 인덱스를 저장하는 경우가 많다.

## 11. 값 저장 vs 인덱스 저장

| 저장 대상 | 사용 상황 |
| --- | --- |
| 값 | 값 자체만 비교하거나 출력하면 될 때 |
| 인덱스 | 결과 배열 위치가 필요할 때 |
| 튜플 | 값과 추가 정보가 함께 필요할 때 |

```python
stack.append((value, index))
```

## 12. 자주 하는 실수

### 빈 스택 확인을 빼먹는 경우

```python
# 위험
if stack[-1] == x:
    stack.pop()
```

```python
# 안전
if stack and stack[-1] == x:
    stack.pop()
```

### `while` 대신 `if`를 쓰는 경우

단조 스택에서는 현재 값 하나가 이전 후보 여러 개의 답을 결정할 수 있다. 그래서 보통 `while`이 필요하다.

```python
while stack and arr[stack[-1]] < arr[i]:
    result[stack.pop()] = arr[i]
```

### 비교 연산을 잘못 쓰는 경우

문제에서 "큰 값"인지 "크거나 같은 값"인지 확인해야 한다.

```python
arr[stack[-1]] < arr[i]   # 현재 값이 더 클 때
arr[stack[-1]] <= arr[i]  # 현재 값이 크거나 같을 때
```

### 스택에 남은 값 처리

오큰수처럼 답이 없는 경우 `-1`로 남겨두면 된다. 하지만 문제에 따라 마지막에 스택에 남은 값을 따로 처리해야 할 수도 있다.

## 13. 관련 문제 유형

| 유형 | 핵심 아이디어 |
| --- | --- |
| 괄호 검사 | 여는 괄호 push, 닫는 괄호에서 top 확인 |
| 오큰수 | 아직 답을 찾지 못한 인덱스 저장 |
| 탑 문제 | 자신을 볼 수 있는 이전 후보 유지 |
| 히스토그램 | 높이가 증가하는 스택 유지 |
| 문자열 폭발 | 최근 문자열 조각을 스택처럼 관리 |
| DFS | 방문할 정점을 스택에 저장 |

## 14. 기본 템플릿

### 일반 스택

```python
stack = []

for x in arr:
    if condition:
        stack.append(x)
    else:
        if stack:
            stack.pop()
```

### 단조 스택

```python
stack = []

for i in range(n):
    while stack and condition(stack[-1], i):
        idx = stack.pop()
        # idx의 답을 현재 i로 결정

    stack.append(i)
```

## 15. 정리

스택은 최근에 들어온 값을 먼저 처리하는 자료구조이다. 단순 구현 문제뿐 아니라, 단조 스택처럼 이전 후보들을 효율적으로 관리하는 문제에서도 자주 등장한다.

스택 문제의 핵심은 `push`와 `pop` 자체가 아니라 **스택에 남아 있는 값들이 어떤 의미를 가지는지**를 정확히 정의하는 것이다.
