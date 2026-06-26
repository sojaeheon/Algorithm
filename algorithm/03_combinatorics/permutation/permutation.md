# Permutation

순열은 여러 원소 중 일부 또는 전체를 **순서를 고려해서** 나열하는 것이다.

```text
[1, 2]와 [2, 1]은 다른 순열이다.
```

## 1. 언제 쓰는가

- 배치 순서가 결과에 영향을 줄 때
- 모든 순서를 시도해야 할 때
- 사람을 줄 세우는 문제
- 연산자 순서 정하기
- 경로 순서 정하기
- `N`이 작아서 완전 탐색이 가능할 때

문제에서 "순서대로 나열", "배열", "모든 순서", "방문 순서" 같은 표현이 나오면 순열을 생각한다.

## 2. 경우의 수

`N`개 중 `R`개를 뽑아 순서 있게 나열하면:

```text
NPr = N! / (N - R)!
```

예를 들어 5개 중 3개를 순서 있게 고르면:

```text
5P3 = 5 * 4 * 3 = 60
```

순열은 경우의 수가 매우 빠르게 커지므로 `N` 범위를 반드시 확인해야 한다.

## 3. itertools 사용

Python에서는 `itertools.permutations`를 사용할 수 있다.

```python
from itertools import permutations

arr = [1, 2, 3]

for case in permutations(arr, 2):
    print(case)
```

출력:

```text
(1, 2)
(1, 3)
(2, 1)
(2, 3)
(3, 1)
(3, 2)
```

## 4. 직접 구현

백트래킹으로 순열을 직접 만들 수 있다.

```python
def make_perm(path, used):
    if len(path) == r:
        print(path)
        return

    for i in range(n):
        if used[i]:
            continue

        used[i] = True
        path.append(arr[i])
        make_perm(path, used)
        path.pop()
        used[i] = False


arr = [1, 2, 3]
n = len(arr)
r = 2
make_perm([], [False] * n)
```

## 5. 코드 핵심

| 요소 | 의미 |
| --- | --- |
| `path` | 현재까지 만든 순열 |
| `used` | 이미 사용한 원소 표시 |
| `len(path) == r` | 순열 하나 완성 |

재귀 호출 후에는 반드시 원래 상태로 되돌려야 한다.

```python
path.pop()
used[i] = False
```

## 6. 중복 원소가 있는 순열

입력에 중복 값이 있으면 같은 순열이 여러 번 나올 수 있다.

```python
arr = [1, 1, 2]
```

중복 결과를 제거하려면 정렬 후 같은 깊이에서 같은 값을 다시 선택하지 않게 처리한다.

```python
arr.sort()

def make_perm(path, used):
    if len(path) == r:
        print(path)
        return

    prev = None

    for i in range(n):
        if used[i]:
            continue
        if prev == arr[i]:
            continue

        prev = arr[i]
        used[i] = True
        path.append(arr[i])
        make_perm(path, used)
        path.pop()
        used[i] = False
```

## 7. 순열과 DFS

순열 생성은 DFS와 같다.

```text
현재 위치에 어떤 값을 놓을지 선택
다음 위치로 이동
끝까지 채우면 하나의 경우 완성
돌아와서 다른 선택 시도
```

## 8. 자주 하는 실수

### 상태 복구 누락

```python
path.append(arr[i])
make_perm(path, used)
path.pop()
```

`pop()`을 빼먹으면 다음 경우에 이전 선택이 남는다.

### `used` 복구 누락

```python
used[i] = True
make_perm(path, used)
used[i] = False
```

### 순열이 아닌 조합 문제를 순열로 푸는 경우

순서가 중요하지 않은데 순열로 풀면 경우의 수가 필요 이상으로 커진다.

## 9. 정리

순열은 순서가 중요한 모든 배치를 확인할 때 사용한다. 핵심은 `used`로 이미 선택한 원소를 관리하고, 재귀가 끝난 뒤 상태를 원래대로 되돌리는 것이다.
