#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int *inp;
int *t;
int n;

int max(int a, int b) {
      if (a > b) return a;
      return b;
}
int min(int a, int b) {
      if (a < b) return a;
      return b;
}

int peak(int l){
      if((l == 0) && n-1==0) return 1;
      if(l == 0){
            if(inp[l] >= inp[l+1])
                  return 1;
            else
                  return 0;
      }
      if(l == (n-1)){
            if(inp[l] >= inp[l-1])
                  return 1;
            else
                  return 0;
      }
      if(inp[l] >= inp[l-1] && inp[l] >= inp[l+1])
            return 1;
      return 0;
}

void build(int l, int r, int v){
       if(l==r){
            t[v] = peak(l);
      } else {
            int m = (l+r)/2;
            build(l, m, 2*v);
            build(m+1, r, 2*v+1);
            t[v] = t[2*v] + t[2*v+1];
      }
 }

int query(int l, int r, int v, int a, int b){
      if(l==a && r==b){
            //printf("v = %d\n", v);
            return t[v];
      } else {
            //printf("v = %d\n", v);
            int m = (r+l)/2;
            if(b <= m){
                  query(l, m, 2*v, a, b);
            } else if(a > m){
                  query(m+1, r, 2*v+1, a, b);
            } else {

                  return
                        (query(l,m,2*v,a,min(b,m)) +
                        query(m+1,r,2*v+1,max(a,m+1), b));
            }
      }
}

int findindex(int a, int l, int r, int v){
      if(l==r){
            return v;
      }else{
            int m = (l+r)/2;
            if(a <= m)
                  findindex(a, l, m, 2*v);
            else
                  findindex(a, m+1, r, 2*v+1);
      }
}




void update(int a, int b, int l, int r, int v){
      if(l==r){
            //printf("now v = %d\n", v);
            inp[a] = b;
            t[v] = peak(a);
            int w;
            if(a > 0){
                  w = findindex(a-1, 0, n-1, 1);
                  //printf("now w = %d\n", w);
                  t[w] = peak(a-1);
                  w/=2;
                  while(w>0){
                        t[w] = t[2*w] + t[2*w+1];
                        w/=2;
                  }
            }
            if(a < n-1){
                  w = findindex(a+1, 0, n-1, 1);
                  //printf("now w = %d\n", w);
                  t[w] = peak(a+1);
                  w/=2;
                  while(w>0){
                        t[w] = t[2*w] + t[2*w+1];
                        w/=2;
                  }
            }
      }else{
            int m = (l+r)/2;
            if(a <= m)
                  update(a, b, l, m, 2*v);
            else
                  update(a, b, m+1, r, 2*v+1);
            t[v] = t[2*v] + t[2*v+1];
      }
}



int main(int argc, char const *argv[]){
      scanf("%d\n", &n);
      inp = (int*)malloc(n*sizeof(int));
      t = (int*)malloc(3*n*sizeof(int));
      for(int i = 0; i < n; i++){
            scanf("%d\n", &inp[i]);
      }
      build(0, n-1, 1);
      char cmd[5];
      int m, a, b;
      scanf("%d\n", &m);
      for (int j = 0; j < m; j++){
		scanf("%s %d %d", cmd, &a, &b);
		if (strcmp("UPD",cmd)){
                  printf("%d\n", query(0, n-1, 1, a, b));
            }
		else{
                  update(a, b, 0, n-1, 1);
            }
      }

      free(inp);
      free(t);
      return 0;
}
