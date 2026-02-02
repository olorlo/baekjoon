#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    int arr[3] = { a, b, c };
    int arr_max = arr[0];
    int temp = 0;
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2-i; j++) {
            if (arr[j]>arr[j+1]) {
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
                
            }
        }
    }
    for (int i = 0; i < 3; i++) {
        printf("%d ",arr[i]);

    }
    return 0;
}