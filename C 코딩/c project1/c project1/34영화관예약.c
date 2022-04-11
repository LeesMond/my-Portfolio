#include<stdio.h>

void line() {
	printf("--------------------------------------------------\n");
}

int main() {
	static int seat[20] = { 0 }; char ans1, ans6; int ans2, ans3, ans4;
	static int f;
	while (1) {
		do {
			printf("무슨 영화를 선택하시겠습니까?\n");
			printf("1. 인터스텔라\n2. 귀멸의 칼날 무한열차\n3. 일라이");
			printf("\n1~3까지 선택 : "); scanf(" %d", &ans3);
			if (ans3 == 1) { printf("인터스텔라 1관\n"); break; }
			if (ans3 == 2) { printf("귀멸의 칼날 무한열차 2관\n"); break; }
			if (ans3 == 3) { printf("일라이 3관\n"); break; }
			else { printf("다시 선택해 주세요\n"); continue; }
		} while (1);
		line();
		printf("자리예약 하시겠습니까? Y/N : "); scanf(" %c", &ans1);
		if (ans1 == 'Y'){
			printf("영화표 예약\n");
			line();
			printf("\n");
			printf("-----------스크린-----------\n");
			printf("1, 2, 3, 4, 5, 6, 7, 8, 9, 10\n11 12 13 14 15 16 17 18 19 20\n");
			printf("\n");
			line();
			for (int i = 0; i < 20; i++) {
				printf("%3d", seat[i]);
				if (i == 9 && i % 9 == 0) {
					printf("\n");
				}
			}
			printf("\n몇명 예약하시겠습니까? : "); scanf("%d", &ans4);
			for (f = 0; f < ans4; f++) {
				if (f <= ans4) {
					printf("%d 번째 자리를 선택해 주세요 : ", f + 1); scanf("%d", &ans2);
					if (ans2 <= 0 && ans2 > 20) {
						continue;
					}
					if (seat[ans2 - 1] == 0) {
						seat[ans2 - 1] = 1;
						printf("예약되었습니다.\n");
					}
					else {
						printf("이미 예약된 자리 입니다.\n");
						continue;
					}
				}
			}
			printf("\n\n\n예약표 확인");
			line();
			printf("\n");
			printf("-----------스크린-----------\n");
			printf("1, 2, 3, 4, 5, 6, 7, 8, 9, 10\n11 12 13 14 15 16 17 18 19 20\n");
			printf("\n");
			line();
			for (int i = 0; i < 20; i++) {
				printf("%3d", seat[i]);
				if (i == 9 && i % 9 == 0) {
					printf("\n");
				}
			}
			printf("\n예약이 완료되었습니다.\n이용해주셔서 감사합니다.");
			return 0;
		}

		else if (ans1 == 'N') {
			printf("다른 영화를 예약하실건가요? Y/N : "); scanf(" %c", &ans6);
			if (ans6 == 'Y') {
				continue;
			}
			if (ans6 == 'N') {
				return 0;
			}
		}
	}
	return 0;
}