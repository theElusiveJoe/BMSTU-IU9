#include <stdio.h>

int main(){
	int m, n, x, i, none = 1,
		maxis = (-32767), smaxis = -32767,
		a, b ; // n - length
  			   // m - highth 
	scanf("%d%d", &m, &n);
	int A[n];
	
	// input first line
	for(i = 0; i < n; ++i){ 
		scanf("%d", &A[i]);
		if(A[i] == maxis)
			none = 1;
		else if(A[i] > maxis){
			a = 0;
			b = i;
			maxis = A[i];
			none = 0;
		}
		//printf("x - %d\nnone - %d\na- %d\nb- %d\nmaxis - %d\n\n", x, none, a, b, maxis);		
	}
	// input oth lines
	for(int j = 1; j < m; ++j){
		maxis = (-32767);
		for(int i = 0; i < n; ++i){
			scanf("%d", &x);
			// не слетает ли седловой элемент?
			if(b == i && (x <= A[i])) // мб он был в этом столбце?
				none = 1;
			if(x >= maxis && j == a) // мб он был в этой строке?
				none = 1;
			//может x - седловой?
			if(x > maxis){
				maxis = x;
				if(x < A[i]){
					a = j;
					b = i;
					none = 0;
				}
			}
			if(x < A[i]){
				A[i] = x;
			}
		//printf("x - %d\nnone - %d\na- %d\nb- %d\nmaxis - %d\n\n", x, none, a, b, maxis);	
		}
	}
			
		
	
	if(none)
		printf("none");
	else 
		printf("%d %d", a, b);
	
	return 0;
}

