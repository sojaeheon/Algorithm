# JUNGOL 2437 Find Order
# https://jungol.co.kr/problem/2437

import sys
from collections import deque


def solution(N, words):
    # 정답에는 문서에 한 번이라도 등장한 문자만 포함한다.
    used_letters = set()

    for word in words:
        used_letters.update(word)

    # graph[a]에는 a보다 뒤에 와야 하는 문자들을 저장한다.
    # indegree[a]는 a보다 먼저 와야 하는 문자의 수이다.
    graph = {letter: set() for letter in used_letters}
    indegree = {letter: 0 for letter in used_letters}

    # 단어들이 이미 정올국의 사전순으로 주어졌으므로
    # 서로 인접한 단어를 비교해 문자 사이의 순서를 알아낸다.
    for index in range(N - 1):
        current_word = words[index]
        next_word = words[index + 1]
        limit = min(len(current_word), len(next_word))

        # 왼쪽부터 비교해서 처음으로 다른 문자를 찾는다.
        for position in range(limit):
            current_letter = current_word[position]
            next_letter = next_word[position]

            if current_letter == next_letter:
                continue

            # 앞 단어가 먼저 나왔으므로 current_letter가
            # next_letter보다 알파벳 순서상 앞에 있어야 한다.
            # set을 사용해 같은 간선의 중복 추가를 막는다.
            if next_letter not in graph[current_letter]:
                graph[current_letter].add(next_letter)
                indegree[next_letter] += 1

            # 사전순은 처음 다른 문자에서 결정되므로 비교를 끝낸다.
            break
        else:
            # for문에서 다른 문자를 발견하지 못하면 한 단어가 다른
            # 단어의 접두사이다. 긴 단어가 먼저라면 올바른 사전순이 아니다.
            # 예: abc가 ab보다 먼저 나오는 경우
            if len(current_word) > len(next_word):
                return "!"

    # 자신보다 먼저 와야 하는 문자가 없는 문자부터 위상 정렬을 시작한다.
    queue = deque(
        sorted(letter for letter in used_letters if indegree[letter] == 0)
    )
    order = []
    has_multiple_orders = False

    while queue:
        # 지금 선택할 수 있는 문자가 두 개 이상이면 어느 것을 먼저
        # 선택해도 되므로 알파벳 순서를 하나로 결정할 수 없다.
        if len(queue) > 1:
            has_multiple_orders = True

        current_letter = queue.popleft()
        order.append(current_letter)

        # current_letter를 순서에 넣었으므로, 그 뒤에 오는 문자들의
        # 진입 차수를 하나씩 줄인다.
        for next_letter in sorted(graph[current_letter]):
            indegree[next_letter] -= 1

            # 앞에 와야 할 문자를 모두 처리했다면 다음 후보가 된다.
            if indegree[next_letter] == 0:
                queue.append(next_letter)

    # 일부 문자를 처리하지 못했다면 문자 관계에 순환이 존재한다.
    # 예: a -> b, b -> a
    if len(order) != len(used_letters):
        return "!"

    # 순환은 없지만 선택지가 두 개 이상이었던 순간이 있다면
    # 가능한 알파벳 순서가 여러 개이다.
    if has_multiple_orders:
        return "?"

    # 모든 순간에 선택할 문자가 정확히 하나였다면 유일한 순서이다.
    return "".join(order)


if __name__ == "__main__":
    input = sys.stdin.readline

    # 정올 버전은 여러 테스트 케이스를 한 번에 입력받는다.
    T = int(input())
    answers = []

    for _ in range(T):
        N = int(input())
        words = [input().strip() for _ in range(N)]
        answers.append(solution(N, words))

    print(*answers, sep="\n")
