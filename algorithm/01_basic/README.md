# Basic

기본 알고리즘과 구현 도구를 정리하는 폴더입니다.

## 문서

| 주제 | 문서 | 핵심 |
| --- | --- | --- |
| 복잡도 | [complexity.md](../00_templates/complexity/complexity.md) | 시간복잡도와 공간복잡도를 계산한다 |
| 정렬 | [sorting.md](sorting/sorting.md) | 기준에 맞게 순서를 바꾸고 이후 탐색을 쉽게 만든다 |
| 버킷 | [bucket.md](bucket/bucket.md) | 값의 범위가 작을 때 빈도나 구간으로 처리한다 |
| 이분 탐색 | [binary_search.md](binary_search/binary_search.md) | 정렬된 범위나 정답 범위를 반씩 줄인다 |
| 그리디 | [greedy.md](greedy/greedy.md) | 매 순간 최선의 선택으로 전체 답을 만든다 |
| 재귀 | [recursion.md](recursion/recursion.md) | 문제를 더 작은 같은 형태의 문제로 나눈다 |
| 비트 연산 | [bit_operation.md](bit_operation/bit_operation.md) | 선택 상태나 방문 상태를 정수 비트로 표현한다 |

## 학습 순서

1. 시간복잡도와 공간복잡도
2. 정렬
3. 버킷
4. 이분 탐색
5. 그리디
6. 재귀
7. 비트 연산

## 문제를 풀 때 확인할 것

- 입력 크기상 `O(N^2)`이 가능한가?
- 정렬하면 문제가 쉬워지는가?
- 값의 범위가 작아서 빈도 배열을 쓸 수 있는가?
- 답을 정해놓고 가능 여부를 검사할 수 있는가?
- 현재 최선의 선택이 항상 전체 최적해로 이어지는가?
- 재귀의 기저 조건과 상태 변화가 명확한가?
- 선택 여부를 비트마스크로 표현할 수 있는가?
