#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
// 백준 C++ 2605번 줄 세우기
int main() {
	int N ;
	cin >> N;
	vector<int> arr(N);
	for (int i = 0; i < N; i++)
		cin >> arr[i];
	vector<int> result;
	for (int i = 0; i < N; i++) {
		result.insert(result.end() - arr[i], i);
	}
	for (int i = 0; i < N; i++)
		cout << result[i] + 1<< ' ';
}