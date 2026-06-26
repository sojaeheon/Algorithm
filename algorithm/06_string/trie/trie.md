# Trie

Trie는 문자열을 문자 단위로 나누어 저장하는 트리 자료구조이다. 공통 접두사를 공유하므로 많은 문자열을 효율적으로 저장하고 검색할 수 있다.

## 1. 언제 쓰는가

- 문자열 집합을 저장해야 한다.
- 접두사 검색이 필요하다.
- 자동 완성처럼 특정 prefix로 시작하는 단어를 찾아야 한다.
- 전화번호 목록처럼 어떤 문자열이 다른 문자열의 접두사인지 확인해야 한다.
- 많은 단어를 빠르게 삽입/검색해야 한다.

## 2. 기본 구조

각 노드는 다음 정보를 가진다.

```text
children: 다음 문자로 이어지는 노드들
is_end: 이 노드에서 단어가 끝나는지 여부
```

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
```

## 3. Trie 클래스

```python
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]

        node.is_end = True

    def search(self, word):
        node = self.root

        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]

        return node.is_end

    def starts_with(self, prefix):
        node = self.root

        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]

        return True
```

## 4. 단어 검색과 접두사 검색

`search`는 단어 전체가 존재하는지 확인한다.

```python
trie.search("abc")
```

`starts_with`는 해당 접두사로 시작하는 단어가 하나라도 있는지 확인한다.

```python
trie.starts_with("ab")
```

이 둘은 다르다.

```text
저장된 단어: "abc"
search("ab") -> False
starts_with("ab") -> True
```

## 5. 접두사 충돌 확인

전화번호 목록처럼 어떤 번호가 다른 번호의 접두사인지 확인할 수 있다.

```python
def insert_and_check(word):
    node = root

    for ch in word:
        if node.is_end:
            return False

        if ch not in node.children:
            node.children[ch] = TrieNode()
        node = node.children[ch]

    if node.children:
        return False

    node.is_end = True
    return True
```

## 6. 복잡도

문자열 길이를 `L`이라고 할 때:

| 연산 | 복잡도 |
| --- | --- |
| 삽입 | `O(L)` |
| 검색 | `O(L)` |
| 접두사 검색 | `O(L)` |

## 7. 장단점

장점:

- 접두사 검색이 빠르다.
- 공통 접두사를 공유해 구조적으로 관리하기 좋다.

단점:

- 노드가 많아질 수 있어 메모리를 많이 쓴다.
- 단순 존재 확인만 필요하면 `set`이 더 간단하다.

## 8. 자주 하는 실수

### is_end 누락

단어가 어디서 끝나는지 표시하지 않으면 `abc`와 `abcd`를 구분하기 어렵다.

### 접두사와 단어 존재 혼동

`starts_with("ab")`가 참이어도 `"ab"`라는 단어가 저장된 것은 아닐 수 있다.

### set으로 충분한 문제에 Trie 사용

접두사 처리가 필요 없고 단어 존재만 보면 되는 문제는 `set`이 더 간단하다.

## 9. 정리

Trie는 문자열의 접두사 구조를 트리로 저장하는 자료구조이다. 단어 전체 검색보다 접두사 검색이 중요할 때 특히 강하다.
