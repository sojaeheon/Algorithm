# KMP

KMP는 긴 문자열 `text` 안에서 패턴 문자열 `pattern`이 등장하는 위치를 `O(N + M)`에 찾는 문자열 매칭 알고리즘이다.

단순 비교는 불일치가 생기면 다음 위치에서 다시 처음부터 비교하지만, KMP는 패턴 안의 접두사/접미사 정보를 이용해 비교 위치를 효율적으로 이동한다.

## 1. 언제 쓰는가

- 긴 문자열에서 특정 패턴을 찾아야 한다.
- 패턴 검색을 여러 위치에서 빠르게 해야 한다.
- `N`, `M`이 커서 단순 비교 `O(NM)`이 불가능하다.
- 접두사와 접미사 정보가 필요한 문제가 나온다.

## 2. 핵심 아이디어

패턴에서 이미 비교한 부분을 버리지 않고 재사용한다.

예를 들어 패턴의 앞부분과 뒷부분이 같은 구조라면, 불일치가 발생했을 때 패턴을 처음부터 다시 보지 않아도 된다.

이를 위해 `lps` 배열을 만든다.

```text
lps[i] = pattern[0:i+1]에서 접두사와 접미사가 일치하는 최대 길이
```

단, 문자열 전체 자기 자신은 제외한다.

## 3. lps 배열 만들기

```python
def build_lps(pattern):
    lps = [0] * len(pattern)
    j = 0

    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]

        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j

    return lps
```

## 4. KMP 검색

```python
def kmp(text, pattern):
    lps = build_lps(pattern)
    result = []
    j = 0

    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = lps[j - 1]

        if text[i] == pattern[j]:
            if j == len(pattern) - 1:
                result.append(i - len(pattern) + 1)
                j = lps[j]
            else:
                j += 1

    return result
```

## 5. 검색 결과 위치

위 코드는 0-index 위치를 반환한다.

문제에서 1-index 출력을 요구하면 다음처럼 바꾼다.

```python
result.append(i - len(pattern) + 2)
```

## 6. 예시

```text
text = "ababcababd"
pattern = "ababd"
```

KMP는 중간에 불일치가 발생해도 `lps`를 이용해 패턴의 비교 위치를 이동한다. 이미 맞았던 접두사/접미사 정보를 재사용하기 때문에 전체 시간은 선형이다.

## 7. 복잡도

| 작업 | 복잡도 |
| --- | --- |
| lps 생성 | `O(M)` |
| 검색 | `O(N)` |
| 전체 | `O(N + M)` |

## 8. 자주 하는 실수

### 패턴을 찾은 뒤 j 처리

패턴을 찾은 뒤에도 겹쳐서 등장할 수 있으므로 `j = lps[j]`로 이어서 탐색한다.

```python
j = lps[j]
```

### 0-index와 1-index 혼동

문제 출력 조건을 확인한다.

### 빈 패턴 처리

일반적인 알고리즘 문제에서는 패턴 길이가 1 이상으로 주어지지만, 직접 함수로 만들 때는 빈 패턴 예외를 고려한다.

## 9. 정리

KMP의 핵심은 불일치가 생겼을 때 패턴을 얼마나 이동할지 `lps` 배열로 미리 계산하는 것이다. 접두사와 접미사의 일치 길이를 이용해 문자열 검색을 선형 시간에 처리한다.
