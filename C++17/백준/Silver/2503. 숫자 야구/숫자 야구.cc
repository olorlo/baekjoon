#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>

using namespace std;

// 백준 C++ 2503 숫자 야구

int main() {

	// 자동 입력
	// freopen("input.txt", "r", stdin);

	// 코테 기본 템플릿 : 빠른 입출력
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	// 완전 탐색으로 123 ~ 987까지 돌려본다
	int N;
	cin >> N;
	int ans = 0;
	int word, strike, ball;

	// 입력 먼저 받기
	vector<tuple<int, int, int>>data(N);
	for (int t = 0; t < N; t++) {
		cin >> word >> strike >> ball;
		data[t] = { word, strike, ball };
	}
	
    // 전체 돌리면서 개수 맞는지 체크 
    // i: 백의 자리, j: 십의 자리, k: 일의 자리
	for (int i = 1; i <= 9; i++) {
		for (int j = 1; j <= 9; j++) {
            // 같은 지 체크
			if (i == j) continue;
			for (int k = 1; k <= 9; k++) {
                // 같은지 체크
				if (k == i || k == j) continue;
                
                // 일단 ok는 true라고 가정함 
                // 나중에 false 조건을 거쳤는데도 true이면 ans ++ 
				bool ok = true;

				for (auto& [word, strike, ball] : data) {
					int cnt_strike = 0;
					int cnt_ball = 0;

					int a = word / 100;
					int b = (word / 10) % 10;
					int c = word % 10;

					// strike 개수 체크
					if (i == a) cnt_strike++;
					if (j == b) cnt_strike++;
					if (k == c) cnt_strike++;

					// ball 개수 체크
					if (i != a && (i == b || i == c)) cnt_ball++;
					if (j != b && (j == a || j == c)) cnt_ball++;
					if (k != c && (k == a || k == b)) cnt_ball++;

					if (strike != cnt_strike || ball != cnt_ball) {
						ok = false;
						break;
					}
					
				}
				if (ok) ans++;
			}
		}
	}
    // 결과 출력
	cout << ans;
}