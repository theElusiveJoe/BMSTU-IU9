#include <stdio.h>

int main(){
	int n, num = 0, t, k;
	long  sum=0, tsum = 0;
	scanf("%d%d", &n, &k);
	int a[k];
	
	for(int i = 0; i < k; ++i){
		scanf("%d", &a[i]);
		sum += a[i];
	}
	tsum = sum;
	
	for(int i = k; i < n; ++i){
		scanf("%d", &t);
		tsum -= a[i%k];
		tsum += t;
		if(tsum > sum){
			num = i - k + 1;
			sum = tsum;
		}
		a[i%k] = t;
	}

	printf("%d", num);
	
	return 0;
}

