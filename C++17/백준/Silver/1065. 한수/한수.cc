#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
using namespace std;

// 백준 C++ 11723 집합

int main() {

	// 자동 입력
	// freopen("input.txt", "r", stdin);

	// 코테 기본 템플릿 : 빠른 입출력
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int N;
	cin >> N;

	vector<int>arr;
	int cnt1 = 0;

	if (N <= 99) {
		cnt1 += N;
		cout << cnt1;
		return 0;
	}
	cnt1 += 99;
    
	int remain = 0;
	int a1;
    
	for (int n = 100; n <= N; n++) {

		bool result = true;
		// 각 자리수마다 비교
		a1 = n;
		while (a1 > 0) {

			remain = a1 % 10;
			arr.push_back(remain);

			if (arr.size() >= 3) {
				int d1 = arr[arr.size() - 1] - arr[arr.size() - 2];
				int d2 = arr[arr.size() - 2] - arr[arr.size() - 3];

				if (d1 != d2) {
					result = false;
					break;
				}
				
			}
			a1 /= 10;
		}
		arr.clear();

		if (result == true) {
			cnt1++;
		}
	}
	cout << cnt1;
}