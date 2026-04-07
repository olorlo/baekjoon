#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int min_result, max_result;

void cal(int now, vector<int>& card, vector<int>& arr, int result) {
	// 종료 조건: 더 이상 연산할 연산자 없을 경우 종료
	if (now == arr.size() - 1) {
		max_result = max(max_result, result);
		min_result = min(min_result, result);
		return;
	}

	for (int i = 0; i < 4; i++) {
		if (card[i] > 0) {
			card[i] --;

			// + 인 경우
			if (i == 0) 
				cal(now + 1, card, arr, result + arr[now+1]);

			// - 인 경우
			else if (i == 1) 
				cal(now + 1, card, arr, result - arr[now + 1]);

			// * 인 경우
			else if (i == 2) 
				cal(now + 1, card, arr, result * arr[now + 1]);

			// / 인 경우
            else if (i == 3) {
                if (result < 0)
                    cal(now + 1, card, arr, -(-result / arr[now + 1]));
                else
                    cal(now + 1, card, arr, result / arr[now + 1]);
            }
			card[i] ++;
		}
	}
	
}

int main() {

    // N: 숫자의 개수
    int N = 0;
    cin >> N;
    
    // arr: 수식에 들어갈 숫자
    vector<int>arr(N);
    for (int i = 0; i < N; i++) cin >> arr[i];

    // card: 연산자 카드의 개수
    vector<int>card(4);
    for (int i = 0; i < 4; i++) cin >> card[i];

    // 계산
    max_result = -1e9;
    min_result = 1e9;
    cal(0, card, arr, arr[0]);

    cout << max_result << '\n';
    cout << min_result;
	
}