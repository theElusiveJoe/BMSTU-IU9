#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct{
      int low, high;
}task;


typedef struct{
      task data[1000];
      int cap;
      int top;
} stack;

void swap(int i, int j, int* a){
      int t = a[i];
      a[i] = a[j];
      a[j] = t;
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

void push(stack* s, int a, int b){
      task t;
      t.low = a;
      t.high  = b;
      if (s->top == s->cap){
            printf("overflow\n");
      } else {
            s->top++;
            s->data[s->top] = t;
      }
}

task pop(stack* s){
      if (s->top == -1){
            printf("devastation\n");
      } else {
            s->top--;
            return s->data[s->top+1];
      }
}

void sort(int *a, int n){
      stack s;
      task t;
      int m, l, r;
      s.cap = 1000;
      s.top = -1;

      t.low = 0, t.high = n-1;
      push(&s, t.low, t.high);

      while (s.top>-1) { // пока стек не пуст
            t = pop(&s);
            m = partition(t.low, t.high, a); //разделили
            l = t.low;
            r = t.high;
            if(m+1 < r){
                  push(&s, m+1, r);
            }
            if(l < m){
                  push(&s, l, m-1);
            }
      }

}


int main(){
      int n;
      scanf("%d\n", &n);
      int a[1000];
      for(int i = 0; i < n; i++){
            scanf("%d\n", &a[i]);
      }
      sort(a, n);

      for(int i = 0; i < n; i++){
            printf("%d ", a[i]);
      }


      return 0;
}
