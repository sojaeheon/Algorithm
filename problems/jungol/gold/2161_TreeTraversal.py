# JUNGOL 2161 Tree Traversal
# https://jungol.co.kr/problem/2161

import sys


def solution(preorder, inorder):
    inorder_index = {
        node: index for index, node in enumerate(inorder)
    }
    preorder_index = 0
    postorder = []

    def build_postorder(inorder_left, inorder_right):
        nonlocal preorder_index

        if inorder_left > inorder_right:
            return

        # 전위 순회에서 가장 먼저 나오는 노드가 현재 서브트리의 루트이다.
        root = preorder[preorder_index]
        preorder_index += 1

        # 중위 순회에서 루트 왼쪽은 왼쪽 서브트리,
        # 루트 오른쪽은 오른쪽 서브트리에 해당한다.
        root_index = inorder_index[root]

        build_postorder(inorder_left, root_index - 1)
        build_postorder(root_index + 1, inorder_right)

        # 후위 순회는 왼쪽, 오른쪽을 처리한 뒤 루트를 기록한다.
        postorder.append(root)

    build_postorder(0, len(inorder) - 1)

    return "".join(postorder)


if __name__ == "__main__":
    input = sys.stdin.readline

    preorder = input().strip()
    inorder = input().strip()

    print(solution(preorder, inorder))
