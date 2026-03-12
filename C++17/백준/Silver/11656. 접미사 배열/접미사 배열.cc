#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>

#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

// 백준 C++ 11656번 접미사 배열
int main() {
	// 테케 자동 입력
	// freopen("input.txt", "r", stdin);

	string s;
	cin >> s;
	string str;
	vector<string>result(s.length());
	for (int i = 0; i < s.length(); i++) {
		str = s.substr(i);
		//sort(str.begin(), str.end());
		result[i] = str;
		
	}
	sort(result.begin(), result.end());
	for (int i = 0; i < s.length(); i++)
		cout << result[i] << "\n";
}	