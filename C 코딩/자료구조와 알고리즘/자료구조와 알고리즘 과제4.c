#include<stdio.h>

void main() {
	char* ptrArray[2];
	char** ptrptr;
	int i;

	ptrArray[0] = "Korea";
	ptrArray[1] = "Japan";

	ptrptr = ptrArray;
	printf("\nptrArray[0]�� �ּ� (&ptrArray[0]) = %u", &ptrArray[0]);
	printf("\nptrArray[0]�� �� (ptrArray[0]) = %u", ptrArray[0]);
	printf("\nptrArray[0]�� ������ (*ptrArray[0]) = %c", *ptrArray[0]);
	printf("\nptrArray[0]�� ���� ���ڿ� (*ptrArray[0]) = %s\n", *ptrArray);

	printf("\nptrArray[1]�� �ּ� (&ptrArray[1]) = %u", &ptrArray[1]);
	printf("\nptrArray[1]�� �� (ptrArray[1]) = %u", ptrArray[1]);
	printf("\nptrArray[1]�� ������ (*ptrArray[1]) = %c", *ptrArray[1]);
	printf("\nptrArray[1]������ ���ڿ� (*ptrArray[1]) = %s\n", *(ptrArray + 1));

	printf("\nptrptr �ּ� (&ptrptr) = %u", &ptrptr);
	printf("\nptrptr �� (ptrptr) = %u", ptrptr);
	printf("\nptrptr 1�� ������ (*ptrptr) = %u", *ptrptr);
	printf("\nptrptr 2�� ������ (**ptrptr) = %c", **ptrptr);
	printf("\nptrptr 2�� ���� ���ڿ� (**ptrptr) = %s\n", *ptrptr);

	printf("\n");
	for (i = 0; i < 5; i++) {
		printf("%c", *(ptrArray[0] + 1));
	}
	printf("\n");
	for (i = 0; i < 5; i++) {
		printf("%c", *(*ptrptr + i));
	}
	printf("\n");
	for (i = 0; i < 5; i++) {
		printf("%c", *(ptrArray[1] + i));
	}
	printf("\n");
	for (i = 0; i < 5; i++) {
		printf("%c", *(*(ptrptr + 1) + i));
	}
	getchar();
}