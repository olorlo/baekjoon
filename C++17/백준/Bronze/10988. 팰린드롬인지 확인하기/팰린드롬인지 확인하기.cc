#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
	char word[100];
	char reverse[100];
	int cnt = 0;
	char* new_str;
	
	scanf("%s", &word);

	int len = strlen(word);

	for (int i = 0; i < len; i++) {
		reverse[i] = word[len - 1 - i];
	}
	for (int i = 0; i < len; i++) {
		if (reverse[i] != word[i]) {
			break;
		}
		cnt++;
	}

	if (cnt == len)
		printf("1");
	else
		printf("0");

	return 0;
}