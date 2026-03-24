#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>

using namespace std;

// 백준 C++ 2567 색종이 - 2

int main() {

	// 자동 입력
	// freopen("input.txt", "r", stdin);

	// 코테 기본 템플릿 : 빠른 입출력
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int n;
	cin >> n;
	vector<vector<int>>arr(100, vector<int>(100, 0));
	int a, b;

	int dy[4] = {-1, 0, 1, 0};
	int dx[4] = {0, 1, 0, -1};

	// 색종이 붙이기
	for (int i = 0; i < n; i++) {
		cin >> a >> b;
		for (int j = b - 1; j < b + 9; j++) 
			for (int l = a - 1; l < a + 9; l++) 
				arr[j][l] = 1;
	}

	int cnt = 0;
	// 둘레 체크
	for (int i = 0; i < 100; i++) 
		for (int j = 0; j < 100; j++) {
			if (arr[i][j] == 1) 
				for (int k = 0; k < 4; k++) {
					int ny = i + dy[k];
					int nx = j + dx[k];
                    
                    // 범위 밖일 때도 둘레 셀 수 있음
					if (ny < 0 || ny >= 100 || nx < 0 || nx >= 100)
						cnt++;

					else if (arr[ny][nx] == 0) 
						cnt++;
				}
		}
	cout << cnt;
}