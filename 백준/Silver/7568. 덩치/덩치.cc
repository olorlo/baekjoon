#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

// 백준 C++ 7568 덩치

int main() {
	// freopen("input.txt", "r", stdin);

	int N;
	cin >> N;
	int x, y;
	vector<vector<int>>arr(N, vector<int>(2, 0));

	vector<int>cnt(N, 0);

	// 입력 받음 
	// 입력 받고 두개를 비교 하고 나보다 작은 게 있다? -> 카운트함
	for (int i = 0; i < N; i++) {
		cin >> arr[i][0] >> arr[i][1];
	}
	for (int i = 0; i < N; i++){
		for (int j = 0; j < N; j++) {
			if (i == j)
				continue;

			if (arr[i][0] < arr[j][0] && arr[i][1] < arr[j][1]) {
				cnt[i] ++;
			}
		}
	}
	for (int i = 0; i < N; i++) {
		cout << cnt[i]+1 << " ";
	}
}