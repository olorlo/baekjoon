#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int main() {

	int N = 0;
	int K = 0;
	scanf("%d %d", &N, &K);
	// 동적 메모리 할당 
	int* arr = (int*)malloc(sizeof(int)*N);

	// 배열 입력
	for (int k = 0; k < N; k++) {
		scanf("%d", &arr[k]);
	}

	// 선택 정렬 알고리즘
	// (i는 맨 마지막부터 시작하는 정렬된 배열 인덱스)
	// (j는 처음부터 i전까지 정렬 안된 배열 인덱스 )
	int cnt = 0;
	for (int i = N - 1; i > 0; i--) {
		int max_index = i;
		
		for (int j = 0; j < i; j++) { //정렬이 안된 상태
			if (arr[max_index] < arr[j]) {
				// 최대값 인덱스가 최대값이 아닐 때 인덱스 값 변경 
				max_index = j;
			}
		}
		// 최대값 인덱스가 i가 아닐때 swap 
		if (max_index != i) {
			int temp = arr[max_index];
			arr[max_index] = arr[i];
			arr[i] = temp;

			// swap 된 수 카운트
			cnt += 1;

			// 카운트 수가 K면 바로 break
			if (cnt == K) {
				break;
			}
		}
			

	}
	// 문제 조건: 카운트 수가 K보다 적으면 -1 출력
	if (cnt < K)
		printf("-1");
	// 아닐 경우: 현재까지 정렬된 배열 출력
	else {
		for (int i = 0; i < N; i++) {
			printf("%d ", arr[i]);
		}
	}

	free(arr);
	return 0;
}
