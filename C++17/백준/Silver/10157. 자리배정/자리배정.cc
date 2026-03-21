#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>

using namespace std;

// 백준 C++ 10157 자리배정

int main() {

	// 자동 입력
	// freopen("input.txt", "r", stdin);

	// 코테 기본 템플릿 : 빠른 입출력
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int C, R;
	cin >> C >> R;

	int K;
	cin >> K;

	vector<vector<int>>arr(R, vector<int>(C, 0));

	// 방향 배열(상우하좌)
	int dy[4] = { -1, 0, 1, 0 };
	int dx[4] = { 0, 1, 0, -1 };

	// 시작
	int start_y = R-1;
	int start_x = 0;
	int dir = 0;

	int current = 1;

	if (K > R * C) {
		cout << 0;
		return 0;
	}

	while (true) {


		if (current == K) {
			cout << start_x+1 << ' ' << R-start_y;
			return 0;
		}
		arr[start_y][start_x] = current;

		int ny = start_y + dy[dir];
		int nx = start_x + dx[dir];

		if (ny < 0 || ny >= R || nx < 0 || nx >= C || arr[ny][nx] != 0) {
			dir = (dir + 1) % 4;
		}

		current += 1;
		start_y += dy[dir];
		start_x += dx[dir];

	}
	cout << 0;
}