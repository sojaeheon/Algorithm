# JUNGOL 1082 화염에서탈출
# 난이도: gold
# 분류: bfs, queue, simulation
# 핵심:
#   불이 먼저 언제 도착하는지 BFS로 계산한다.
#   그 다음 사람이 이동할 때 불보다 먼저 도착할 수 있는 칸만 이동한다.
# 시간 복잡도: O(RC)
# 공간 복잡도: O(RC)

from collections import deque
import sys


# 1. 문제 이해
# - 입력:
#   R: 행의 수
#   C: 열의 수
#   grid: 지도
# - 출력:
#   시작 위치에서 집/목적지까지 도착하는 최소 시간
#   도착할 수 없으면 문제에서 요구하는 실패 문구 출력
# - 지도 문자:
#   S: 시작 위치
#   D: 목적지
#   *: 불
#   X: 바위
#   .: 빈 칸


# 2. 아이디어
# - 불과 사람이 동시에 움직이는 문제이다.
# - 안전하게 처리하려면 불의 도착 시간을 먼저 구한다.
# - 사람이 어떤 칸에 t초에 도착하려고 할 때,
#   불이 그 칸에 t초 이하로 도착한다면 이동할 수 없다.
# - 목적지 D는 불이 번지지 않는 칸으로 처리한다.


# 3. 풀이 계획
# 1) 지도에서 시작 위치, 목적지, 불 위치들을 찾는다.
# 2) 모든 불 위치를 큐에 넣고 BFS를 돌려 fire_time을 만든다.
# 3) 시작 위치에서 사람 BFS를 돌린다.
# 4) 다음 칸이 벽이 아니고, 불보다 먼저 도착 가능하면 이동한다.
# 5) 목적지에 도착하면 시간을 반환한다.
# 6) 끝까지 도착하지 못하면 실패 값을 반환한다.


def solution(R, C, grid):
    # TODO: 문제 풀이 로직 작성
    # return answer
    pass


if __name__ == "__main__":
    input = sys.stdin.readline

    R, C = map(int, input().split())
    grid = [list(input().strip()) for _ in range(R)]

    print(solution(R, C, grid))
