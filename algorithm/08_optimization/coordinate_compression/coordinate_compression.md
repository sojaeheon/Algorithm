# Coordinate Compression

좌표 압축은 큰 값들의 대소 관계만 유지한 채 작은 인덱스로 바꾸는 기법이다.

값의 실제 크기보다 순서와 상대적인 위치가 중요할 때 사용한다.

## 1. 언제 쓰는가

- 좌표 값은 매우 크지만 등장하는 값의 개수는 적다.
- 큰 좌표를 배열 인덱스로 사용하고 싶다.
- 세그먼트 트리나 펜윅 트리의 인덱스로 바꾸고 싶다.
- 스위핑에서 좌표를 작은 범위로 줄이고 싶다.
- 값의 대소 관계만 필요하다.

## 2. 기본 코드

```python
arr = [1000, -3, 1000, 7]

values = sorted(set(arr))
compressed = {value: idx for idx, value in enumerate(values)}

result = [compressed[x] for x in arr]
```

결과:

```text
values = [-3, 7, 1000]
result = [2, 0, 2, 1]
```

## 3. 왜 set과 sort를 쓰는가

좌표 압축에서는 중복 좌표를 하나로 합쳐야 한다.

```python
values = sorted(set(arr))
```

그리고 정렬해야 원래 값의 대소 관계가 압축된 인덱스에도 유지된다.

```text
-3 < 7 < 1000
0 < 1 < 2
```

## 4. 1-index 압축

펜윅 트리처럼 1-index가 편한 자료구조에서는 1부터 시작하게 만들 수 있다.

```python
compressed = {value: idx + 1 for idx, value in enumerate(values)}
```

## 5. 좌표 압축 함수

```python
def compress(arr):
    values = sorted(set(arr))
    index = {value: i for i, value in enumerate(values)}
    return [index[x] for x in arr], values
```

`values`를 함께 반환하면 압축 인덱스에서 원래 좌표를 다시 확인할 수 있다.

## 6. 구간 문제에서 주의

스위핑이나 구간 길이 계산에서는 압축 인덱스 차이가 실제 길이가 아니다.

```text
좌표: [10, 100, 1000]
압축: [0, 1, 2]
```

압축 인덱스 차이:

```text
2 - 0 = 2
```

실제 좌표 차이:

```text
1000 - 10 = 990
```

길이가 필요하면 원래 좌표 배열 `values`를 사용한다.

```python
real_length = values[right_idx] - values[left_idx]
```

## 7. 여러 좌표 묶기

구간 `[left, right]`들이 주어지면 왼쪽과 오른쪽 좌표를 모두 모아야 한다.

```python
coords = []

for left, right in intervals:
    coords.append(left)
    coords.append(right)

values = sorted(set(coords))
idx = {x: i for i, x in enumerate(values)}
```

## 8. 복잡도

정렬 때문에 `O(N log N)`이다.

압축 값을 찾는 것은 dict를 사용하므로 평균 `O(1)`이다.

## 9. 자주 하는 실수

### 중복 제거 누락

`set` 없이 정렬하면 같은 값이 서로 다른 인덱스를 가질 수 있다.

### 실제 거리 계산 실수

압축 좌표는 순서만 보존한다. 거리나 길이는 원래 좌표로 계산한다.

### 필요한 좌표를 모두 넣지 않는 경우

구간 문제에서는 시작점, 끝점, 필요하면 끝점 + 1까지 넣어야 할 수 있다. 문제의 구간 포함 방식을 확인한다.

## 10. 정리

좌표 압축은 큰 좌표를 작은 인덱스로 바꾸는 전처리이다. 핵심은 대소 관계는 유지되지만 실제 거리 정보는 압축 인덱스에 남아 있지 않다는 점이다.
