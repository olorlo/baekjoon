#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

// 백준 C++ 2477번 참외밭
int main()
{
	// 파일 입력
	// freopen("input.txt", "r", stdin);

	// 빠른 입출력
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int K;
	cin >> K;

	vector<int>d(6);
	vector<int>l(6);

	for (int i = 0; i < 6; i++) {
		cin >> d[i] >> l[i];
	}

	//// 큰 사각형 구하기
	//int max_garo = 0, max_sero = 0;
	//for (int i = 0; i < 6; i++) {
	//	// 가로일 때
	//	if (d[i] == 1 || d[i] == 2) 
	//		max_garo = max(max_garo, l[i]);
	//	// 세로 일때
	//	else
	//		max_sero = max(max_sero, l[i]);
	//}
	//int big = max_garo * max_sero;

	//// 작은 사각형 구하기
	//int small = 0;
	//for (int i = 0; i < 6; i++) {
	//	// 방향이 같으면 작은 사각형이 만들어진다.
	//	if (d[i] == d[(i + 2) % 6]) {
	//		small = l[(i + 1)%6] * l[(i + 2)%6];
	//		break;
	//	}
	//}

	// 큰 사각형 + 인덱스
	int max_garo = 0, max_sero = 0;
	int idx_garo = 0, idx_sero = 0;

	for (int i = 0; i < 6; i++) {
		if ((d[i] == 1 || d[i] == 2) && l[i] > max_garo) {
			max_garo = l[i];
			idx_garo = i;
		}
		if ((d[i] == 3 || d[i] == 4) && l[i] > max_sero) {
			max_sero = l[i];
			idx_sero = i;
		}
	}

	// 작은 사각형
	int small = l[(idx_garo + 3) % 6] * l[(idx_sero + 3) % 6];

	// 결과
	int area = (max_garo * max_sero - small);


	// 넓이 구하기
	//int area = big - small;

	cout << area * K;
}