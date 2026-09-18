# Programmers 프로세스
# 난이도: LV2
# 분류: queue, simulation
# 핵심:
#   대기 큐에서 현재 프로세스를 꺼낸 뒤,
#   더 높은 우선순위가 남아 있으면 다시 뒤에 넣는 과정을 시뮬레이션한다.
# 시간 복잡도: O(N^2)
# 공간 복잡도: O(N)

from collections import deque


# 1. 문제 이해
# - 입력:
#   priorities: 각 프로세스의 우선순위 목록
#   location: 내가 알고 싶은 프로세스의 처음 위치
# - 출력:
#   location 위치에 있던 프로세스가 몇 번째로 실행되는지
# - 조건:
#   숫자가 클수록 우선순위가 높다.


# 2. 아이디어
# - 각 프로세스를 (처음 위치, 우선순위) 형태로 큐에 넣는다.
# - 큐의 맨 앞 프로세스를 꺼낸다.
# - 남은 프로세스 중 더 높은 우선순위가 있으면 다시 큐 뒤에 넣는다.
# - 그렇지 않으면 실행 순서를 1 증가시킨다.
# - 실행한 프로세스의 처음 위치가 location이면 그 순서를 반환한다.


# 3. 풀이 계획
# 1) priorities를 돌며 (index, priority)를 큐에 넣는다.
# 2) 실행 순서 answer를 0으로 둔다.
# 3) 큐가 빌 때까지 맨 앞 프로세스를 꺼낸다.
# 4) 더 높은 우선순위가 남아 있으면 다시 뒤에 넣는다.
# 5) 실행 가능하면 answer를 증가시키고, location인지 확인한다.


def solution(priorities, location):
    answer = 0
    processes = deque()

    for index, priority in enumerate(priorities):
        processes.append((index, priority))

    while processes:
        current_index, current_priority = processes.popleft()

        has_higher_priority = False

        for _, priority in processes:
            if priority > current_priority:
                has_higher_priority = True
                break

        if has_higher_priority:
            processes.append((current_index, current_priority))
        else:
            answer += 1

            if current_index == location:
                return answer

    return answer


if __name__ == "__main__":
    # 프로그래머스식으로 연습할 때는 아래처럼 직접 테스트한다.
    print(solution([2, 1, 3, 2], 2))  # 예상: 1
    print(solution([1, 1, 9, 1, 1, 1], 0))  # 예상: 5
