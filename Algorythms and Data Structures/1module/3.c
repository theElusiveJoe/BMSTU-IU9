#include <stdio.h>

int main(int argc,char **argv){
	long n, a, b, x, y;
	scanf("%ld", &n);
	scanf("%ld%ld", &a, &b);
	for(int i = 1; i < n; ++i){
		scanf("%ld%ld", &x, &y);
		if(x <= b+1){
			if(b < y) b = y;
		} else {
			printf("%ld %ld\n", a, b);
			a = x; b = y;
		}
	}
	printf("%ld %ld\n", a, b);

	return 0;
}
