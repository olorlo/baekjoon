#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <algorithm>
#include <vector>

#include <cstdio>
#include <string>
using namespace std;

// 백준 C++ 2578 빙고

int main() {
	// 자동 입력
	// freopen("input.txt", "r", stdin);

	// 빠른 입출력
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	vector<vector<int>>bingo_board(5, vector<int>(5, 0));
	vector<vector<int>>call(5, vector<int>(5, 0));

	// 빙고판 입력
	for (int i = 0; i < 5; i++) {
		for (int j = 0; j < 5; j++) {
			cin >> bingo_board[i][j];
		}
	}

	// 부르는 번호
	for (int i = 0; i < 5; i++) {
		for (int j = 0; j < 5; j++) {
			cin >> call[i][j];
		}
	}

	int cnt = 0;

	int bingo_cnt = 0;

	for (int i = 0; i < 5; i++) {
		for (int j = 0; j < 5; j++) {
			
			bool found = false;
			// 부르는 수 찾아서 지움
			for (int k = 0; k < 5; k++) {
				for (int l = 0; l < 5; l++) {
					if (bingo_board[k][l] == call[i][j]) {
						bingo_board[k][l] = 0;
						found = true;
						break;
					}
				}
				if (found)
					break;
			}

			cnt++;

			// 밑의 코드는 모든 경우의 수를 다시 보는봄
			// 매번 부르는 수를 찾을때마다 빙고를 체크하기때문에 초기화 해주어야함
			bingo_cnt = 0;

			// 빙고 가로 체크
			for (int r = 0; r < 5; r++) {
				bool line = true;
				for (int c = 0; c < 5; c++) {
					if (bingo_board[r][c] != 0) line = false;
				}
				if (line) bingo_cnt++;
			}

			// 빙고 세로 체크
			for (int c = 0; c < 5; c++) {
				bool line = true;
				for (int r = 0; r < 5; r++) {
					if (bingo_board[r][c] !=0) line = false;
				}
				if (line) bingo_cnt++;
			}

			// 빙고 왼쪽 대각선 체크
			bool line1 = true;
			for (int k = 0; k < 5; k++) {
				if (bingo_board[k][k] != 0) line1 = false;
			}
			if (line1) bingo_cnt++;

			// 빙고 오른쪽 대각선 체크
			bool line2 = true;
			for (int k = 0; k < 5; k++) {
				if (bingo_board[4 - k][k] != 0) line2 = false;
			}
			if (line2) bingo_cnt++;

			if (bingo_cnt >= 3) {
				cout << cnt;
				return 0;
			}
		}
	}
}