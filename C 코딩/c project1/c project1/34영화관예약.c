#include<stdio.h>

void line() {
	printf("--------------------------------------------------\n");
}

int main() {
	static int seat[20] = { 0 }; char ans1, ans6; int ans2, ans3, ans4;
	static int f;
	while (1) {
		do {
			printf("���� ��ȭ�� �����Ͻðڽ��ϱ�?\n");
			printf("1. ���ͽ��ڶ�\n2. �͸��� Į�� ���ѿ���\n3. �϶���");
			printf("\n1~3���� ���� : "); scanf(" %d", &ans3);
			if (ans3 == 1) { printf("���ͽ��ڶ� 1��\n"); break; }
			if (ans3 == 2) { printf("�͸��� Į�� ���ѿ��� 2��\n"); break; }
			if (ans3 == 3) { printf("�϶��� 3��\n"); break; }
			else { printf("�ٽ� ������ �ּ���\n"); continue; }
		} while (1);
		line();
		printf("�ڸ����� �Ͻðڽ��ϱ�? Y/N : "); scanf(" %c", &ans1);
		if (ans1 == 'Y'){
			printf("��ȭǥ ����\n");
			line();
			printf("\n");
			printf("-----------��ũ��-----------\n");
			printf("1, 2, 3, 4, 5, 6, 7, 8, 9, 10\n11 12 13 14 15 16 17 18 19 20\n");
			printf("\n");
			line();
			for (int i = 0; i < 20; i++) {
				printf("%3d", seat[i]);
				if (i == 9 && i % 9 == 0) {
					printf("\n");
				}
			}
			printf("\n��� �����Ͻðڽ��ϱ�? : "); scanf("%d", &ans4);
			for (f = 0; f < ans4; f++) {
				if (f <= ans4) {
					printf("%d ��° �ڸ��� ������ �ּ��� : ", f + 1); scanf("%d", &ans2);
					if (ans2 <= 0 && ans2 > 20) {
						continue;
					}
					if (seat[ans2 - 1] == 0) {
						seat[ans2 - 1] = 1;
						printf("����Ǿ����ϴ�.\n");
					}
					else {
						printf("�̹� ����� �ڸ� �Դϴ�.\n");
						continue;
					}
				}
			}
			printf("\n\n\n����ǥ Ȯ��");
			line();
			printf("\n");
			printf("-----------��ũ��-----------\n");
			printf("1, 2, 3, 4, 5, 6, 7, 8, 9, 10\n11 12 13 14 15 16 17 18 19 20\n");
			printf("\n");
			line();
			for (int i = 0; i < 20; i++) {
				printf("%3d", seat[i]);
				if (i == 9 && i % 9 == 0) {
					printf("\n");
				}
			}
			printf("\n������ �Ϸ�Ǿ����ϴ�.\n�̿����ּż� �����մϴ�.");
			return 0;
		}

		else if (ans1 == 'N') {
			printf("�ٸ� ��ȭ�� �����Ͻǰǰ���? Y/N : "); scanf(" %c", &ans6);
			if (ans6 == 'Y') {
				continue;
			}
			if (ans6 == 'N') {
				return 0;
			}
		}
	}
	return 0;
}