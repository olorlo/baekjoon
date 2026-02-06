#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
	char word[1000001];
	int cnt[26] = { 0 };

	scanf("%s", &word);
	int len = strlen(word);

	// 문자를 숫자로 바꿔서 배열 인덱스로 사용하는 방법
	for (int i = 0; i < len; i++) {
		// 소문자면 대문자로 바꾸기(출력이 대문자니까)
		char c = word[i];
		if (c >= 'a' && c <= 'z') {
			c -= 32;
		}
		// 인덱스를 0부터 시작하도록 A를 빼주고, 
		// word[i]가 들어오면 각 인덱스마다 1씩 증가
		cnt[c - 'A']++;
	}

	// 최대값 + 중복 검사
	int max_cnt = 0;
	int i_index = 0;
	int duplicate = 0;

	for (int i = 0; i < 26; i++) {
		if (cnt[i] > max_cnt) {
			i_index = i;
			max_cnt = cnt[i];
			duplicate = 0;
		}
		else if (cnt[i] == max_cnt) {
			duplicate = 1;
		}
	}
	if (duplicate==1)
		printf("?");
	else
		printf("%c", i_index+'A');
	return 0;
}