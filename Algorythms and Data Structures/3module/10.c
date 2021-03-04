#include <stdlib.h>
#include <stdio.h>
#include <string.h>


typedef struct Elem{
	int k;
	int v;
	struct Elem *next;
} elem;


elem* initElem(){
	elem *el = (elem*)malloc(sizeof(elem));
	el->next = NULL;
	el->k = 0;
	el->v = 0;
	return el;
}


void insert(elem **t, int m, int k, int v){
	elem *el = initElem();
	el->k = k;
	el->v = v;
	el->next = t[k%m];
	t[k%m] = el;
}



int find(elem **t, int m, int k){
	elem *el = t[k%m];
	while (el!=NULL && el->k != k)
		el = el->next;

	if (el != NULL)
		return el->v;
	else
		return 0;
}


int main(){
	int n = 0, m = 0;
	scanf("%d %d", &n, &m);

	elem **t = (elem**)malloc(m*sizeof(elem*));
	for (int i = 0; i < m; i++)
		t[i] = initElem();

	int k, v;
	char cmd[7];
	for (int i = 0; i < n; i++){
		scanf("%s %d", cmd, &k);

		if (!strcmp(cmd, "ASSIGN")){
			scanf("%d", &v);
			insert(t, m, k, v);
		}else{
			printf("%d\n", find(t, m, k));
		}
	}

	elem *el1, *el2;
	for (int i = 0; i < m; i++) {
		el1 = t[i];
		while (el1 != NULL){
			el2 = el1->next;
			free(el1);
			el1 = el2;
		}
	}
	free(t);

	return 0;
}
