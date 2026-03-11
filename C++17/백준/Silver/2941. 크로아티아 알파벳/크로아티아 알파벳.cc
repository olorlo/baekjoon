#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

// 백준 C++ 1316번 그룹 단어 체커
int main() {
	// 테케 자동 입력
	// freopen("input.txt", "r", stdin);

	string s;
	cin >> s;

	int cnt = 0;

	for (int i = 0; i < s.length(); i++) {
		if (s[i] == 'c' && (s[i + 1] == '=' || s[i + 1] == '-')) i++;
		else if (s[i] == 'd' && s[i + 1] == '-') i++;
		else if (s[i] == 'd' && s[i + 1] == 'z' && s[i + 2] == '=') i += 2;
		else if (s[i] == 'l' && s[i + 1] == 'j') i++;
		else if (s[i] == 'n' && s[i + 1] == 'j') i++;
		else if (s[i] == 's' && s[i + 1] == '=') i++;
		else if (s[i] == 'z' && s[i + 1] == '=') i++;

		cnt++;
	}

	cout << cnt;
}	