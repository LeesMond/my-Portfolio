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
//	printf("-�յ޸� ���߱�-\n");
//	do {
//		printf("�ո� : 0, �޸� : 1\n��� �����Ͻðڽ��ϱ�?");
//		scanf("%d", &n1);
//		if (coin_toss() == n1) {
//			printf("������ϴ�.\n");
//			printf("����Ͻðڽ��ϱ�?");
//			scanf(" %c", &c);
//			if (c == 'Y') {
//				continue;
//			}
//			if (c == 'N') {
//				break;
//			}
//		}
//		else {
//			printf("Ʋ�Ƚ��ϴ�.\n");
//			printf("����Ͻðڽ��ϱ�?");
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