# Python IO

Python 문제 풀이에서 자주 사용하는 입출력 템플릿입니다.

## 1. 빠른 입력

```python
import sys
input = sys.stdin.readline
```

## 2. 정수 하나

```python
n = int(input())
```

## 3. 한 줄 여러 정수

```python
a, b = map(int, input().split())
```

## 4. 리스트 입력

```python
arr = list(map(int, input().split()))
```

## 5. 2차원 배열

```python
board = [list(map(int, input().split())) for _ in range(n)]
```

문자 격자:

```python
board = [list(input().strip()) for _ in range(n)]
```

## 6. 출력

```python
print(answer)
print(*arr)
```

## 7. 많은 출력

```python
result = []

for x in arr:
    result.append(str(x))

print('\n'.join(result))
```

## 8. 정리

입력이 많으면 `sys.stdin.readline`을 사용하고, 출력이 많으면 문자열로 모아서 한 번에 출력한다.
