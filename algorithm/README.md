# Algorithm Notes

알고리즘 개념을 문제 풀이에 다시 사용할 수 있도록 정리한 공간입니다.

## 분류

| 폴더 | 내용 |
| --- | --- |
| `00_templates` | 문서 템플릿, 공통 작성 규칙 |
| `01_basic` | 정렬, 이분 탐색, 재귀, 비트 연산 |
| `02_data_structure` | 스택, 큐, 해시, 힙, 트리, 구간 질의 자료구조 |
| `03_combinatorics` | 순열, 조합, 부분집합 |
| `04_graph` | BFS, DFS, 위상 정렬, MST, 최단 경로, SCC, BCC |
| `05_dp` | DP, 메모이제이션, LIS, 배낭, 트리 DP, 비트마스크 DP |
| `06_string` | 문자열 매칭, KMP, Trie, Rolling Hash |
| `07_geometry` | CCW, 각도 정렬, 볼록 껍질, 스위핑 |
| `08_optimization` | 좌표 압축, 오프라인 쿼리 |

## Basic

- [정렬](01_basic/sorting/sorting.md)
- [이분 탐색](01_basic/binary_search/binary_search.md)
- [재귀](01_basic/recursion/recursion.md)
- [비트 연산](01_basic/bit_operation/bit_operation.md)

## Data Structure

- [스택](02_data_structure/stack/stack.md)
- [원형 큐](02_data_structure/circular_queue/circular_queue.md)
- [연결 리스트](02_data_structure/linked_list/linked_list.md)
- [해시](02_data_structure/hash/hash.md)
- [힙](02_data_structure/heap/heap.md)
- [BST](02_data_structure/bst/bst.md)
- [서로소 집합](02_data_structure/disjoint_set/disjoint_set.md)
- [세그먼트 트리](02_data_structure/segment_tree/segment_tree.md)
- [Lazy Propagation](02_data_structure/lazy_propagation/lazy_propagation.md)
- [Sparse Table](02_data_structure/sparse_table/sparse_table.md)

## Combinatorics

- [순열](03_combinatorics/permutation/permutation.md)
- [조합](03_combinatorics/combination/combination.md)
- [부분집합](03_combinatorics/subset/subset.md)

## Graph

- [BFS](04_graph/bfs/bfs.md)
- [DFS](04_graph/dfs/dfs.md)
- [위상 정렬](04_graph/topological_sort/topological_sort.md)
- [최소 신장 트리](04_graph/mst/mst.md)
- [최단 경로](04_graph/shortest_path/shortest_path.md)
- [오일러 경로](04_graph/euler_path/euler_path.md)
- [오일러 투어 테크닉](04_graph/euler_tour_technique/euler_tour_technique.md)
- [SCC](04_graph/scc/scc.md)
- [BCC](04_graph/bcc/bcc.md)

## DP

- [DP 기본](05_dp/dp.md)
- [메모이제이션](05_dp/memoization/memoization.md)
- [배낭 DP](05_dp/knapsack/knapsack.md)
- [LIS](05_dp/lis/lis.md)
- [트리 DP](05_dp/tree_dp/tree_dp.md)
- [비트마스크 DP](05_dp/bitmask_dp/bitmask_dp.md)

## String

- [문자열 매칭](06_string/string_matching/string_matching.md)
- [KMP](06_string/kmp/kmp.md)
- [Trie](06_string/trie/trie.md)
- [Rolling Hash](06_string/rolling_hash/rolling_hash.md)

## Geometry

- [CCW](07_geometry/ccw/ccw.md)
- [각도 정렬](07_geometry/angle_sort/angle_sort.md)
- [볼록 껍질](07_geometry/convex_hull/convex_hull.md)
- [스위핑](07_geometry/sweeping/sweeping.md)

## Optimization

- [좌표 압축](08_optimization/coordinate_compression/coordinate_compression.md)
- [오프라인 쿼리](08_optimization/offline_query/offline_query.md)

## 문서 작성 원칙

- 정의보다 "언제 쓰는지"를 먼저 떠올릴 수 있게 적는다.
- 코드 템플릿은 외워서 칠 수 있는 길이로 유지한다.
- 비슷한 알고리즘은 비교표를 함께 둔다.
- 문제를 풀면 관련 문서 하단에 문제 번호와 핵심 아이디어를 추가한다.
