# Graph

그래프 알고리즘은 정점과 간선으로 표현되는 관계를 다룹니다.

## 문서

| 주제 | 문서 | 핵심 |
| --- | --- | --- |
| BFS | [bfs.md](bfs/bfs.md) | 가중치 없는 최단 거리 |
| DFS | [dfs.md](dfs/dfs.md) | 깊이 우선 탐색, 연결성, 백트래킹 |
| 위상 정렬 | [topological_sort.md](topological_sort/topological_sort.md) | 방향 그래프의 선후 관계 |
| MST | [mst.md](mst/mst.md) | 모든 정점을 최소 비용으로 연결 |
| 최단 경로 | [shortest_path.md](shortest_path/shortest_path.md) | 정점 사이의 최소 비용 |
| 오일러 경로 | [euler_path.md](euler_path/euler_path.md) | 모든 간선을 한 번씩 사용 |
| 오일러 투어 테크닉 | [euler_tour_technique.md](euler_tour_technique/euler_tour_technique.md) | 트리의 서브트리를 구간으로 변환 |
| SCC | [scc.md](scc/scc.md) | 방향 그래프의 강한 연결 요소 |
| BCC | [bcc.md](bcc/bcc.md) | 무방향 그래프의 단절 구조 |

## 알고리즘 선택

| 상황 | 추천 |
| --- | --- |
| 가중치 없는 최단 거리 | BFS |
| 연결 요소, 깊은 탐색 | DFS |
| 작업 순서 | Topological Sort |
| 전체 연결 최소 비용 | MST |
| 한 시작점 최단 거리 | Dijkstra, Bellman-Ford |
| 모든 정점 쌍 최단 거리 | Floyd-Warshall |
| 방향 그래프의 순환 그룹 | SCC |
| 무방향 그래프의 단절점/단절선 | BCC |
