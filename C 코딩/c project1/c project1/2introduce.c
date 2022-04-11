//#include<stdio.h>
//
//void enn() {
//	int n1;
//	printf("(미국)\n금액을 입력하세요 : ");
//	scanf("%d", &n1);
//	printf("\n2020년 04월 01일 10:09분 기준");
//	printf("\n금액은 %.4f 달러",n1*0.00081);
//}
//void jap() {
//	int n1;
//	printf("(일본)\n금액을 입력하세요 : ");
//	scanf("%d", &n1);
//	printf("\n2020년 04월 01일 10:09분 기준");
//	printf("\n금액은 %.4f 엔", n1 * 0.087);
//}
//void cha() {
//	int n1;
//	printf("(중국)\n금액을 입력하세요 : ");
//	scanf("%d", &n1);
//	printf("\n2020년 04월 01일 10:09분 기준");
//	printf("\n금액은 %.4f 위안", n1 * 0.0058);
//}
//void eur() {
//	int n1;
//	printf("(유럽)\n금액을 입력하세요 : ");
//	scanf("%d", &n1);
//	printf("\n2020년 04월 01일 10:09분 기준");
//	printf("\n금액은 %.4f 유로", n1 * 0.00074);
//}
//
//int main(void) {
//	printf("21741024 이종무\n");
//	int n0, n1, res;
//	printf("1. 미국\n");
//	printf("2. 일본\n");
//	printf("3. 중국\n");
//	printf("4. 유럽\n");
//	printf("나라를 선택하세요 : \n");
//	scanf("%d", &n0);
//
//	if (n0 == 1) {
//		enn();
//	}
//	else if (n0 == 2) {
//		jap();
//	}
//	else if (n0 == 2) {
//		cha();
//	}
//	else if (n0 == 2) {
//		eur();
//	}
//	else {
//		printf("아직 서비스 하지 않습니다.");
//	}
//}