//#include<stdio.h>
//
//int main(void) {
//	int x, y;
//	char a;
//	printf("----------------\n");
//	printf("A - ���ϱ�\n");
//	printf("M - ����\n");
//	printf("D - ���ϱ�\n");
//	printf("S - ������\n");
//	printf("Q - ������\n");
//	printf("----------------\n");
//
//	do {
//		printf("������ ������ ���ΰ���? : ");
//		scanf(" %c", &a);
//
//		if (a == 'Q')
//			break;
//		printf("���� �Է� : ");
//		scanf("%d %d", &x, &y);
//		if (a == 'A') {
//			printf("��� : %d\n", x + y);
//			continue;
//		} else if (a == 'M') {
//			printf("��� : %d\n", x - y);
//			continue;
//		} else if (a == 'D') {
//			printf("��� : %d\n", x * y);
//			continue;
//		} else if (a == 'S') {
//			printf("��� : %d\n", x / y);
//			continue;
//		}
//	} while (1);
//	return 0;
//}