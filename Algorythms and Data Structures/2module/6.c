#include <stdlib.h>
#include <stdio.h>

void swap(void *base, int i, int j){


      char **c= base;

      char* t = c[i];
      c[i] = c[j];
      c[j] = t;
}

int compare(const void* a,const void* b){
      int count = 0, k = 0;
      char**c = (char**)a;
      char**d = (char**)b;

      while((*c)[k] != 0){
            if((*c)[k] == 'a')
                  count++;
            k++;
      }
      k = 0;

      while((*d)[k] != 0){
            if((*d)[k] == 'a')
                  count--;
            k++;
      }
      return count;
}

void heapify(int i, int  nel, int width, void* base, int (*compare)(const void *a, const void *b)){
      int l = 2*i + 1;
      int r = l+1;
      int j = i;

      while(1){
            l = 2*i + 1;
            r = l+1;
            j = i;

            if(l < nel && compare(base+i*sizeof(char*), base+l*sizeof(char*)) < 0)
                  i = l;
            if(r < nel && compare(base+i*sizeof(char*), base+r*sizeof(char*)) < 0)
                  i = r;
            if(i == j)
                  break;
            swap(base, i, j);
      }
}



void buildheap(void *base, int nel, int width, int (*compare)(const void *a, const void *b)){
      for(int i = (nel/2 - 1); i >=0; i--){
            heapify(i, nel, width, base, compare);
      }
}

void hsort(void *base, int nel, int width, int (*compare)(const void *a, const void *b)){
      buildheap(base, nel, width, compare);
      for(int i = nel-1; i >=0 ; i--){
            swap(base, 0, i);
            heapify(0, i, width, base, compare);
            for(int i = 0; i < nel; i++){
                  printf("%c ", (*(char**)(base+i*sizeof(char*)))[0]);
            }
            printf("\n");
      }
}


int main(){
      int n, len = 20;
      scanf("%d\n", &n);
      char**a = (char**)malloc(n*sizeof(char*));;
      for(int i = 0; i < n; i++){
            a[i] = (char*)malloc(len*sizeof(char));
            scanf("%s", a[i]);
      }

      hsort((void*)a, n, sizeof(char*), compare);

      printf("\n******result******\n");
      for(int i = 0; i < n; i++){
            printf("%c ", *(char*)(a[i]));
            free(a[i]);
      }
      free(a);

      printf("\n");
      return 0;
}
