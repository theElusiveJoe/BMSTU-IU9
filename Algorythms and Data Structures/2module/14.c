#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int max(int a, int b) {
      if (a > b) return a;
      return b;
}
int min(int a, int b) {
      if (a < b) return a;
      return b;
}

 void build(long* t, long l, long r, long v, long *inp){
       if(l==r){
            t[v] = inp[l];
      } else {
            long m = (l+r)/2;
            build(t, l, m, 2*v, inp);
            build(t, m+1, r, 2*v+1, inp);
            t[v] = max(t[2*v], t[2*v+1]);
      }
 }

long findmax(long *t, long l, long r, long v, long a, long b){
      //printf("%ld ", v);
      if(l==a && r==b){
            return t[v];
      } else {
            int m = (r+l)/2;
            if(b <= m){
                  findmax(t, l, m, 2*v, a, b);
            } else if(a > m){
                  findmax(t, m+1, r, 2*v+1, a, b);
            } else {
                  return max(
                        findmax(t,l,m,2*v,a,min(b,m)),
                        findmax(t,m+1,r,2*v+1,max(a,m+1), b));
            }
      }
}

void update(long *t, long a, long b, long l, long r, long v){
      if(l==r)
            t[v] = b;
      else{
            long m = (l+r)/2;
            if(a <= m)
                  update(t, a, b, l, m, 2*v);
            else
                  update(t, a, b, m+1, r, 2*v+1);
            t[v] = max(t[2*v], t[2*v+1]);
      }
}


int main(int argc, char const *argv[]) {
      long n;
      scanf("%ld\n", &n);
      long *inp = (long*)malloc(n*sizeof(long));
      if(inp == NULL){
            printf("error\n");
            return 0;
      }
      for(long i = 0; i < n; i++)
            scanf("%ld\n", &inp[i]);
      long m;
      scanf("%ld\n", &m);

      long* t = (long*)malloc(4*n*sizeof(long));
      if(t == NULL){
            printf("error\n");
            return 0;
      }
      build(t, 0, n-1, 1, inp);

      char s[4];
      long a, b;
      for(long i = 0; i < m; i++){
            scanf("%s %ld %ld\n", &s, &a, &b);
            if(!(strcmp(s, "MAX"))){
                  printf("%ld\n", findmax(t, 0, n-1, 1, a, b));
            } else {
                  update(t, a, b, 0, n-1, 1);
            }
      }
      free(inp);
      free(t);

      return 0;
}
