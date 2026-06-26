# Geometry

좌표, 방향, 선분, 다각형을 다루는 기하 알고리즘을 정리합니다.

## 문서

| 주제 | 문서 | 핵심 |
| --- | --- | --- |
| CCW | [ccw.md](ccw/ccw.md) | 세 점의 방향 판단 |
| 각도 정렬 | [angle_sort.md](angle_sort/angle_sort.md) | 기준점에서 방향 순서 정렬 |
| 볼록 껍질 | [convex_hull.md](convex_hull/convex_hull.md) | 점 집합의 외곽선 |
| 스위핑 | [sweeping.md](sweeping/sweeping.md) | 이벤트를 정렬해 순서대로 처리 |

## 주의할 점

- 가능하면 정수 연산을 유지한다.
- 일직선, 끝점 접촉, 중복 점을 따로 확인한다.
- `float` 비교가 필요한 경우 오차를 고려한다.
