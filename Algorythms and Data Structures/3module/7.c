#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct Elem{
	struct Elem *next;
	char *word;
} elem;


int cmp(elem *cur){
	return strlen(cur->word) - strlen(cur->next->word);
}

void swap(elem *cur){
	char* tmp;
	tmp = cur->word;
	cur->word = cur->next->word;
	cur->next->word = tmp;
}

void bsort(elem* head){
	elem* cur;
	int flag = 1;
	while(flag){
		flag = 0;
		cur = head;
		while(cur->next->word!=NULL){
			if (cmp(cur) > 0){
				swap(cur);
				flag = 1;
			}
			cur = cur->next;
		}
	}
}


int main(){
	char sent[500];
	char buf[500];
	gets(sent);

	int i = 0, j = 0, k;

	elem *head = (elem*)malloc(sizeof(elem));
	head->next = NULL;
	head->word = NULL;
	elem *cur = head;
	do {
		if(sent[i] != ' ' && sent[i] != 0){
			buf[j] = sent[i];
			j++;
		} else if (j != 0){
			buf[j] = 0;
			char *wptr = (char*)malloc((j+1)*sizeof(char));

			for(k = 0; k <= j; k++){
				wptr[k] = buf[k];
			}
			j=0;
			cur->word = wptr;
			cur->next = (elem*)malloc(sizeof(elem));
			cur = cur->next;
			cur->next = NULL;
			cur->word = NULL;
		}
		i++;
	} while(sent[i-1] != 0);

	bsort(head);

	cur = head;
	elem *cur2;
	while (cur->word!= NULL) {
		printf("%s ", cur->word);
		cur2 = cur->next;
		free(cur->word);
		free(cur);
		cur = cur2;
	}
	free(cur2->word);
	free(cur2);

	return 0;
}
