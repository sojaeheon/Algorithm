# JUNGOL 3337 쇼핑몰
# 난이도: gold
# 분류: priority_queue, heap, sorting
# 핵심:
#   손님은 가장 빨리 비는 계산대로 들어간다.
#   계산을 마친 순서는 계산 종료 시간이 빠른 순서이고,
#   시간이 같으면 계산대 번호가 큰 순서가 먼저 나간다.
# 시간 복잡도: O(N log K + N log N)
# 공간 복잡도: O(N + K)

import heapq
import sys


# 1. 문제 이해
# - 입력:
#   N: 손님의 수
#   K: 계산대의 수
#   customers: (회원번호, 계산 시간) 목록
# - 출력:
#   계산을 마치고 나가는 순서가 i번째일 때, i * 회원번호를 모두 더한 값
# - 조건:
#   손님은 입력 순서대로 계산대에 배정된다.
#   여러 계산대가 동시에 비어 있으면 번호가 작은 계산대에 먼저 들어간다.
#   여러 손님이 동시에 계산을 마치면 번호가 큰 계산대의 손님이 먼저 나간다.


# 2. 아이디어
# - 계산대 상태를 우선순위 큐로 관리한다.
# - heap에는 (계산 종료 시간, 계산대 번호)를 넣는다.
# - 그러면 가장 빨리 비는 계산대가 먼저 나오고,
#   종료 시간이 같으면 번호가 작은 계산대가 먼저 나온다.
# - 각 손님이 계산을 끝낸 정보는 (종료 시간, 계산대 번호, 회원번호)로 저장한다.
# - 마지막에 종료 시간 오름차순, 계산대 번호 내림차순으로 정렬한다.


# 3. 풀이 계획
# 1) K개의 계산대를 (0, 계산대 번호) 상태로 heap에 넣는다.
# 2) 손님을 입력 순서대로 하나씩 확인한다.
# 3) 가장 빨리 비는 계산대를 꺼내고, 현재 손님의 종료 시간을 계산한다.
# 4) 완료 정보를 finished에 저장하고, 계산대 상태를 다시 heap에 넣는다.
# 5) finished를 퇴장 순서대로 정렬한다.
# 6) 1번 순서부터 i * 회원번호를 더한다.


# 4. 학습 메모
# - heapq에 튜플을 넣으면 앞의 값부터 차례대로 비교한다.
#   예: (5, 1), (5, 2)가 있으면 첫 번째 값 5가 같으므로 두 번째 값 1, 2를 비교한다.
#   그래서 (계산 종료 시간, 계산대 번호)를 넣으면 종료 시간이 빠른 계산대가 먼저 나오고,
#   종료 시간이 같으면 계산대 번호가 작은 계산대가 먼저 나온다.
# - enumerate(finished, start=1)는 finished를 반복하면서 순서 번호도 함께 꺼낸다.
#   start=1을 쓰면 0번째가 아니라 1번째부터 세기 때문에 퇴장 순서 계산에 맞다.
#   예: for order, info in enumerate(finished, start=1)
#       order는 퇴장 순서, info는 finished의 원소가 된다.
# - (_, _, customer_id)는 튜플에서 앞의 두 값은 사용하지 않고 회원번호만 쓰겠다는 뜻이다.


def solution(N, K, customers):
    counter_heap = []

    for counter_number in range(1, K + 1):
        heapq.heappush(counter_heap, (0, counter_number))

    finished = []

    for customer_id, payment_time in customers:
        current_time, counter_number = heapq.heappop(counter_heap)
        finish_time = current_time + payment_time

        finished.append((finish_time, counter_number, customer_id))
        heapq.heappush(counter_heap, (finish_time, counter_number))

    finished.sort(key=lambda x: (x[0], -x[1]))

    answer = 0

    for order, (_, _, customer_id) in enumerate(finished, start=1):
        answer += order * customer_id

    return answer


if __name__ == "__main__":
    input = sys.stdin.readline

    N, K = map(int, input().split())

    customers = []
    for _ in range(N):
        customer_id, payment_time = map(int, input().split())
        customers.append((customer_id, payment_time))

    print(solution(N, K, customers))
