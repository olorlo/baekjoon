// 백준 5086번 배수와 약수

#include <iostream>
using namespace std;

int main() {
	int a, b;
	while (true) {
		cin >> a >> b;
		if (a == 0 && b == 0)
			break;
		// 줄바꿈 방식 2가지 \n, endl
		if (b % a == 0)
			cout << "factor\n";
		else if (a % b == 0)
			cout << "multiple" << endl;
		else
			cout << "neither" << endl;
	}
}