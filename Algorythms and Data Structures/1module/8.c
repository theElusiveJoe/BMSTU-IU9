#include <stdio.h>
#include <stdlib.h>


int main(int argc,char **argv){
	long n1, n2;
	
	scanf("%ld", &n1);
	int *a = (int*)malloc(n1*sizeof(int));
	if(a==NULL) 
		return -1;
	for(int i = 0; i < n1; ++i){
		scanf("%d", a+i);
	}
	
	scanf("%ld", &n2);
	int *b = (int*)malloc(n2*sizeof(int));
	if(a==NULL) 
		return -1;
	for(int i = 0; i < n2; ++i){
		scanf("%d", b+i);
	}
	
	
	long i = 0, j = 0;
	while(i < n1 && j < n2){
		if(*(a+i)<*(b+j)){
			printf("%d ", *(a+i));
			++i;
		}else{
			printf("%d ", *(b+j));
			++j;
		}
	}
	
	if(j == n2)
		for(;i < n1; ++i) // если второй кончился
			printf("%d ", *(a+i));	
	else
		for(;j < n2; ++j) // если первый кончился
			printf("%d ", *(b+j));
	
	
	free(a);
	free(b);
	return 0;
}
















