// 백준 2675번 C++ 문자열 반복

#include <iostream>
#include <vector>
using namespace std;

int main() {

	// 테스트 케이스
	int T = 0;
	cin >> T;
	for (int i = 0; i < T; i++) {

		int R = 0;
		string S;
		cin >> R >> S;
		string P;
		int s = 0;

		while(true) {
			if (S[s]) {
				for (int j = 0; j < R; j++) {
					P += S[s];
				}
				s++;
			}
			else
				break;
		}
		cout << P;
		cout << '\n';
	}

}