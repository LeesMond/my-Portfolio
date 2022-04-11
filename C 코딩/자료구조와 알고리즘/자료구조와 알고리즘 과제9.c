#include<stdio.h>
#include<stdlib.h>
#include<string.h>

typedef struct listnode {
	char data[4];
	struct listnode* link;
} listnode;

typedef struct {
	listnode* head;
} linkedlist_h;

linkedlist_h* createlinkedlist_h(void) {
	linkedlist_h* l;
	l = (linkedlist_h*)malloc(sizeof(linkedlist_h));
	l->head = NULL;
	return l;
}

void freelinkedlist_h(linkedlist_h* l) {
	listnode* p;
	while (l->head != NULL) {
		p = l->head;
		l->head = l->head->link;
		free(p);
		p = NULL;
	}
}

void printlist(linkedlist_h* l) {
	listnode* p;
	printf("l = (");
	p = l->head;
	while (p != NULL) {
		printf("%s", p->data);
		p = p->link;
		if (p != NULL)printf(",");
	}
	printf(")\n");
}

void insertfirstnode(linkedlist_h* l, char* x) {
	listnode* newnode;
	newnode = (listnode*)malloc(sizeof(listnode));
	strcpy(newnode->data, x);
	newnode->link = l->head;
	l->head = newnode;
}

void insertmiddlenode(linkedlist_h* l, listnode* pre, char* x) {
	listnode* newnode;
	newnode = (listnode*)malloc(sizeof(listnode));
	strcpy(newnode->data, x);
	if (l == NULL) {
		newnode->link = NULL;
		l->head = newnode;
	}
	else if (pre == NULL) {
		l->head = newnode;
	}
	else {
		newnode->link = pre->link;
		pre->link = newnode;
	}
}

void insertlastnode(linkedlist_h* l, char* x) {
	listnode* newnode;
	listnode* temp;
	newnode = (listnode*)malloc(sizeof(listnode));
	strcpy(newnode->data, x);
	newnode->link = NULL;
	if (l->head == NULL) {
		l->head = newnode;
		return;
	}
	temp = l->head;
	while (temp->link != NULL) temp = temp->link;
	temp->link = newnode;
}

void deletnode(linkedlist_h* l, listnode* p) {
	listnode* pre;
	if (l->head == NULL) return;
	if (l->head->link == NULL) {
		free(l->head);
		l->head = NULL;
		return;
	}
	else if (p == NULL)return;
	else {
		pre = l->head;
		while (pre -> link != p){
			pre = pre->link;
		}
		pre->link = p->link;
		free(p);
	}
}

linkedlist_h* searchnode(linkedlist_h* l, char* x) {
	listnode *temp;
	temp = l->head;
	while (temp != NULL) {
		if (strcmp(temp->data, x) == 0)return temp;
		else temp = temp->link;
	}
	return temp;
}

void reverse(linkedlist_h * l) {
	listnode* p;
	listnode* q;
	listnode* r;

	p = l->head;
	q = NULL;
	r = NULL;

	while (p!=NULL){
		r = q;
		q = p;
		p = p->link;
		q->link = r;
	}
	l->head = q;
}

int main() {
	linkedlist_h* l;
	listnode *p;
	l = createlinkedlist_h();
	printf("(1) 리스트에서 [월], [수], [일] 노드 삽입하기!\n");
	insertlastnode(l, "월");insertlastnode(l, "수");insertlastnode(l, "일");
	printlist(l); getchar();

	printf("(2) 리스트에서 [수] 노드 탐색하기! \n");
	p = searchnode(l, "수");
	if (p == NULL)printf("찾는 데이터가 없습니다.\n");
	else printf("[%s]를 찾았습니다.\n", p->data);
	getchar();

	printf("(3) 리스트에서 [수] 뒤에 [금] 노드 삽입하기!\n");
	insertmiddlenode(l, p, "금");
	printlist(l); getchar();

	printf("(4) 리스트에서 [일] 노드 삭제하기!\n");
	p = searchnode(l, "일");
	deletnode(l, p);
	printlist(l); getchar();

	printf("(5) 리스트 순서를 역순으로 바꾸기!\n");
	reverse(l);
	printlist(l);

	freelinkedlist_h(l);
	getchar();

	return 0;
}