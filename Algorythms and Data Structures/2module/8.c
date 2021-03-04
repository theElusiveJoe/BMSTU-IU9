#include <stdio.h>

void swap(int i, int j, int* a){
      int t = a[i];
      a[i] = a[j];
      a[j] = t;
}

void selectsort(int l, int r, int* a){
      int minind, i, j;
      for(i = l; i < r; i++){
            minind = i;
            for(j = i+1; j <=r; j++){
                  if(a[j] < a[minind])
                        minind = j;
            }
            swap(i, minind, a);
      }
}

int partition(int l, int r, int*a){
      int i = l, j = l;
      while (j < r) {
            if(a[j] < a[r]){
                  swap(j, i, a);
                  i++;
            }
            j++;
      }
      swap(i, r, a);
      return i;
}

void qsortrec(int l, int r, int m, int* a){
      if(l < r){
            if((l-r+1) < m){
                  selectsort(l, r, a);
            } else {
                  int q = partition(l, r, a);
                  qsortrec(l, q-1, m, a);
                  qsortrec(q+1, r, m, a);
            }
      }
}

void qsort(int n, int m, int*a){
      qsortrec(0, n-1, m, a);
}



int main(){
      int n, m;
      scanf("%d %d \n", &n, &m);
      int a[n];
      for(int i = 0; i < n; i++)
            scanf("%d\n", &a[i]);

      qsort(n, m, a);

      for(int i = 0; i < n; i++)
            printf("%d\n", a[i]);

      return 0;
}
