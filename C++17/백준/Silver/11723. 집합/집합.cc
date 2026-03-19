#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <cstdio>
#include <string>
using namespace std;

// 백준 C++ 11723 집합

int main() {

	// 자동 입력
	// freopen("input.txt", "r", stdin);

	// 코테 기본 템플릿 : 빠른 입출력
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int M;
	cin >> M;

	// 비트마스크 풀이
	int S = 0;

	string cmd;
	int x;

	while (M--) {
		cin >> cmd;
		if (cmd == "all") {
			S = (1 << 20) - 1;
			continue;
		}
		else if (cmd == "empty") {
			S = 0;
			continue;
		}

		cin >> x;
		if (cmd == "add")
			S |= (1 << (x - 1));
		else if (cmd == "remove")
			// x-1 자리에 1을 넣고 비트 반전시킴 + and 연산 수행하면 해당 자리만 비트 연산수행됨
			S &= ~(1 << (x - 1));
		else if (cmd == "check") {
			if (S & (1 << (x - 1)))
				cout << 1 << '\n';
			else
				cout << 0 << '\n';
		}
		else if (cmd == "toggle") {
			// S에 있으면 제거, 없으면 추가
			S ^= (1 << (x - 1));
		}
	}

}