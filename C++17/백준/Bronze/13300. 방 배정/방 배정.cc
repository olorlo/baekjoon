#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
// 백준 C++ 13300번 방 배정
int main() {
	int N, K;
	cin >> N >> K;

	// vector<타입> 이름(개수, 초기값)
	vector<vector<int>> room(7, vector<int>(2,0));

	for (int i = 0; i < N; i++) {
		int S, Y;
		cin >> S >> Y;
		room[Y][S]++;
	}
	int cnt = 0;
	for (int y = 1; y < 7; y++) {
		for (int s = 0; s < 2; s++) {
			if (room[y][s] == 0)
				continue;
			// 필요한 방의 개수
			cnt += (room[y][s] + K - 1) / K;
		}
	}

	cout << cnt;
}