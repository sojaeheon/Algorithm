// JUNGOL 1697 큐
// 난이도: bronze
// 분류: queue, data_structure
// 핵심:
//   큐는 먼저 들어온 값이 먼저 나가는 FIFO 자료구조이다.
//   C++에서는 STL queue를 사용할 수 있다.
//   명령 i는 삽입, o는 출력 후 제거, c는 개수 출력이다.
// 시간 복잡도: O(N)
// 공간 복잡도: O(N)


// 1. 문제 이해
// - 입력:
//   N: 명령의 개수, 1 <= N <= 100
//   commands: N개의 명령
//   "i a": a를 큐에 넣는다.
//   "o": 큐에서 데이터를 빼고 출력한다. 비어 있으면 "empty"를 출력한다.
//   "c": 큐에 들어 있는 데이터의 수를 출력한다.
// - 출력:
//   o, c 명령에 대한 결과를 한 줄에 하나씩 출력한다.
// - 구해야 하는 것:
//   명령 순서대로 큐를 처리한 결과


// 2. STL queue 기본 문법
// - 선언:
//   queue<int> q;
// - 값 넣기:
//   q.push(value);
// - 맨 앞 값 확인:
//   q.front();
// - 맨 앞 값 제거:
//   q.pop();
// - 비었는지 확인:
//   q.empty();
// - 크기 확인:
//   q.size();


// 3. 아이디어
// - 명령을 하나씩 읽는다.
// - i 명령이면 queue에 값을 넣는다.
// - o 명령처럼 값을 꺼내야 하는 명령에서는
//   큐가 비어 있는지 먼저 확인한다.
// - 큐가 비어 있는데 front/pop을 하면 오류가 나므로 empty를 출력한다.


// 4. 풀이 계획
// 1) 명령 개수 N을 입력받는다.
// 2) queue<int>를 만든다.
// 3) 명령을 하나씩 입력받는다.
// 4) i 명령이면 값을 입력받아 push한다.
// 5) o 명령이면 비었을 때 empty, 아니면 front 출력 후 pop한다.
// 6) c 명령이면 size를 출력한다.


#include <iostream>
#include <queue>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    queue<int> pipe;
    int n, a;
    char w;

    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> w;

        if (w == 'i') {
            cin >> a;
            pipe.push(a);
        }
        else if (w == 'o') {
            if (pipe.empty()) {
                cout << "empty" << '\n';
            }
            else {
                cout << pipe.front() << '\n';
                pipe.pop();
            }
        }
        else if (w == 'c') {
            cout << pipe.size() << '\n';
        }
    }

    return 0;
}
