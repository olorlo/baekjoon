// 백준 1546번 평균

#include <iostream>
#include <vector>
using namespace std;

int main() {
	// 과목의 개수 N
	int N = 0;
	cin >> N;

	float M = 0;
	float sum_score = 0;

	// 점수 입력 받기
	vector<float> score(N);
	for (int i =0; i<N;i++)
		cin >> score[i];

	// 점수 중 최대값 찾기
	for (int i = 0; i < N; i++) 
		if (score[i] > M)
			M = score[i];
	
	// 점수 조정
	for (int i = 0; i < N; i++) {
		sum_score += (score[i] / M) * 100.0;
	}
	cout << sum_score / N;
}