# Data Structure

자료구조는 데이터를 어떤 방식으로 저장하고 꺼낼지 정하는 도구입니다.

## 문서

| 주제 | 문서 | 사용 상황 |
| --- | --- | --- |
| Stack | [stack.md](stack/stack.md) | 최근 값부터 처리 |
| Queue | [queue.md](queue/queue.md) | 먼저 들어온 값부터 처리 |
| Deque | [deque.md](deque/deque.md) | 양쪽 삽입/삭제, 슬라이딩 윈도우 |
| Circular Queue | [circular_queue.md](circular_queue/circular_queue.md) | 배열 기반 큐 구현 |
| Linked List | [linked_list.md](linked_list/linked_list.md) | 노드 연결 구조 이해 |
| Hash | [hash.md](hash/hash.md) | 빠른 검색, 중복 확인, 개수 세기 |
| Heap | [heap.md](heap/heap.md) | 최솟값/최댓값 빠른 추출 |
| BST | [bst.md](bst/bst.md) | 정렬된 트리 구조 |
| Disjoint Set | [disjoint_set.md](disjoint_set/disjoint_set.md) | 집합 합치기, 연결 여부 확인 |
| Fenwick Tree | [fenwick_tree.md](fenwick_tree/fenwick_tree.md) | 점 갱신과 구간 합 |
| Segment Tree | [segment_tree.md](segment_tree/segment_tree.md) | 구간 질의와 점 갱신 |
| Lazy Propagation | [lazy_propagation.md](lazy_propagation/lazy_propagation.md) | 구간 갱신과 구간 질의 |
| Sparse Table | [sparse_table.md](sparse_table/sparse_table.md) | 정적 배열의 빠른 구간 질의 |

## 선택 기준

| 상황 | 추천 |
| --- | --- |
| 최근에 넣은 값을 먼저 처리 | Stack |
| 먼저 넣은 값을 먼저 처리 | Queue |
| 양쪽 끝을 모두 사용 | Deque |
| 가장 작은 값을 반복해서 꺼냄 | Heap |
| 존재 여부를 빠르게 확인 | Hash |
| 같은 집합인지 확인 | Disjoint Set |
| 구간 합만 빠르게 처리 | Fenwick Tree |
| 값이 바뀌는 구간 질의 | Segment Tree |
| 구간 갱신도 필요 | Lazy Propagation |
| 값이 안 바뀌는 RMQ | Sparse Table |
