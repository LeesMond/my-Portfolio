#include<stdio.h>

int main(void) {
	char borad[3][3];
	int x, y, k, i;

	for (x = 0; x < 3; x++)
		for (y = 0; y < 3; y++)borad[x][y] = ' ';
	for (k = 0; k < 3; k++) {
		printf("(x, y)ÁÂÇ¥ : ");
		scanf("%d %d", &x, &y);
		borad[x][y] = (k % 2 == 0) ? 'X' : 'O';
		for (i = 0; i < 3; i++) {
			printf("---|---|---\n");
			printf(" %c | %c | %c\n", borad[i][0], borad[i][1], borad[i][2]);
		}
		printf("---|---|---\n");
	}
	return 0;
}