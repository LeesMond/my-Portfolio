//#include<stdio.h>
//#include<stdlib.h>
//#include<time.h>
//
//int get_dice_face() {
//	static int a = 0;
//	static int b = 0;
//	static int c = 0;
//	static int d = 0;
//	static int e = 0;
//	static int f = 0;
//	for (int y = 1; y <= 100; y++) {
//		int i = rand() % 6;
//		if (i == 0) a++;
//		if (i == 1) b++;
//		if (i == 2) c++;
//		if (i == 3) d++;
//		if (i == 4) e++;
//		if (i == 5) f++;
//	}
//	printf("1 -> %d\n2 -> %d\n3 -> %d\n4 -> %d\n5 -> %d\n6 -> %d\n", a, b, c, d, e, f);
//}
//
//int main() {
//	srand((unsigned)time(NULL));
//	get_dice_face();
//}