// JUNGOL 8553 Tutorial : STL Sort 2 (정렬 기준 설정)
// 난이도: bronze5
// 분류: sorting, stl, sort, compare_function
// 핵심:
//   C++ STL sort()의 세 번째 인자로 비교 함수를 넘기면
//   원하는 기준으로 정렬할 수 있다.
//   세 자리 정수를 일의 자리, 십의 자리, 백의 자리 순서로 비교한다.
// 시간 복잡도: O(N log N)
// 공간 복잡도: O(N)

#include <bits/stdc++.h>
using namespace std;
// 1. 문제 이해
// - 입력:
//   N: 배열의 크기
//   arr: N개의 세 자리 정수
// - 출력:
//   정렬 기준에 맞게 정렬한 정수들을 한 줄에 하나씩 출력
// - 핵심 문법:
//   sort(시작 위치, 끝 위치, 비교 함수);


// 2. 아이디어
// - sort(arr.begin(), arr.end())는 기본적으로 오름차순 정렬이다.
// - 여러 기준으로 정렬하려면 비교 함수를 직접 만들 수 있다.
// - comp(left, right)가 true이면 left를 right보다 앞에 둔다.
// - 1순위: 일의 자리 숫자가 작은 수가 앞에 온다.
// - 2순위: 십의 자리 숫자가 작은 수가 앞에 온다.
// - 3순위: 백의 자리 숫자가 작은 수가 앞에 온다.


// 3. 풀이 계획
// 1) N을 입력받는다.
// 2) 배열 arr를 입력받는다.
// 3) 비교 함수 comp를 사용해 배열 전체를 정렬한다.
// 4) 정렬된 숫자를 한 줄에 하나씩 출력한다.


bool comp(int left, int right) {
    int left_one = left % 10;
    int right_one = right % 10;

    if (left_one != right_one) {
        return left_one < right_one;
    }

    int left_ten = (left / 10) % 10;
    int right_ten = (right / 10) % 10;

    if (left_ten != right_ten) {
        return left_ten < right_ten;
    }

    int left_hundred = left / 100;
    int right_hundred = right / 100;

    return left_hundred < right_hundred;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int N;
    cin >> N;

    vector<int> arr(N);
    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }

    sort(arr.begin(), arr.end(), comp);

    for (int i = 0; i < N; i++) {
        cout << arr[i] << '\n';
    }

    return 0;
}
