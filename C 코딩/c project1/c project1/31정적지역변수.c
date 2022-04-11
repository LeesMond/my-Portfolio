//#include<stdio.h>
//
//int main() {
//	do {
//		static int v = 1;
//		static int b = 1;
//		static int n = 1;
//		static int m = 1;
//		int x, y;
//		char z;
//		printf("연산을 입력하세요 : ");
//		scanf("%d %c %d", &x, &z, &y);
//
//		if (z == '+') {
//			printf("덧셈은 총 %d번 실행됬습니다.\n", v);
//			printf("연산 결과 : %d\n", x + y);
//			v++;
//		}
//		if (z == '-') {
//			printf("뺄셈은 총 %d번 실행됬습니다.\n", b);
//			printf("연산 결과 : %d\n", x - y);
//			b++;
//		}
//		if (z == '*') {
//			printf("곱하기은 총 %d번 실행됬습니다.\n", n);
//			printf("연산 결과 : %d\n", x * y);
//			n++;
//		}
//		if (z == '/') {
//			printf("나누기은 총 %d번 실행됬습니다.\n", m);
//			printf("연산 결과 : %d\n", x / y);
//			m++;
//		}
//	} while (1);
//}