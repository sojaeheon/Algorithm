# Convex Hull

볼록 껍질은 주어진 점들을 모두 포함하는 가장 바깥쪽 볼록 다각형이다.

고무줄로 점들을 감싸면 고무줄이 닿는 점들이 볼록 껍질을 이룬다고 생각할 수 있다.

## 1. 언제 쓰는가

- 점 집합의 외곽선이 필요하다.
- 가장 바깥 경계만 남겨야 한다.
- 점들을 포함하는 최소 볼록 다각형을 구해야 한다.
- 회전하는 캘리퍼스 같은 기하 알고리즘의 전처리가 필요하다.

## 2. Monotone Chain

가장 구현하기 쉬운 볼록 껍질 알고리즘 중 하나이다.

흐름:

```text
1. 점들을 x, y 기준으로 정렬한다.
2. 아래 껍질(lower)을 만든다.
3. 위 껍질(upper)을 만든다.
4. 두 껍질을 합친다.
```

## 3. 코드

```python
def cross(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def convex_hull(points):
    points = sorted(set(points))

    if len(points) <= 1:
        return points

    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]
```

## 4. 조건 의미

```python
cross(lower[-2], lower[-1], p) <= 0
```

반시계 방향이 아니면 가운데 점은 볼록 껍질의 바깥 경계에 필요 없으므로 제거한다.

## 5. 일직선 위의 점 처리

일직선 위의 점을 껍질에 포함하지 않으려면:

```python
cross(...) <= 0
```

일직선 위의 점도 포함하려면:

```python
cross(...) < 0
```

문제 조건에 따라 선택해야 한다.

## 6. 중복 점 처리

중복 점은 제거하는 것이 안전하다.

```python
points = sorted(set(points))
```

## 7. 복잡도

정렬이 필요하므로 `O(N log N)`이다. 껍질을 만드는 과정은 각 점이 들어가고 나오는 횟수가 제한되어 `O(N)`이다.

## 8. 자주 하는 실수

### 일직선 포함 여부

문제에서 외곽의 모든 점을 요구하는지, 꼭짓점만 요구하는지 확인한다.

### 점이 1개 또는 2개인 경우

예외 처리를 해야 한다.

### 중복 점

중복 점을 제거하지 않으면 결과가 꼬일 수 있다.

## 9. 정리

볼록 껍질은 점 집합의 바깥 경계를 구하는 알고리즘이다. Monotone Chain은 정렬과 CCW만으로 구현할 수 있어 문제 풀이에서 자주 사용된다.
