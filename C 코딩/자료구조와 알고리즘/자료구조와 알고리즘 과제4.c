#include<stdio.h>

void main() {
	char* ptrArray[2];
	char** ptrptr;
	int i;

	ptrArray[0] = "Korea";
	ptrArray[1] = "Japan";

	ptrptr = ptrArray;
	printf("\nptrArray[0]의 주소 (&ptrArray[0]) = %u", &ptrArray[0]);
	printf("\nptrArray[0]의 값 (ptrArray[0]) = %u", ptrArray[0]);
	printf("\nptrArray[0]의 참조값 (*ptrArray[0]) = %c", *ptrArray[0]);
	printf("\nptrArray[0]의 참조 문자열 (*ptrArray[0]) = %s\n", *ptrArray);

	printf("\nptrArray[1]의 주소 (&ptrArray[1]) = %u", &ptrArray[1]);
	printf("\nptrArray[1]의 값 (ptrArray[1]) = %u", ptrArray[1]);
	printf("\nptrArray[1]의 참조값 (*ptrArray[1]) = %c", *ptrArray[1]);
	printf("\nptrArray[1]의참조 문자열 (*ptrArray[1]) = %s\n", *(ptrArray + 1));

	printf("\nptrptr 주소 (&ptrptr) = %u", &ptrptr);
	printf("\nptrptr 값 (ptrptr) = %u", ptrptr);
	printf("\nptrptr 1차 참조값 (*ptrptr) = %u", *ptrptr);
	printf("\nptrptr 2차 참조값 (**ptrptr) = %c", **ptrptr);
	printf("\nptrptr 2차 참조 문자열 (**ptrptr) = %s\n", *ptrptr);

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