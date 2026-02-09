#include <iostream>
// #include <bits/stdc++.h> : c++ 표준 라이브러리 거의 전부 포함하는 헤더!
// iostream, vector, algorithm, sting 모두 다 가져옴

// std::cin 대신 cin으로 쓰고 싶다면 작성
using namespace std;

int main() {
	// 메인 함수 제일 위에(입,출력 전) 밑에껄 넣으면 
	// C 표준입출력(printf/scanf)과
	// C++ 스트림(cin / cout)의 동기화 끊기
	ios::sync_with_stdio(false);

	// cin할 때마다 cout 버퍼를 먼저 비우는 것을 막음(cin과 cout의 연결 해제)
	// 성능이 빨라진다.
	cin.tie(NULL);

	int A, B;
	// 밑의 방식도 되고 
	// cin >> A; 
	// cin >> B;도 가능
	cin >> A >> B;
	
	if (A > B)
		cout << '>';
	else if (A < B)
		cout << '<';
	else // 문자 2개 출력할 때는 큰 따옴표로 감싸기
		cout << "==";
}

// 코테 템플릿
//#include <bits/stdc++.h>
//using namespace std;
//
//int main() {
//	ios::sync_with_stdio(false);
//	cin.tie(NULL);
//}