#include <stdio.h>

int main(){
	int n, t1 = 1, t2, i;
	scanf("%d", &n);
	scanf("%d", &t1);
	
	if (n==1){
		if(t1) printf("0 1 ");
		else printf("1 ");
		return 0;
	}
	
	for(i = 1; i < n; ++i){
		scanf("%d", &t2);
		if(!(t1 || t2)){ //if both are zeros
			printf("1 0 ");
			++i;
			break;
		}
		printf("0 ");
		t1= t2;
	}
	
	if(i==n){
		printf("0 1 ");
		return 0;
	}
	
	while(i<n){
		++i;
		scanf("%d", &t1);
		printf("%d ", t1);
	}
	return 0;
}
