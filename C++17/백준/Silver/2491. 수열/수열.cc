#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

// 백준 C++ 2491 수열

int main() {
	// 테케 자동 입력
	// freopen("input.txt", "r", stdin);

	int N;
	cin >> N;

	vector<int>arr(N);

	for (int i = 0; i < N; i++) {
		cin >> arr[i];
	}

	int cnt_increase = 1;
	int cnt_decrease = 1;

	vector<int>result;

	for (int i = 0; i < N-1; i++) {
		if (arr[i] <= arr[i+1]) {
			cnt_increase++;
		}
		else {
			result.push_back(cnt_increase);
			cnt_increase = 1;
		}

		if (arr[i] >= arr[i + 1]) {
			cnt_decrease++;
		}
		else {
			result.push_back(cnt_decrease);
			cnt_decrease = 1;
		}
	}

	result.push_back(cnt_increase);
	result.push_back(cnt_decrease);

	// result 벡터에서 최대값 찾기
	cout << *max_element(result.begin(), result.end());
}