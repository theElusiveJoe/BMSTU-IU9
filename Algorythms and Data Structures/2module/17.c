#include <stdio.h>
#include <stdlib.h>

int **t;
int *lg;
int n;

int gcd(int a, int b) {
      if(b)
            return gcd(b, a%b);
      else
            return abs(a);
}

void calclogs(int m){
      lg = (int*)malloc((1 << m)*sizeof(int));
      int i = 1, j = 0;
      while(i < m){
            while(j < (1 << i)){
                  lg[j] = i-1;
                  //printf("%d\n", lg[j]);
                  j++;
            }
            i++;
      }
}

void log2help(int x) {
        int i,j;
        i=1;
        j=0;
        while(i<x) {
                while (j<(1 << i)) {
                        lg[j]=i-1;
                        j+=1;
                }
                i+=1;
        }
}

void build(){
      int m = lg[n]+1;
      t = (int**)malloc(n*sizeof(int*));
      for(int i = 0; i < n; i++){
            t[i] = (int*)malloc(m*sizeof(int));
      }


      int i = 0;
      while(i < n){
            scanf("%d ", &t[i][0]);
            i++;
      }

      int j = 1;
      while(j < m){
            i = 0;
            while(i <= (n - (1 << j))){
                  t[i][j] = gcd(t[i][j-1], t[i+(1 << (j-1))][j-1]);
                  i++;
            }
            j++;
      }
}

int query(int l, int r){
      int j = lg[r-l+1];
      return gcd(t[l][j], t[r-(1<<j)+1][j]);
}

int main(int argc, char const *argv[]){
      scanf("%d\n", &n);
      calclogs(30);
      build();

      int m, a, b;
      scanf("%d\n", &m);
      for (int j = 0; j < m; j++){
		scanf("%d %d",&a, &b);
            printf("%d\n", query(a,b));
      }

      free(lg);
      for(int i = 0; i < n; i++){
            free(t[i]);
      }
      free(t);
      return 0;
}
