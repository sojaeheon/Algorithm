# Hash

해시는 값을 빠르게 찾기 위해 key를 기반으로 데이터를 저장하는 자료구조이다. Python에서는 `set`과 `dict`를 주로 사용한다.

## 1. 언제 쓰는가

- 중복을 확인해야 한다.
- 어떤 값이 존재하는지 빠르게 알아야 한다.
- 값의 개수를 세야 한다.
- key와 value를 연결해서 저장해야 한다.
- 리스트에서 `in` 검색을 반복하면 느릴 때

## 2. set

`set`은 중복 없는 값의 모음이다.

```python
seen = set()

seen.add(3)
seen.add(5)

if 3 in seen:
    print("exists")
```

## 3. dict

`dict`는 key와 value를 연결한다.

```python
score = {}

score["kim"] = 90
score["lee"] = 80

print(score["kim"])
```

## 4. 개수 세기

```python
count = {}

for x in arr:
    count[x] = count.get(x, 0) + 1
```

`collections.Counter`를 사용할 수도 있다.

```python
from collections import Counter

count = Counter(arr)
```

## 5. defaultdict

초기값 처리가 번거로울 때 사용한다.

```python
from collections import defaultdict

graph = defaultdict(list)

graph[a].append(b)
```

개수 세기에도 사용할 수 있다.

```python
count = defaultdict(int)

for x in arr:
    count[x] += 1
```

## 6. 복잡도

평균적으로 삽입, 삭제, 검색은 `O(1)`이다.

| 연산 | 평균 복잡도 |
| --- | --- |
| 삽입 | `O(1)` |
| 삭제 | `O(1)` |
| 검색 | `O(1)` |

## 7. 리스트 검색과 비교

리스트에서 `x in arr`는 `O(N)`이다.

```python
if x in arr:
    pass
```

이 검사를 많이 반복하면 느리다. 존재 여부만 필요하면 `set`으로 바꾼다.

```python
arr_set = set(arr)

if x in arr_set:
    pass
```

## 8. key로 사용할 수 있는 값

`dict`와 `set`의 key는 변하지 않는 값이어야 한다.

사용 가능:

- `int`
- `str`
- `tuple`

사용 불가:

- `list`
- `dict`
- `set`

리스트를 key로 쓰고 싶으면 튜플로 바꾼다.

```python
key = tuple([1, 2, 3])
```

## 9. 대표 패턴

### 중복 제거

```python
unique = list(set(arr))
```

순서를 유지하고 싶으면:

```python
unique = []
seen = set()

for x in arr:
    if x in seen:
        continue
    seen.add(x)
    unique.append(x)
```

### 두 수의 합

```python
seen = set()

for x in arr:
    if target - x in seen:
        print("found")
        break
    seen.add(x)
```

## 10. 자주 하는 실수

### 순서가 필요한데 set 사용

`set`은 순서를 보장하는 용도로 쓰면 안 된다. 정렬된 결과가 필요하면 `sorted()`를 사용한다.

### 없는 key 접근

```python
count[x] += 1  # x가 없으면 에러
```

다음처럼 처리한다.

```python
count[x] = count.get(x, 0) + 1
```

또는 `defaultdict(int)`를 사용한다.

### 리스트를 key로 사용

```python
# 불가능
dict_key = [1, 2]
```

```python
# 가능
dict_key = (1, 2)
```

## 11. 정리

해시는 빠른 검색과 개수 세기에 강하다. 문제에서 존재 여부, 중복, 빈도, key-value 관계가 보이면 `set`, `dict`, `Counter`를 먼저 떠올린다.
