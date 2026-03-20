#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <algorithm>
#include <vector>

#include <cstdio>
#include <string>
using namespace std;

// 백준 C++ 1244 스위치 켜고 끄기

int main() {
	// 자동 입력
	// freopen("input.txt", "r", stdin);

	// 빠른 입출력
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int N;
	cin >> N;

	vector<int>arr(N+1);

	for (int i = 1; i <= N; i++)
		cin >> arr[i];

	int M;
	cin >> M;

	int a, b;

	for (int i = 0; i < M; i++) {
		cin >> a >> b;

		// 남자일 때
		if (a == 1) {
			for (int k = b; k <= N; k+=b) {
				arr[k] ^= 1;
			}
		}
		
		// 여자일 때
		else {

			for (int k = 0; k < N; k++) {
				if (b - k < 1 || b + k > N)
					break;
				if (k == 0)
					arr[b] ^= 1;
				else if (arr[b + k] == arr[b - k]) {
					arr[b + k] ^= 1;
					arr[b - k] ^= 1;
				}
				else
					break;
			}
		}

	}
	for (int i = 1; i <= N; i++) {
		cout << arr[i] << ' ';
		if (i % 20 == 0)
			cout << '\n';
	}
}