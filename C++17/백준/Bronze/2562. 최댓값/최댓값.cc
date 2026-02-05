#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int main() {
	int arr[9];
	for (int i = 0; i < 9; i++) {
		scanf("%d", &arr[i]);
	}
	int max_arr = 0;
	int index_i = 0;
	for (int i = 0; i < 9; i++) {
		if (arr[i] > max_arr) {
			max_arr = arr[i];
			index_i = i;
		}
	}
	
	printf("%d\n%d", max_arr, index_i+1);
	
	return 0;
}