# JUNGOL 3924 Superbull
# 문제: https://jungol.co.kr/problem/3924
# 난이도: Gold 1
# 분류: graph, mst, prim, maximum_spanning_tree
# 핵심:
#   두 팀 사이의 간선 가중치는 두 팀 ID의 XOR 값이다.
#   완전 그래프의 모든 간선을 저장하지 않고 배열 기반 Prim으로 최대 신장 트리를 구한다.
# 시간 복잡도: O(N^2)
# 공간 복잡도: O(N)

import sys


# 1. 문제 이해
# - N개 팀이 토너먼트를 진행한다.
# - 두 팀 i, j가 경기하면 점수는 team_ids[i] ^ team_ids[j]이다.
# - 토너먼트 전체 경기 점수 합의 최댓값을 출력한다.


# 2. 입력
# - 첫 줄: 팀의 수 N
# - 다음 N줄: 각 팀의 ID


def solution(N, team_ids):
    selected = [False] * N
    max_score = [-1] * N
    max_score[0] = 0
    answer = 0

    for _ in range(N):
        current = -1

        # 아직 선택하지 않은 팀 중 현재 트리에 가장 큰 점수로
        # 연결할 수 있는 팀을 고른다.
        for team in range(N):
            if selected[team]:
                continue

            if current == -1 or max_score[team] > max_score[current]:
                current = team

        selected[current] = True
        answer += max_score[current]

        # 새로 선택한 팀과 나머지 팀의 XOR 점수로 최대 연결 점수를 갱신한다.
        for next_team in range(N):
            if selected[next_team]:
                continue

            score = team_ids[current] ^ team_ids[next_team]

            if score > max_score[next_team]:
                max_score[next_team] = score

    return answer


if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input())
    team_ids = [int(input()) for _ in range(N)]

    print(solution(N, team_ids))
