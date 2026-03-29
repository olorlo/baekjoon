#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

long long func(long long a, long long b, long long c) {
	// B를 기준으로 나눔

	// 종료조건: b가 0이면 더 이상 안 곱해도 됨
	if (b == 0) return 1;

	// b를 반으로 줄여서 다시 함수에 넣음
	long long temp = func(a, b / 2, c);

	// b가 짝수이면 temp 2번 곱해줌
	if (b % 2 == 0)
		return (temp * temp) % c;

	// b가 홀수이면 2번 곱해주고 모듈러 연산을 하여 결과를 줄인뒤에 다시 a를 곱해서 모듈러 연산
	else
		return (temp * temp % c) * a % c;

}

// 백준 C++ 1629 곱셈
/*
 우리가 구하려는 것: a ^ b % c
 pow나 for문 사용 시 무조건 시간 초과
 핵심 아이디어: 반으로 계속 쪼갠다 
 -> 2^10인 경우
 (2^5)^2
 (2*(2^2)^2)^2
 (2*(2^1)^2)^2)^2 
 이런 식으로 쪼갤 수 있음
*/
 
int main() {

	// 자동 입력
	// freopen("input.txt", "r", stdin);

	// 코테 기본 템플릿 : 빠른 입출력
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int A, B, C;
	cin >> A >> B >> C;

	cout << func(A, B, C);
}