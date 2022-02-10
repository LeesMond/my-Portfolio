//#include<stdio.h>
//#include<stdlib.h>
//#include<time.h>
//
//int coin_toss(void);
//
//int main(void) {
//	int n1;
//	char c;
//	srand((unsigned)time(NULL));
//	printf("-앞뒷면 맞추기-\n");
//	do {
//		printf("앞면 : 0, 뒷면 : 1\n어디를 선택하시겠습니까?");
//		scanf("%d", &n1);
//		if (coin_toss() == n1) {
//			printf("맞췄습니다.\n");
//			printf("계속하시겠습니까?");
//			scanf(" %c", &c);
//			if (c == 'Y') {
//				continue;
//			}
//			if (c == 'N') {
//				break;
//			}
//		}
//		else {
//			printf("틀렸습니다.\n");
//			printf("계속하시겠습니까?");
//			scanf(" %c", &c);
//			if (c == 'Y') {
//				continue;
//			}
//			if (c == 'N') {
//				break;
//			}
//		}
//	} while (1);
//}
//int coin_toss(void) {
//	int i = rand() % 2;
//	if (i == 0)
//		return 0;
//	else
//		return 1;
//}