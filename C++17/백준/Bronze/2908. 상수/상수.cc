// 백준 2908번 C++ 상수

#include <iostream>
#include <algorithm>
using namespace std;

int main() {

	string A, B;
	cin >> A >> B;

	reverse(A.begin(), A.end());
	reverse(B.begin(), B.end());

	if (A > B) {
		cout << A;
	}
	else {
		cout << B;
	}

}