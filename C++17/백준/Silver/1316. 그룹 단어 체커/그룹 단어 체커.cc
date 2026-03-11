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

	// 단어 개수 입력
	int N;
	cin >> N;

	int cnt = 0;

	// 단어 c 입력 시 
	for (int i = 0; i < N; i++) {
		string c;
		cin >> c;

		// true, false만 필요하기 때문에 bool로 선언함
		bool visited[26] = { 0 };
		bool group = true;

		// 지금 단어가 그룹 단어인지 체크
		// 
		for (int j = 0; j < c.length(); j++) {
			if (j>0 && c[j] != c[j - 1]) {
				// 알파벳을 배열 인덱스로 바꿔주기 위해서 제일 처음 수 a를 뺌
				// 만약 해당 알파벳이 이미 방문된 곳이라면 그룹 단어가 아님 -> group = False
				if (visited[c[j] - 'a']) {
					group = false;
					break;
				}
			}
			// 방문되지 않은 곳이라면 방문 표시 해줌
			visited[c[j] - 'a'] = true;
		}
		// 그룹 단어라면 개수 카운트
		if (group)
			cnt++;
	}
	// 결과 출력
	cout << cnt;
}	