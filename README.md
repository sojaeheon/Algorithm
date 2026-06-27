# Algorithm

자료구조와 알고리즘 개념을 정리하고, JUNGOL 문제 풀이를 함께 관리하는 저장소입니다.

## 바로가기

- [알고리즘 전체 목차](algorithm/README.md)
- [문제 풀이 폴더](problems/README.md)
- [JUNGOL 풀이 기록](problems/jungol/README.md)
- [알고리즘 문서 템플릿](algorithm/00_templates/algorithm_note_template.md)
- [시간복잡도와 공간복잡도](algorithm/00_templates/complexity/complexity.md)
- [Python 입출력 템플릿](algorithm/00_templates/python_io/python_io.md)
- [STL 대응표](algorithm/00_templates/stl/stl.md)

## 폴더 구조

```text
algorithm/
  00_templates/        # 템플릿, Python 입출력, STL 대응표
  01_basic/            # 정렬, 이분 탐색, 재귀, 비트 연산, 버킷
  02_data_structure/   # 스택, 큐, 덱, 해시, 힙, 트리, 구간 질의
  03_combinatorics/    # 순열, 조합, 부분집합
  04_graph/            # BFS, DFS, 위상 정렬, MST, 최단 경로, SCC, BCC
  05_dp/               # DP, 메모이제이션, LIS, 배낭, 트리 DP
  06_string/           # 문자열 매칭, KMP, Trie, Rolling Hash
  07_geometry/         # CCW, 각도 정렬, 볼록 껍질, 스위핑
  08_optimization/     # 좌표 압축, 오프라인 쿼리

problems/
  jungol/              # JUNGOL 문제 풀이
```

## 학습 로드맵

### 1. 풀이 기본기

- [Python 입출력](algorithm/00_templates/python_io/python_io.md)
- [시간복잡도와 공간복잡도](algorithm/00_templates/complexity/complexity.md)
- [정렬](algorithm/01_basic/sorting/sorting.md)
- [버킷](algorithm/01_basic/bucket/bucket.md)
- [이분 탐색](algorithm/01_basic/binary_search/binary_search.md)
- [재귀](algorithm/01_basic/recursion/recursion.md)
- [비트 연산](algorithm/01_basic/bit_operation/bit_operation.md)

### 2. 기본 자료구조

- [스택](algorithm/02_data_structure/stack/stack.md)
- [큐](algorithm/02_data_structure/queue/queue.md)
- [덱](algorithm/02_data_structure/deque/deque.md)
- [원형 큐](algorithm/02_data_structure/circular_queue/circular_queue.md)
- [연결 리스트](algorithm/02_data_structure/linked_list/linked_list.md)
- [해시](algorithm/02_data_structure/hash/hash.md)
- [힙](algorithm/02_data_structure/heap/heap.md)
- [BST](algorithm/02_data_structure/bst/bst.md)

### 3. 완전 탐색과 경우의 수

- [순열](algorithm/03_combinatorics/permutation/permutation.md)
- [조합](algorithm/03_combinatorics/combination/combination.md)
- [부분집합](algorithm/03_combinatorics/subset/subset.md)

### 4. 그래프 기본

- [BFS](algorithm/04_graph/bfs/bfs.md)
- [DFS](algorithm/04_graph/dfs/dfs.md)
- [위상 정렬](algorithm/04_graph/topological_sort/topological_sort.md)

### 5. 그래프 응용

- [서로소 집합](algorithm/02_data_structure/disjoint_set/disjoint_set.md)
- [최소 신장 트리](algorithm/04_graph/mst/mst.md)
- [최단 경로](algorithm/04_graph/shortest_path/shortest_path.md)
- [SCC](algorithm/04_graph/scc/scc.md)
- [BCC](algorithm/04_graph/bcc/bcc.md)
- [오일러 경로](algorithm/04_graph/euler_path/euler_path.md)
- [오일러 투어 테크닉](algorithm/04_graph/euler_tour_technique/euler_tour_technique.md)

### 6. Dynamic Programming

- [DP 기본](algorithm/05_dp/dp.md)
- [메모이제이션](algorithm/05_dp/memoization/memoization.md)
- [LIS](algorithm/05_dp/lis/lis.md)
- [배낭 DP](algorithm/05_dp/knapsack/knapsack.md)
- [트리 DP](algorithm/05_dp/tree_dp/tree_dp.md)
- [비트마스크 DP](algorithm/05_dp/bitmask_dp/bitmask_dp.md)

### 7. 구간 질의와 최적화

- [Fenwick Tree](algorithm/02_data_structure/fenwick_tree/fenwick_tree.md)
- [세그먼트 트리](algorithm/02_data_structure/segment_tree/segment_tree.md)
- [Lazy Propagation](algorithm/02_data_structure/lazy_propagation/lazy_propagation.md)
- [Sparse Table](algorithm/02_data_structure/sparse_table/sparse_table.md)
- [좌표 압축](algorithm/08_optimization/coordinate_compression/coordinate_compression.md)
- [오프라인 쿼리](algorithm/08_optimization/offline_query/offline_query.md)

### 8. 문자열

- [문자열 매칭](algorithm/06_string/string_matching/string_matching.md)
- [KMP](algorithm/06_string/kmp/kmp.md)
- [Trie](algorithm/06_string/trie/trie.md)
- [Rolling Hash](algorithm/06_string/rolling_hash/rolling_hash.md)

### 9. 기하와 스위핑

- [CCW](algorithm/07_geometry/ccw/ccw.md)
- [각도 정렬](algorithm/07_geometry/angle_sort/angle_sort.md)
- [볼록 껍질](algorithm/07_geometry/convex_hull/convex_hull.md)
- [스위핑](algorithm/07_geometry/sweeping/sweeping.md)

## 문제 풀이 기록 방식

문제 풀이 파일은 플랫폼별 폴더에 저장합니다.

```text
problems/jungol/문제번호_문제이름.py
```

풀이 파일 상단에는 문제 정보와 핵심 아이디어를 남깁니다.

```python
# JUNGOL 0000 문제이름
# 분류:
# 핵심:
# 시간 복잡도:
```

문제를 풀고 나면 관련 알고리즘 문서에도 문제 번호와 핵심 아이디어를 추가합니다.
