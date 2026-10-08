# Programmers 72413 합승 택시 요금
# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/72413
# 난이도: LV3
# 분류: graph, shortest_path, dijkstra, heap
# 핵심:
#   두 사람이 어느 지점까지 함께 이동한 뒤 각자의 목적지로 갈라진다고 생각한다.
#   s, a, b에서 다익스트라를 실행한 뒤 가능한 모든 합승 종료 지점을 확인한다.
# 시간 복잡도: O((N + E) log N)
# 공간 복잡도: O(N + E)



# 1. 문제 이해
# - 입력:
#   n: 지점의 개수
#   s: 두 사람의 출발 지점
#   a: A의 도착 지점
#   b: B의 도착 지점
#   fares: [지점1, 지점2, 택시 요금] 목록
# - 출력:
#   두 사람이 각자의 목적지까지 이동하는 데 필요한 최소 택시 요금
# - 조건:
#   택시 요금은 양방향에서 같다.
#   처음부터 따로 이동하는 경우도 가능하다.


# 2. 아이디어
# - 합승이 끝나는 지점을 split이라고 한다.
# - 전체 요금은 다음 세 구간의 최단 거리 합이다.
#   s -> split: 두 사람이 함께 이동
#   split -> a: A가 혼자 이동
#   split -> b: B가 혼자 이동
# - split을 1번부터 n번까지 모두 확인해 가장 작은 합을 찾는다.
# - 노선이 양방향이므로 a -> split의 최단 거리는 split -> a와 같다.
# - 따라서 s, a, b에서 시작하는 최단 거리 배열 3개만 있으면 된다.


# 3. 풀이 계획
# 1) fares로 양방향 인접 리스트를 만든다.
# 2) 다익스트라 함수를 작성한다.
# 3) s, a, b에서 각각 다익스트라를 실행한다.
# 4) 모든 합승 종료 지점 split에 대해
#    from_s[split] + from_a[split] + from_b[split]을 계산한다.
# 5) 가장 작은 요금을 반환한다.

import heapq

def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n + 1)]

    for start, end, fare in fares:
        graph[start].append((end, fare))
        graph[end].append((start, fare))

    def dijkstra(start):
        INF = float("inf")
        distance = [INF] * (n + 1)
        distance[start] = 0

        heap = [(0, start)]

        while heap:
            current_fare, current_node = heapq.heappop(heap)

            # 이미 더 저렴한 경로를 찾은 뒤 남은 오래된 항목은 무시한다.
            if current_fare != distance[current_node]:
                continue

            for next_node, move_fare in graph[current_node]:
                next_fare = current_fare + move_fare

                if next_fare < distance[next_node]:
                    distance[next_node] = next_fare
                    heapq.heappush(heap, (next_fare, next_node))

        return distance

    from_s = dijkstra(s)
    from_a = dijkstra(a)
    from_b = dijkstra(b)

    answer = float("inf")

    for split in range(1, n + 1):
        total_fare = from_s[split] + from_a[split] + from_b[split]
        answer = min(answer, total_fare)

    return answer


if __name__ == "__main__":
    print(
        solution(
            6,
            4,
            6,
            2,
            [
                [4, 1, 10],
                [3, 5, 24],
                [5, 6, 2],
                [3, 1, 41],
                [5, 1, 24],
                [4, 6, 50],
                [2, 4, 66],
                [2, 3, 22],
                [1, 6, 25],
            ],
        )
    )  # 예상: 82

    print(
        solution(
            7,
            3,
            4,
            1,
            [
                [5, 7, 9],
                [4, 6, 4],
                [3, 6, 1],
                [3, 2, 3],
                [2, 1, 6],
            ],
        )
    )  # 예상: 14

    print(
        solution(
            6,
            4,
            5,
            6,
            [
                [2, 6, 6],
                [6, 3, 7],
                [4, 6, 7],
                [6, 5, 11],
                [2, 5, 12],
                [5, 3, 20],
                [2, 4, 8],
                [4, 3, 9],
            ],
        )
    )  # 예상: 18
