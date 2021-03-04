#include <math.h>
#include <stdio.h>
#include <stdlib.h>

void swap(int* a, int i, int j){
      int t = a[i];
      a[i] = a[j];
      a[j] = t;
}

void insertsort(int* a, int l, int r){
      int i, j;
      for(i=l+1; i <= r;i++)
	   for(j=i; j>l && abs(a[j-1]) > abs(a[j]); j--)
			swap(a, j, j-1);
}

void merge(int*a, int l, int m, int r){
      int t[r-l+1];
      int i = l;
      int j = m+1;
      int k = 0;
     while (k < r-l + 1){
            if((j <= r) && ((i > m) || ( abs(a[j]) < abs(a[i]) ))){
                  t[k] = a[j];
                  j++;
            } else {
                  t[k] = a[i];
                  i++;
            }
            k++;
      }
      for(i = l; i <= r; i++)
            a[i] = t[i-l];
}

void mergesortrec(int*a, int l, int r){
      if((r-l) < 4){
            insertsort(a, l, r);
      } else {
             int m = (l+r)/2;
            mergesortrec(a, l, m);
            mergesortrec(a, m+1, r);
            merge(a, l, m, r);
      }
}


void mergesort(int*a, int n){
      mergesortrec(a, 0, n-1);
}

int main(){
      int n, i;
      scanf("%d\n", &n);
      int a[n];
      for(i = 0; i < n; i++){
            scanf("%d ",&a[i]);
      }

      mergesort(a, n);

      for(i = 0; i < n; i++){
            printf("%d ", a[i]);
      }
      return 0;
}
