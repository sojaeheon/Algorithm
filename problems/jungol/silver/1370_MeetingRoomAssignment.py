# JUNGOL 1370 회의실 배정
# 난이도: silver
# 분류: greedy, sorting
# 핵심:
#   끝나는 시간이 빠른 회의부터 선택하면 더 많은 회의를 배정할 수 있다.
# 시간 복잡도: O(N log N)
# 공간 복잡도: O(N)

import sys


# 1. 문제 이해
# - 입력:
#   N: 회의의 수
#   meetings: (회의 번호, 시작 시간, 끝나는 시간) 목록
# - 출력:
#   한 회의실에서 진행할 수 있는 회의의 최대 개수
#   선택한 회의 번호를 시간대순으로 출력
# - 조건:
#   종료 시간과 시작 시간이 같은 경우는 겹치지 않는다.
#   답이 여러 가지이면 아무거나 출력해도 된다.


# 2. 아이디어
# - 회의를 끝나는 시간 기준으로 정렬한다.
# - 끝나는 시간이 같으면 시작 시간이 빠른 순서로 정렬한다.
# - 현재 회의의 시작 시간이 마지막으로 선택한 회의의 종료 시간 이상이면 선택한다.


# 3. 풀이 계획
# 1) 회의 목록을 입력받는다.
# 2) (끝나는 시간, 시작 시간) 기준으로 정렬한다.
# 3) 마지막으로 선택한 회의의 종료 시간을 저장한다.
# 4) 현재 회의의 시작 시간이 마지막 종료 시간 이상이면 선택한다.


def solution(N, meetings):
    # 끝나는 시간이 빠른 회의부터 선택해야 뒤에 더 많은 회의를 넣을 수 있다.
    meetings.sort(key=lambda x: (x[2], x[1]))

    selected = []
    last_end_time = 0

    for meeting_number, start_time, end_time in meetings:
        if start_time >= last_end_time:
            selected.append(meeting_number)
            last_end_time = end_time

    return selected


if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input())

    meetings = []
    for _ in range(N):
        meeting_number, start_time, end_time = map(int, input().split())
        meetings.append((meeting_number, start_time, end_time))

    selected = solution(N, meetings)

    print(len(selected))
    print(*selected)
