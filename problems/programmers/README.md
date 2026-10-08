# 프로그래머스

프로그래머스에서 푼 문제와 아직 풀이 중인 문제를 구분해 기록합니다.

## 완료한 문제

| 문제 | 난이도 | 분류 | 핵심 |
| --- | --- | --- | --- |
| [42587 프로세스](lv2/Process.py) | LV2 | queue, simulation | 큐에서 프로세스를 꺼내 더 높은 우선순위가 남아 있으면 뒤로 보내고, 실행 순서를 센다 |
| [1844 게임 맵 최단거리](lv2/GameMapShortestPath.py) | LV2 | bfs, queue, shortest_path | 이동 비용이 모두 같은 격자에서 BFS로 도착점까지의 최소 이동 칸 수를 구한다 |
| [43162 네트워크](lv3/Network.py) | LV3 | graph, bfs, connected_component | 방문하지 않은 컴퓨터마다 BFS를 시작해 연결 요소의 개수를 센다 |
| [72413 합승 택시 요금](lv3/SharedTaxiFare.py) | LV3 | graph, dijkstra, shortest_path | 출발지와 두 목적지에서 다익스트라를 실행하고 모든 합승 종료 지점의 요금을 비교한다 |

## 미완성 문제

| 문제 | 난이도 | 현재 상태 | 다음 작업 |
| --- | --- | --- | --- |
| [12909 올바른 괄호](lv2/CorrectParentheses.py) | LV2 | 풀이 뼈대 | 스택으로 여는 괄호와 닫는 괄호의 짝 검사 |

## C++ 연습 파일

- [42587 프로세스](lv2/Process.cpp)
- [1844 게임 맵 최단거리](lv2/GameMapShortestPath.cpp)
