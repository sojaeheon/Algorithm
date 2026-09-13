// JUNGOL 8557 Tutorial : STL Pair
// 난이도: bronze5
// 분류: stl, pair, sorting
// 핵심:
//   pair는 두 값을 하나로 묶어서 저장하는 C++ STL 자료형이다.
//   pair의 첫 번째 값은 first, 두 번째 값은 second로 접근한다.
//   pair를 sort하면 first 오름차순, first가 같으면 second 오름차순으로 정렬된다.
// 시간 복잡도: O(N log N)
// 공간 복잡도: O(N)

#include <bits/stdc++.h>

using namespace std;


// 1. 문제 이해
// - 입력:
//   N: 정수 점의 개수
//   points: N개의 (x, y) 좌표
// - 출력:
//   점들을 x 좌표 오름차순, x가 같으면 y 좌표 오름차순으로 정렬한 뒤
//   각 점마다 x * y 값을 한 줄에 하나씩 출력한다.
// - 구해야 하는 것:
//   pair<int, int>에 (x, y)를 저장하고 기본 정렬 기준을 이용한다.


// 2. STL pair 기본 문법
// - 선언:
//   pair<int, int> p;
//   pair<string, int> student;
// - 값 넣기:
//   p = {3, 5};
//   p = make_pair(3, 5);
// - 값 꺼내기:
//   p.first   -> 첫 번째 값
//   p.second  -> 두 번째 값


// 3. 아이디어
// - 점 하나는 x, y 두 값을 함께 관리해야 하므로 pair를 사용한다.
// - vector<pair<int, int>>에 여러 점을 저장한다.
// - sort(points.begin(), points.end())를 하면 기본 정렬 기준은 다음과 같다.
//   1순위: first 오름차순
//   2순위: second 오름차순
// - 따라서 별도의 비교 함수를 만들 필요가 없다.


// 4. 풀이 계획
// 1) N을 입력받는다.
// 2) 각 점의 x, y를 pair로 묶어 points에 저장한다.
// 3) points를 기본 기준으로 정렬한다.
// 4) 정렬된 점마다 x * y를 출력한다.


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    vector<pair<int, int>> points(N);

    for (int i = 0; i < N; i++) {
        int x, y;
        cin >> x >> y;

        points[i] = {x, y};
    }

    sort(points.begin(), points.end());

    for (int i = 0; i < N; i++) {
        int x = points[i].first;
        int y = points[i].second;

        cout << x * y << '\n';
    }

    return 0;
}
