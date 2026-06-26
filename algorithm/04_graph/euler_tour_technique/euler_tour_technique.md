# Euler Tour Technique

오일러 투어 테크닉은 트리에서 각 노드의 진입 시간과 탈출 시간을 기록해 서브트리 문제를 배열 구간 문제로 바꾸는 기법이다.

오일러 경로와 이름은 비슷하지만 완전히 다른 개념이다.

## 1. 언제 쓰는가

- 서브트리 전체의 합을 구해야 한다.
- 서브트리 전체에 값을 더해야 한다.
- 트리 문제를 세그먼트 트리나 펜윅 트리로 풀고 싶다.
- 어떤 노드의 서브트리를 연속된 구간으로 표현하고 싶다.

## 2. 핵심 아이디어

DFS로 트리를 순회하면서 각 노드에 들어가는 시간을 기록한다.

한 노드의 서브트리에 포함되는 노드들은 DFS 순서에서 연속된 구간을 이룬다.

```text
node x의 서브트리 = [tin[x], tout[x]]
```

## 3. 기본 코드

```python
timer = 0


def dfs(now, parent):
    global timer

    timer += 1
    tin[now] = timer

    for nxt in tree[now]:
        if nxt == parent:
            continue
        dfs(nxt, now)

    tout[now] = timer
```

초기화:

```python
tin = [0] * (n + 1)
tout = [0] * (n + 1)
dfs(1, 0)
```

## 4. 서브트리 구간

노드 `x`의 서브트리는 다음 구간이다.

```python
left = tin[x]
right = tout[x]
```

이 구간에 세그먼트 트리나 펜윅 트리를 적용할 수 있다.

## 5. 노드 값을 배열로 옮기기

```python
flat = [0] * (n + 1)

for node in range(1, n + 1):
    flat[tin[node]] = value[node]
```

이제 `flat[tin[x]:tout[x]]` 구간이 x의 서브트리 값들이다.

## 6. 서브트리 합

펜윅 트리나 세그먼트 트리로 `[tin[x], tout[x]]` 구간 합을 구하면 x의 서브트리 합이 된다.

```python
subtree_sum = query(tin[x], tout[x])
```

## 7. 주의할 점

### 트리에서만 사용

오일러 투어 테크닉은 보통 트리의 서브트리를 구간으로 바꿀 때 사용한다.

### parent 처리

무방향 트리에서는 부모로 되돌아가지 않게 해야 한다.

```python
if nxt == parent:
    continue
```

### 진입/탈출 기록 방식

문제에 따라 진입 시점만 기록하는 방식과 진입/탈출을 모두 배열에 넣는 방식이 있다. 서브트리 구간 질의는 보통 진입 시점 기준 배열을 사용한다.

## 8. 정리

오일러 투어 테크닉은 트리의 서브트리를 연속된 배열 구간으로 바꾸는 방법이다. 트리 문제를 구간 질의 자료구조와 연결할 수 있게 해주는 강력한 전처리이다.
