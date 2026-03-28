#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>

using namespace std;

// 백준 C++ 1912 연속합

int main() {

	// 자동 입력
	// freopen("input.txt", "r", stdin);

	// 코테 기본 템플릿 : 빠른 입출력
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int n;
	cin >> n;
	vector<int>arr(n);

	for (int i = 0; i < n; i++)
		cin >> arr[i];

	vector<int>dp(n);
	dp[0] = arr[0];
	
	int result = arr[0];

	for (int i = 1; i < n; i++) {
		dp[i] = max(arr[i], dp[i - 1] + arr[i]);
		result = max(result, dp[i]);
	}

	cout << result;
}