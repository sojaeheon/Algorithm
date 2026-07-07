# JUNGOL 1459 숫자고르기
# 티어: gold
# 분류: dfs, graph, cycle
# 핵심:
#   위칸 숫자 i에서 아래칸 숫자 numbers[i]로 이동한다고 생각한다.
#   어떤 시작점에서 출발해 다시 시작점으로 돌아올 수 있으면,
#   그 숫자는 선택 가능한 숫자이다.
# 시간 복잡도: O(N^2)
#   시작점을 1번부터 N번까지 모두 잡고,
#   각 시작점마다 최악의 경우 N개의 숫자를 따라갈 수 있다.
# 공간 복잡도: O(N)
#   시작점마다 크기 N의 visited 배열을 사용하고,
#   numbers와 answer도 최대 N개까지 저장한다.


# 1. 문제 이해
# - 입력:
#   N: 숫자의 개수
#   numbers[i]: i번 위칸 숫자 아래에 적힌 숫자
# - 출력:
#   첫 줄: 고른 숫자의 개수
#   이후 줄: 고른 숫자를 오름차순으로 한 줄에 하나씩 출력
# - 구해야 하는 것:
#   선택한 위칸 숫자 집합과 아래칸 숫자 집합이 같아지는 최대 집합
# - 조건:
#   1 <= N <= 100


# 2. 아이디어
# - i -> numbers[i] 로 이동하는 그래프로 본다.
# - start에서 출발해서 numbers를 계속 따라간다.
# - 이동 중 다시 start를 만나면 start는 정답에 포함될 수 있다.
# - 모든 숫자를 start로 한 번씩 검사한다.


# 3. 구현 계획
# 1) 1번부터 N번까지 각각 시작점으로 둔다.
# 2) 시작점마다 방문 배열을 새로 만들고 numbers를 따라간다.
# 3) 따라가다가 start를 다시 만나면 정답에 추가한다.
# 4) 정답 개수와 정답 숫자들을 출력한다.


def solution(N, numbers):
    answer = []

    for start in range(1, N + 1):
        visited = [False] * (N + 1)
        current = start

        while not visited[current]:
            visited[current] = True
            current = numbers[current]

            if current == start:
                answer.append(start)
                break

    return answer


if __name__ == "__main__":
    N = int(input())
    numbers = [0]

    for _ in range(N):
        numbers.append(int(input()))

    answer = solution(N, numbers)

    print(len(answer))
    for number in answer:
        print(number)
