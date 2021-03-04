#include <stdio.h>
#include <math.h>


int main(int argc,char **argv){
	long n, k, x0, res = 0, t;
	scanf("%ld%ld%ld", &n, &k, &x0);
	//n-степень полинома, k-номер производной
	
	for(int i = 0; i < n-k; ++i){
		scanf("%ld", &t);
		for(int j = 0; j < k; j++)
			t*=(n-i-j);
		printf("%ld\n", t);
		res +=t;
		res *=x0;
	}
	scanf("%ld", &t);
	for(int j = 0; j < k; j++)
			t*=(k-j);
	res+=t;
	printf("%ld\n", t);
	
	printf("%ld\n", res);

	return 0;
}
