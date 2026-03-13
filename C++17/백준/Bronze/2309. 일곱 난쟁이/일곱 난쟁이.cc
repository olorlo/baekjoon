#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>

#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <numeric>
using namespace std;

// 백준 C++ 2309번 일곱 난쟁이

vector<int>height(9);
vector<int>result;

void dfs(int idx, int cnt) {

	if (cnt == 7) {
		if (accumulate(result.begin(), result.end(), 0) == 100) {
			sort(result.begin(), result.end());
			for (int x : result)
				cout << x << "\n";
			exit(0);
		}
		return;
	}
	for (int i = idx; i < 9; i++) {
		result.push_back(height[i]);
		dfs(i + 1, cnt + 1);
		result.pop_back();
	}

}


int main() {
	// 테케 자동 입력
	//freopen("input.txt", "r", stdin);

	int sum = 0;

	for (int i = 0; i < 9; i++) {
		cin >> height[i];
	}
	dfs(0, 0);

}	