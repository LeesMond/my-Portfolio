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
//		printf("������ �Է��ϼ��� : ");
//		scanf("%d %c %d", &x, &z, &y);
//
//		if (z == '+') {
//			printf("������ �� %d�� ��������ϴ�.\n", v);
//			printf("���� ��� : %d\n", x + y);
//			v++;
//		}
//		if (z == '-') {
//			printf("������ �� %d�� ��������ϴ�.\n", b);
//			printf("���� ��� : %d\n", x - y);
//			b++;
//		}
//		if (z == '*') {
//			printf("���ϱ��� �� %d�� ��������ϴ�.\n", n);
//			printf("���� ��� : %d\n", x * y);
//			n++;
//		}
//		if (z == '/') {
//			printf("�������� �� %d�� ��������ϴ�.\n", m);
//			printf("���� ��� : %d\n", x / y);
//			m++;
//		}
//	} while (1);
//}