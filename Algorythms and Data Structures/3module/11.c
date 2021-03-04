#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>


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


void insert(elem **t, int m,int absk, int k, int v){
	elem *el = initElem();
	el->k = k;
	el->v = v;
	el->next = t[absk%m];
	t[absk%m] = el;
}



elem* find(elem **t, int m, int absk, int k){
	elem *el = t[absk%m];
	while (el!=NULL && el->k != k)
		el = el->next;

	return el;
}


int main(){
	int n = 0;
	scanf("%d\n", &n);

      int m = 100000;
      elem **t = (elem**)malloc(m*sizeof(elem*));
	for (int i = 0; i < m; i++)
		t[i] = initElem();
	elem *el, *el2;

	int x;
	int xor = 0;
	int res = 0;
	for(int i = 0; i < n; i++){
		scanf("%d ", &x);
		xor = xor^x;
		if(xor==0){
			res++;
		}
		el = find(t, m, abs(xor), xor);
		if (el == NULL){
			insert(t, m, abs(xor), xor, 1);
		} else {
			el->v++;
		}
	}



      for (int i = 0; i < m; i++) {
		el = t[i];
		while (el != NULL){
			el2 = el->next;
                  //if (el->v) printf("[%d %d]\n", el->k , el->v);
                  res+=((el->v)*((el->v)-1))/2;
			free(el);
			el = el2;
		}
	}
	free(t);
	printf("%d\n", res);

	return 0;
}
