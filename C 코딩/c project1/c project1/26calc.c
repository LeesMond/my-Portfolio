//#include<stdio.h>
//
//int main(void) {
//	int x, y;
//	char a;
//	printf("----------------\n");
//	printf("A - 더하기\n");
//	printf("M - 빼기\n");
//	printf("D - 곱하기\n");
//	printf("S - 나누기\n");
//	printf("Q - 나가기\n");
//	printf("----------------\n");
//
//	do {
//		printf("무엇을 선택할 것인가요? : ");
//		scanf(" %c", &a);
//
//		if (a == 'Q')
//			break;
//		printf("숫자 입력 : ");
//		scanf("%d %d", &x, &y);
//		if (a == 'A') {
//			printf("결과 : %d\n", x + y);
//			continue;
//		} else if (a == 'M') {
//			printf("결과 : %d\n", x - y);
//			continue;
//		} else if (a == 'D') {
//			printf("결과 : %d\n", x * y);
//			continue;
//		} else if (a == 'S') {
//			printf("결과 : %d\n", x / y);
//			continue;
//		}
//	} while (1);
//	return 0;
//}