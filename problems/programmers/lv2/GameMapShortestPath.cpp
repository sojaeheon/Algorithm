// Programmers 게임 맵 최단거리
// 난이도: LV2
// 분류: bfs, queue, shortest_path, grid
// 핵심:
//   격자에서 상하좌우로 한 칸씩 이동할 때 최단거리는 BFS로 구한다.
//   시작점에서 도착점까지 도달할 수 없으면 -1을 반환한다.
// 시간 복잡도: O(NM)
// 공간 복잡도: O(NM)

#include <bits/stdc++.h>

using namespace std;


// 1. 문제 이해
// - 입력:
//   maps: 0과 1로 이루어진 2차원 배열
//   1은 이동 가능, 0은 벽
// - 출력:
//   왼쪽 위에서 오른쪽 아래까지 가는 최단 칸 수
//   도달할 수 없으면 -1
// - 조건:
//   시작 위치는 (0, 0), 도착 위치는 (n - 1, m - 1)


// 2. 아이디어
// - 모든 이동 비용이 1로 같으므로 BFS를 사용한다.
// - queue에는 현재 위치와 현재까지의 거리를 넣는다.
// - 방문한 칸은 다시 방문하지 않는다.
// - 도착점에 처음 도달한 순간의 거리가 최단거리이다.


// 3. 풀이 계획
// 1) 행 개수 n, 열 개수 m을 구한다.
// 2) 방문 배열을 만든다.
// 3) 시작점 (0, 0)을 큐에 넣고 방문 처리한다.
// 4) 큐에서 위치를 꺼내 상하좌우를 확인한다.
// 5) 이동 가능한 칸이면 방문 처리하고 큐에 넣는다.
// 6) 도착점에 도달하면 거리 반환, 끝까지 못 가면 -1 반환.


int solution(vector<vector<int>> maps) {
    int n = maps.size();
    int m = maps[0].size();

    vector<vector<int>> distance(n, vector<int>(m, 0));
    queue<pair<int, int>> q;

    q.push({0, 0});
    distance[0][0] = 1;

    int dr[4] = {-1, 1, 0, 0};
    int dc[4] = {0, 0, -1, 1};

    while (!q.empty()) {
        int row = q.front().first;
        int col = q.front().second;
        q.pop();

        if (row == n - 1 && col == m - 1) {
            return distance[row][col];
        }

        for (int direction = 0; direction < 4; direction++) {
            int next_row = row + dr[direction];
            int next_col = col + dc[direction];

            if (next_row < 0 || next_row >= n || next_col < 0 || next_col >= m) {
                continue;
            }

            if (maps[next_row][next_col] == 0) {
                continue;
            }

            if (distance[next_row][next_col] != 0) {
                continue;
            }

            distance[next_row][next_col] = distance[row][col] + 1;
            q.push({next_row, next_col});
        }
    }

    return -1;
}


int main() {
    cout << solution({
        {1, 0, 1, 1, 1},
        {1, 0, 1, 0, 1},
        {1, 0, 1, 1, 1},
        {1, 1, 1, 0, 1},
        {0, 0, 0, 0, 1}
    }) << '\n';  // 예상: 11

    cout << solution({
        {1, 0, 1, 1, 1},
        {1, 0, 1, 0, 1},
        {1, 0, 1, 1, 1},
        {1, 1, 1, 0, 0},
        {0, 0, 0, 0, 1}
    }) << '\n';  // 예상: -1

    return 0;
}
