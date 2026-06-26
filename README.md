# Algorithm

자료구조와 알고리즘 개념을 정리하고, JUNGOL 문제 풀이 코드를 함께 관리하는 저장소입니다.

## 폴더 구조

```text
algorithm/
  00_templates/        # 문서 템플릿, 공통 작성 규칙
  01_basic/            # 정렬, 이분 탐색, 재귀, 비트 연산, 버킷
  02_data_structure/   # 스택, 큐, 덱, 해시, 힙, 트리, 구간 질의
  03_combinatorics/    # 순열, 조합, 부분집합
  04_graph/            # BFS, DFS, MST, 최단 경로, SCC, BCC
  05_dp/               # DP, 메모이제이션, LIS, 배낭, 트리 DP
  06_string/           # 문자열 매칭, KMP, Trie, Rolling Hash
  07_geometry/         # CCW, 각도 정렬, 볼록 껍질, 스위핑
  08_optimization/     # 좌표 압축, 오프라인 쿼리

problems/
  jungol/              # JUNGOL 문제 풀이
```

## 바로가기

- [알고리즘 정리](algorithm/README.md)
- [문제 풀이](problems/README.md)
- [JUNGOL 풀이](problems/jungol/README.md)
- [문서 템플릿](algorithm/00_templates/algorithm_note_template.md)
- [Python 입출력](algorithm/00_templates/python_io/python_io.md)
- [STL 정리](algorithm/00_templates/stl/stl.md)

## 학습 순서

1. 시간 복잡도, 입출력, 정렬, 이분 탐색, 버킷
2. 스택, 큐, 덱, 연결 리스트, 해시, 힙
3. 순열, 조합, 부분집합, 재귀, 백트래킹
4. BFS, DFS, 위상 정렬
5. 서로소 집합, MST, 최단 경로
6. DP, 메모이제이션, LIS, 배낭 DP
7. 문자열 매칭, KMP, Trie, Rolling Hash
8. Fenwick Tree, 세그먼트 트리, Lazy Propagation, Sparse Table
9. SCC, BCC, 오일러 경로, 오일러 투어 테크닉
10. CCW, 각도 정렬, 볼록 껍질, 스위핑, 좌표 압축

## 정리 방식

각 알고리즘 문서는 다음 흐름으로 정리합니다.

```text
개념
언제 쓰는가
핵심 아이디어
시간 복잡도
기본 코드
대표 패턴
자주 하는 실수
정리
```

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

## 현재 상태

핵심 알고리즘 문서 대부분은 기본 개념, 코드 템플릿, 실수 포인트까지 정리되어 있습니다. 앞으로는 JUNGOL 문제를 풀면서 각 문서의 하단에 관련 문제를 추가하고, 풀이 파일을 함께 쌓아가면 됩니다.
