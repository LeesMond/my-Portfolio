#include<stdio.h>

void main() {
	int i = 0, n;
	int mutiply[9];

	printf("\n1~9�� ������ �Է��ϼ��� : ");
	while (1) {
		scanf("%d", &n);
		if (n < 0 || n>9) {
			printf("\n1~9�� ������ �Է��ϼ��� : ");
		}
		else
			break;
	 }

	printf("\n");
	for (i = 0; i < 9; i++) {
		mutiply[i] = n * (i + 1);
		printf("\n%d * %d = %d", n, (i + 1), mutiply[i]);
	}
	getchar();
}