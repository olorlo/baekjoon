#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

// 백준 C++ 1057 토너먼트

int main() {
	// 테케 자동 입력
	// freopen("input.txt", "r", stdin);

	int N, jimin, hansu;
	cin >> N >> jimin >> hansu;
	int cnt = 0;

	while (true) {
		if (min(jimin, hansu) % 2 == 1 && abs(jimin - hansu) == 1) {
			cnt++;
			break;
		}

		jimin = (jimin + 1) / 2;
		hansu = (hansu + 1) / 2;
		cnt++;
	}

	cout << cnt;
}