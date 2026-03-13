#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>

#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

// 백준 C++ 10709번 기상캐스터
int main() {
	// 테케 자동 입력
	// freopen("input.txt", "r", stdin);

	// 입력
	int H, W;
	cin >> H >> W;
	vector<vector<char>>arr(H, vector<char>(W));
	vector<vector<int>>result(H, vector<int>(W, -1));

	for (int i = 0; i < H; i++) {
		for (int j = 0; j < W; j++) {
			cin >> arr[i][j];
		}
	}


	// 각 구역에 대해서 지금부터 몇 분 뒤 처음으로 구름이 오는지 
	for (int i = 0; i < H; i++) {
		int cloud = -1;

		for (int j = 0; j < W; j++) {

			if (arr[i][j] == 'c') {
				cloud = j;
				result[i][j] = 0;
			}
			else if (cloud != -1) {
				result[i][j] = j - cloud;
			}
		}
	}

	// 출력
	for (int i = 0; i < H; i++) {
		for (int j = 0; j < W; j++) {
			cout << result[i][j] << " ";
		}
		cout << "\n";
	}
}	