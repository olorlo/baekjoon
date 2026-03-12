#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

// 백준 C++ 10815번 숫자카드
int main() {
	// 테케 자동 입력
	// freopen("input.txt", "r", stdin);

	// 범위가 너무 커서 완탐하면 시간 초과난다
	// 이진 탐색으로 구현! -> C++: 이진탐색 함수 존재
	int N;
	cin >> N;

	vector<int>arr(N);
	for (int i = 0; i < N; i++)
		cin >> arr[i];

	// 이진탐색을 위해 arr 정렬
	sort(arr.begin(), arr.end());

	int M;
	cin >> M;

	vector<int>b(M);
	for (int i = 0; i < M; i++)
		cin >> b[i];

	vector<int>result(M);

	for (int i = 0; i < M; i++) {
		// binary_search 함수: 값이 존재하면 true, 없으면 false를 반환하는 함수
		// binary_search(시작 iterator, 끝 iterator, 찾을 값)
		cout << binary_search(arr.begin(), arr.end(), b[i]) << " ";
	}
}	