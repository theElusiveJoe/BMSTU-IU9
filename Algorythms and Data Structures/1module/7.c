#include <stdio.h>
#include <stdlib.h>

int main(){
	long n, k;
	scanf("%ld%ld", &k, &n);
	long *b = (long*)malloc((n-1)*sizeof(long));
	if(b==NULL)
		return -1;

	for(long i = 0; i < n-1; ++i) // забиваем единичками
		*(b+i) = 1;

	/*for(int i = 0; i <= sqrt(n); ++i){ // забиваем массив простых чисел
			for(long j = 2*(i+2)-2; j < n-1; j+=(i+2))
				a[j]=0;
	}
//отладка
/***********************
	for(long i = 0; i < n-1; ++i){
		if(a[i])
		printf("%ld ",i+2);
	}
	printf("\n");
/***********************/
	for(int i = 0; i <= n-1; ++i){
			for(long j = 2*i+2; j < n-1; j+=(i+2))
				*(b+j)=*(b+i)+1;
	}
	for(long i = 0; i < n-1; ++i){
		if(*(b+i)==k)
			printf("%ld ",i+2);
	}
	/*for(long i = 0; i < n-1; ++i){
		if(b[i]==k)
			printf("*%ld %ld\n",i+2, b[i]);
		else
			printf("%ld %ld\n",i+2, b[i]);
	}*/

	free(b);
	return 0;
}
