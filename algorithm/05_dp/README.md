# Dynamic Programming

DP는 작은 문제의 답을 저장하고 재사용해 큰 문제의 답을 구하는 방법입니다.

## 문서

| 주제 | 문서 | 핵심 |
| --- | --- | --- |
| DP 기본 | [dp.md](dp.md) | 상태 정의, 초기값, 점화식 |
| 메모이제이션 | [memoization.md](memoization/memoization.md) | 재귀 결과 저장 |
| 배낭 DP | [knapsack.md](knapsack/knapsack.md) | 제한 용량 안에서 선택 |
| LIS | [lis.md](lis/lis.md) | 가장 긴 증가 부분 수열 |
| 트리 DP | [tree_dp.md](tree_dp/tree_dp.md) | 서브트리 정보를 부모로 올림 |
| 비트마스크 DP | [bitmask_dp.md](bitmask_dp/bitmask_dp.md) | 집합 상태를 비트로 표현 |

## DP 풀이 순서

1. `dp` 상태의 의미를 문장으로 쓴다.
2. 초기값을 정한다.
3. 점화식을 세운다.
4. 반복 순서를 정한다.
5. 정답이 어느 위치에 있는지 확인한다.

## 자주 하는 실수

- 상태 정의 없이 코드부터 작성
- 초기값 누락
- 반복 방향 실수
- `dp[n]`이 항상 답이라고 가정
