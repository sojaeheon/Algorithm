# Rolling Hash

Rolling Hash는 문자열을 숫자 해시로 바꾸어 부분 문자열 비교를 빠르게 하는 기법이다.

문자열 자체를 매번 비교하면 길이만큼 시간이 걸리지만, 해시를 미리 계산해두면 부분 문자열의 해시를 빠르게 구할 수 있다.

## 1. 언제 쓰는가

- 부분 문자열 비교가 많다.
- 문자열 매칭을 빠르게 처리하고 싶다.
- 같은 길이의 구간들이 같은지 여러 번 확인해야 한다.
- 긴 문자열에서 중복 부분 문자열을 찾고 싶다.

## 2. 핵심 아이디어

문자열을 진법 표현처럼 본다.

```text
"abc" = a * BASE^2 + b * BASE + c
```

이를 누적해서 저장하면 원하는 구간의 해시를 빠르게 계산할 수 있다.

## 3. 기본 코드

```python
MOD = 1_000_000_007
BASE = 911382323

s = input().strip()
n = len(s)

prefix = [0] * (n + 1)
power = [1] * (n + 1)

for i, ch in enumerate(s):
    prefix[i + 1] = (prefix[i] * BASE + ord(ch)) % MOD
    power[i + 1] = (power[i] * BASE) % MOD


def get_hash(left, right):
    return (prefix[right] - prefix[left] * power[right - left]) % MOD
```

`get_hash(left, right)`는 `s[left:right]`의 해시를 반환한다.

## 4. 구간 해시 비교

```python
hash1 = get_hash(l1, r1)
hash2 = get_hash(l2, r2)

if hash1 == hash2:
    print("same maybe")
```

해시가 같으면 문자열이 같을 가능성이 높지만, 충돌 가능성은 있다.

## 5. 충돌

서로 다른 문자열이 같은 해시를 가질 수 있다. 이를 해시 충돌이라고 한다.

충돌을 줄이는 방법:

- 서로 다른 MOD 두 개 사용
- BASE와 MOD를 적절히 선택
- 해시가 같을 때 실제 문자열로 한 번 더 검증

## 6. Double Hash

```python
MOD1 = 1_000_000_007
MOD2 = 1_000_000_009
BASE = 911382323
```

두 해시를 튜플로 비교한다.

```python
if hash1_a == hash2_a and hash1_b == hash2_b:
    pass
```

## 7. 복잡도

| 작업 | 복잡도 |
| --- | --- |
| 전처리 | `O(N)` |
| 구간 해시 | `O(1)` |
| 비교 | `O(1)` |

## 8. 자주 하는 실수

### 음수 모듈러

Python은 `% MOD`를 하면 양수로 정리되지만, 다른 언어에서는 음수 처리를 조심해야 한다.

```python
(prefix[right] - prefix[left] * power[right - left]) % MOD
```

### right 범위

위 코드의 `right`는 포함하지 않는 끝 인덱스이다.

```text
s[left:right]
```

### 충돌 가능성 무시

정확성이 매우 중요한 문제에서는 double hash 또는 실제 문자열 검증을 고려한다.

## 9. 정리

Rolling Hash는 부분 문자열을 숫자로 바꾸어 빠르게 비교하는 기법이다. 빠르지만 충돌 가능성이 있으므로 문제의 요구 정확도에 맞게 보완해야 한다.
