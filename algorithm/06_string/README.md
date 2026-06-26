# String

문자열 검색, 접두사 구조, 부분 문자열 비교 알고리즘을 정리합니다.

## 문서

| 주제 | 문서 | 핵심 |
| --- | --- | --- |
| 문자열 매칭 | [string_matching.md](string_matching/string_matching.md) | 패턴 검색 방법 선택 |
| KMP | [kmp.md](kmp/kmp.md) | 접두사/접미사를 이용한 선형 검색 |
| Trie | [trie.md](trie/trie.md) | 문자열 집합과 접두사 검색 |
| Rolling Hash | [rolling_hash.md](rolling_hash/rolling_hash.md) | 부분 문자열 빠른 비교 |

## 선택 기준

| 상황 | 추천 |
| --- | --- |
| 문자열이 짧음 | 단순 비교 |
| 긴 text에서 하나의 pattern 검색 | KMP |
| 많은 단어와 접두사 검색 | Trie |
| 부분 문자열 비교가 많음 | Rolling Hash |
