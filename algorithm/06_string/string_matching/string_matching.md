# String Matching

문자열 매칭은 긴 문자열 안에서 특정 패턴이 등장하는지, 등장한다면 어디에 등장하는지 찾는 문제이다.

## 1. 문제 형태

```text
text = "ababcababd"
pattern = "ababd"
```

찾고 싶은 것:

- 패턴이 존재하는가?
- 패턴이 몇 번 등장하는가?
- 패턴이 등장하는 모든 위치는 어디인가?

## 2. 단순 매칭

가장 단순한 방법은 모든 시작 위치에서 패턴과 비교하는 것이다.

```python
def find_pattern(text, pattern):
    n = len(text)
    m = len(pattern)
    result = []

    for i in range(n - m + 1):
        if text[i:i + m] == pattern:
            result.append(i)

    return result
```

## 3. 단순 매칭 복잡도

슬라이싱 비교는 패턴 길이만큼 비용이 든다.

```text
시작 위치 N개 * 패턴 길이 M
```

따라서 최악의 경우 `O(NM)`이다.

문자열이 짧으면 충분하지만, 길이가 크면 KMP 같은 알고리즘이 필요하다.

## 4. 알고리즘 선택

| 상황 | 방법 |
| --- | --- |
| 문자열이 짧다 | 단순 비교 |
| 하나의 긴 패턴을 찾는다 | KMP |
| 많은 단어를 저장하고 접두사를 찾는다 | Trie |
| 부분 문자열 비교가 많다 | Rolling Hash |
| 여러 패턴을 동시에 찾는다 | Aho-Corasick |

## 5. Python 기본 기능

단순 존재 확인:

```python
if pattern in text:
    print("found")
```

첫 위치:

```python
idx = text.find(pattern)
```

개수:

```python
count = text.count(pattern)
```

단, `count`는 겹치는 등장을 세지 않는다.

```python
"aaaa".count("aa")  # 2
```

겹치는 등장까지 세려면 직접 탐색하거나 KMP를 사용한다.

## 6. 겹치는 패턴

```text
text = "aaaa"
pattern = "aa"
```

겹쳐서 세면 위치는 `0, 1, 2`로 총 3번이다.

단순 반복으로 세려면:

```python
count = 0

for i in range(len(text) - len(pattern) + 1):
    if text[i:i + len(pattern)] == pattern:
        count += 1
```

## 7. 인덱스 주의

알고리즘 코드는 보통 0-index 위치를 다룬다.

문제에서 1-index로 출력하라고 하면 `+1`을 해야 한다.

```python
print(position + 1)
```

## 8. 자주 하는 실수

### 슬라이싱 비용 무시

```python
text[i:i + m] == pattern
```

이 비교는 `O(M)`이다.

### 겹치는 등장 처리

`str.count()`는 겹치는 패턴을 모두 세지 않는다.

### 대소문자와 공백

문제에서 대소문자를 구분하는지, 공백도 문자열에 포함되는지 확인한다.

## 9. 정리

문자열 매칭은 입력 크기와 요구사항에 따라 방법을 고르는 것이 중요하다. 짧으면 단순 비교, 길면 KMP, 접두사 구조가 중요하면 Trie, 부분 문자열 비교가 많으면 Rolling Hash를 고려한다.
