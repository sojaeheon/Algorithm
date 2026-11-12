
import heapq

def solution(board):
    n = len(board)
    INF = float('inf')

    # 상, 하, 좌, 우
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    # dist[y][x][방향]
    dist = [[[INF] * 4 for _ in range(n)] for _ in range(n)]

    # 비용, y, x, 이전 방향
    heap = [(0, 0, 0, -1)]

    while heap:
        cost, y, x, direction = heapq.heappop(heap)

        # 기존에 더 저렴한 경로가 있다면 무시
        if direction != -1 and cost > dist[y][x][direction]:
            continue

        # 도착
        if y == n - 1 and x == n - 1:
            return cost

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            # 범위 확인
            if not (0 <= ny < n and 0 <= nx < n):
                continue

            # 벽 확인
            if board[ny][nx] == 1:
                continue

            # 이동 비용
            if direction == -1 or direction == d:
                new_cost = cost + 100
            else:
                new_cost = cost + 600

            # 최소 비용 갱신
            if new_cost < dist[ny][nx][d]:
                dist[ny][nx][d] = new_cost
                heapq.heappush(heap, (new_cost, ny, nx, d))

    return -1
