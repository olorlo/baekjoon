#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
int main() {
	int N, k;
	scanf("%d %d", &N, &k);
	// 배열 arr 동적할당
	int* arr=(int*)malloc(sizeof(int)*N);
	// 배열 입력 받음
	for (int i = 0; i < N; i++) {
		scanf("%d", &arr[i]);
	}
	// 배열 정렬
	int temp = 0;
	for (int i = 0; i < N - 1; i++) {
		for (int j = 0; j < N - 1 - i; j++) {
			if (arr[j] > arr[j + 1]) {
				temp = arr[j];
				arr[j] = arr[j + 1];
				arr[j + 1] = temp;
			}
		}
	}
	printf("%d", arr[N - k]);

	return 0;
}