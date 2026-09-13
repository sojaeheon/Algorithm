// JUNGOL 8551 Tutorial : STL Sort 1 (기본 사용법)
// 난이도: bronze5
// 분류: sorting, stl, sort
// 핵심:
//   C++ STL sort()를 사용해 배열의 특정 구간과 전체 구간을 오름차순 정렬한다.
//   sort(start, end)는 start 이상 end 미만 범위를 정렬한다.
// 시간 복잡도: O(N log N)
// 공간 복잡도: O(N)

#include <bits/stdc++.h>

using namespace std;


// 1. 문제 이해
// - 입력:
//   N: 배열의 크기
//   arr: N개의 정수
//   s, e: 먼저 정렬할 구간의 시작/끝 인덱스
// - 출력:
//   1) 인덱스 s 이상 e 이하인 구간만 오름차순 정렬한 배열
//   2) 배열 전체를 오름차순 정렬한 배열
// - 주의:
//   sort(arr.begin() + s, arr.begin() + e + 1)처럼 e + 1까지 써야
//   인덱스 e가 정렬 범위에 포함된다.


// 2. 아이디어
// - 원본 배열을 하나 복사한다.
// - 복사한 배열에서는 부분 구간만 정렬한다.
// - 원본 배열에서는 전체를 정렬한다.
// - C++의 sort는 기본적으로 오름차순 정렬이다.


// 3. 풀이 계획
// 1) N과 배열, s, e를 입력받는다.
// 2) arr를 partial_sorted에 복사한다.
// 3) partial_sorted의 [s, e] 구간만 정렬하고 출력한다.
// 4) arr 전체를 정렬하고 출력한다.


void print_vector(const vector<long long>& values) {
    for (int i = 0; i < (int)values.size(); i++) {
        if (i > 0) {
            cout << ' ';
        }
        cout << values[i];
    }
    cout << '\n';
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    vector<long long> arr(N);
    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }

    int s, e;
    cin >> s >> e;

    vector<long long> partial_sorted = arr;

    sort(partial_sorted.begin() + s, partial_sorted.begin() + e + 1);
    print_vector(partial_sorted);

    sort(arr.begin(), arr.end());
    print_vector(arr);

    return 0;
}
