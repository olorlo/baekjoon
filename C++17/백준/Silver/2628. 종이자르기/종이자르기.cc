#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

// 백준 C++ 2628 종이자르기

int main() {
	// 테케 자동 입력
	// freopen("input.txt", "r", stdin);

	int n, m;
	cin >> n >> m;

	int a;
	cin >> a;

	int b, c;

	vector<int>y_arr;
	vector<int>x_arr;

	y_arr.push_back(0);
	y_arr.push_back(m);

	x_arr.push_back(0);
	x_arr.push_back(n);

	for (int cut = 0; cut < a; cut++) {
		cin >> b >> c;

		// 가로로 자르기
		if (b == 0) y_arr.push_back(c);

		// 세로로 자르기 ( b==1)
		else x_arr.push_back(c);
	}		

	sort(y_arr.begin(), y_arr.end());
	sort(x_arr.begin(), x_arr.end());

	int max_y = 0;
	int max_x = 0;

	for (int i = 1; i < y_arr.size(); i++) {
		max_y = max(y_arr[i] - y_arr[i-1], max_y);
	}

	for (int i = 1; i < x_arr.size(); i++) {
		max_x = max(x_arr[i] - x_arr[i-1], max_x);
	}

	cout << max_y * max_x;
}	