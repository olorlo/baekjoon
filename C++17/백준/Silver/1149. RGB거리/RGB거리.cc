#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>

using namespace std;

// 백준 C++ 1149 RGB 거리

int main() {

	// 자동 입력
	// freopen("input.txt", "r", stdin);

	// 코테 기본 템플릿 : 빠른 입출력
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int N;
	cin >> N;

	vector<vector<int>>cost(N, vector<int>(3, 0));
	// dp[i][color] = i번째 집을 color로 칠한 최소 비용
	vector<vector<int>>dp(N, vector<int>(3, 0));

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < 3; j++) {
			cin >> cost[i][j];
		}
	}
	dp[0][0] = cost[0][0];
	dp[0][1] = cost[0][1];
	dp[0][2] = cost[0][2];

	for (int i = 1; i < N; i++) {
		dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + cost[i][0];
		dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + cost[i][1];
		dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + cost[i][2];
	}
	int ans = min({ dp[N - 1][0], dp[N - 1][2], dp[N - 1][1] });
	cout << ans;
}