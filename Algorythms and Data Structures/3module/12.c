#include <stdlib.h>
#include <stdio.h>
#include <string.h>


int m = 26;
int gi;


typedef struct Node{
	int k;
	int endshere;
	struct Node* p;
	struct Node* arcs[26];
} node;


node* init(){
	node* y = (node*)malloc(sizeof(node));
	y->endshere = 0;
	y->p = NULL;
	y->k=1;
	for(int i = 0; i<m; i++){
		y->arcs[i] = NULL;
	}
	return y;
}


int foo(char ch){
	return ch-97;
}


void printtree(node *t, int num, int sp){
	printf("%d(%d)->", num, t->k);
	if(t->endshere)
		printf("*");
	int flag = 0;
	for(int i = 0; i<m;i++){
		if(t->arcs[i]!=0)
			flag++;
	}
	for(int i = 0; i<m;i++){
		if(t->arcs[i]!=0){
			if (flag > 1){
				printf("\n");
				for(int j = 0; j <= num-1; j++)
					printf("        ");
			}
			printf(" %c ", i+97);
			printtree(t->arcs[i], num+1, 0);
		}
	}

}


node* descend(node* t, char* str, int change){
	node *x = t, *y;
	gi = 0;
	int len = strlen(str);
	while(gi < len){
		if (x->arcs[foo(str[gi])] == NULL)
			break;
		x = x->arcs[foo(str[gi])];
		x->k += change;
		gi++;
	}

	return x;
}


void insert(node *t, char *str){
	node *x = descend(t, str, 1), *y;
	int i = gi;
	int len = strlen(str);
	if(i == len && x->endshere){
		descend(t, str, -1);
		return;
	}

	while(i < len){
		y = init();
		x->arcs[foo(str[i])] = y;
		y->p = x;

		x = y;
		i++;
	}
	x->endshere = 1;
}


int prefix(node *t, char *str){
	node *x = t, *y;
	int len = strlen(str);
	int i = 0;
	while(i < len){
		if(x->arcs[foo(str[i])] == NULL)
			return 0;
		x = x->arcs[foo(str[i])];
		i++;
	}
	return x->k;
}


void delete(node *t, char *str){
	node *x = descend(t, str, -1), *y;
	x->endshere = 0;
	int i = gi;
	while(x->p!=NULL){
		if(x->k!=0)
			break;
		y = x->p;
		i--;
		y->arcs[foo(str[i])] = NULL;
		free(x);
		x = y;
	}
}


void freetree(node* t){
	for(int i = 0; i<m; i++)
		if(t->arcs[i] != NULL)
			freetree(t->arcs[i]);
	free(t);
}


int main(){
	int n;
	scanf("%d\n", &n);

	node *t = init();

	char *str = (char*)malloc(100000*sizeof(char));
	char cmd[10];
	for(int i = 0; i < n; i++){
		scanf("%s ", cmd);
		scanf("%s", str);
		if(!strcmp(cmd, "INSERT")){
			insert(t, str);
		} else if(!strcmp(cmd, "PREFIX")){
			printf("%d\n", prefix(t, str));
		} else {
			delete(t, str);
		}
	}

	freetree(t);
	free(str);

	return 0;
}
