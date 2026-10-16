# Programmers 더 맵게
# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42626
# 난이도: LV2
# 분류: heap, priority_queue, greedy
# 핵심:
#   가장 맵지 않은 음식 두 개를 반복해서 꺼내 섞어야 하므로 최소 힙을 사용한다.
# 시간 복잡도: O(N log N)
# 공간 복잡도: O(N)

import heapq


# 1. 문제 이해
# - 입력:
#   scoville: 각 음식의 스코빌 지수 목록
#   K: 모든 음식이 도달해야 하는 최소 스코빌 지수
# - 섞는 방법:
#   가장 맵지 않은 음식 + (두 번째로 맵지 않은 음식 * 2)
# - 출력:
#   모든 음식의 스코빌 지수를 K 이상으로 만드는 최소 횟수
#   만들 수 없다면 -1


# 2. 아이디어
# - 가장 작은 값 두 개를 빠르게 꺼내기 위해 최소 힙을 사용한다.
# - 힙의 최솟값이 K 이상이 될 때까지 두 음식을 섞는다.
# - 최솟값이 K보다 작은데 음식이 하나뿐이면 더 섞을 수 없으므로 -1이다.


# 3. 풀이 계획
# 1) scoville을 최소 힙으로 만든다.
# 2) 힙의 최솟값이 K보다 작은 동안 반복한다.
# 3) 가장 작은 값 두 개를 꺼내 공식에 따라 섞는다.
# 4) 섞은 값을 힙에 넣고 횟수를 증가시킨다.
# 5) 성공하면 횟수, 불가능하면 -1을 반환한다.

import heapq

def solution(scoville, K):
    # TODO: 최소 힙을 이용해 필요한 최소 혼합 횟수를 구한다.
    hp = []

    answer = 0
    
    for s in scoville:
        heapq.heappush(hp,s)

    while hp[0] < K:
        if len(hp) < 2:
            return -1
        answer += 1

        first = heapq.heappop(hp)
        second = heapq.heappop(hp)

        mix_food = first + second * 2

        heapq.heappush(hp,mix_food)

    return answer


    

if __name__ == "__main__":
    print(solution([1, 2, 3, 9, 10, 12], 7))  # 예상: 2
    print(solution([10, 12], 7))  # 예상: 0
    print(solution([0, 0], 1))  # 예상: -1
