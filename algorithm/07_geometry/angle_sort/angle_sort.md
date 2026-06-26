# Angle Sort

각도 정렬은 기준점에서 다른 점이나 벡터들을 반시계 방향 또는 시계 방향 순서로 정렬하는 기법이다.

## 1. 언제 쓰는가

- 한 점을 기준으로 주변 점의 순서가 필요하다.
- 벡터를 방향 순서대로 처리해야 한다.
- 볼록 껍질, 선분 처리, 기하 스위핑에서 방향 정렬이 필요하다.
- 같은 기준점에서 점들을 회전 순서로 봐야 한다.

## 2. atan2 사용

가장 간단한 방법은 `math.atan2`를 사용하는 것이다.

```python
import math

base = (0, 0)

points.sort(key=lambda p: math.atan2(p[1] - base[1], p[0] - base[0]))
```

`atan2(y, x)`는 벡터가 x축과 이루는 각도를 반환한다.

## 3. 거리 기준 추가

같은 각도에 있는 점이 여러 개라면 거리 기준을 추가할 수 있다.

```python
def dist2(p):
    dx = p[0] - base[0]
    dy = p[1] - base[1]
    return dx * dx + dy * dy


points.sort(key=lambda p: (
    math.atan2(p[1] - base[1], p[0] - base[0]),
    dist2(p),
))
```

## 4. atan2의 장단점

장점:

- 구현이 간단하다.
- 대부분의 일반적인 정렬 문제에서 충분하다.

단점:

- 부동소수점 오차 가능성이 있다.
- 정밀한 기하 문제에서는 정수 기반 비교가 더 안전할 수 있다.

## 5. 사분면 + CCW 방식

정수 연산으로 각도 순서를 비교하려면 사분면과 외적을 사용한다.

```python
from functools import cmp_to_key


def half(p):
    x, y = p
    return 0 if y > 0 or (y == 0 and x >= 0) else 1


def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]


def compare(a, b):
    ha = half(a)
    hb = half(b)

    if ha != hb:
        return ha - hb

    c = cross(a, b)
    if c > 0:
        return -1
    if c < 0:
        return 1

    da = a[0] * a[0] + a[1] * a[1]
    db = b[0] * b[0] + b[1] * b[1]
    return da - db


vectors.sort(key=cmp_to_key(compare))
```

## 6. 기준점 기준 벡터 변환

점 자체를 정렬하기 전에 기준점에서의 벡터로 바꾸어 생각한다.

```python
vectors = [(p[0] - base[0], p[1] - base[1]) for p in points]
```

## 7. 자주 하는 실수

### 기준점 빼기 누락

각도는 원점 기준이 아니라 기준점 기준일 수 있다.

```python
p[0] - base[0], p[1] - base[1]
```

### 같은 각도 처리

같은 방향의 점들은 거리 기준 정렬이 필요할 수 있다.

### atan2 범위

`atan2`는 보통 `-pi`부터 `pi` 범위의 값을 반환한다. 원하는 시작 방향이 다르면 조정이 필요할 수 있다.

## 8. 정리

각도 정렬은 기준점에서 점들을 방향 순서대로 나열하는 기법이다. 간단한 문제는 `atan2`, 정밀한 정수 기하 문제는 CCW 기반 비교를 사용한다.
