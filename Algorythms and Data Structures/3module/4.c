#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct queue {
        int *data;
        int *max;
        int cap, top1, top2;
        int len;
} q;

int max(int a, int b){
      return (a > b ? a : b);
}

void qinit(){
      q.len = 20000;
      q.top1 = 0;
      q.top2 = q.len-1;
      q.data = (int*)malloc(q.len*sizeof(int));
      q.max = (int*)malloc(q.len*sizeof(int));
}

void push1(int x){
      q.data[q.top1] = x;
      if(q.top1 == 0){
            q.max[0] = x;
      } else {
            q.max[q.top1] = max(x, q.max[q.top1-1]);
      }
      q.top1++;
}

void push2(int x){
      q.data[q.top2] = x;
      if(q.top2 == q.len-1){
            q.max[q.top2] = x;
      } else {
            q.max[q.top2] = max(x, q.max[q.top2+1]);
      }
      q.top2--;
}

void enq(int x){
      push1(x);
}

int pop1(){
      q.top1--;
      return q.data[q.top1];
}

int pop2(){
      q.top2++;
      return q.data[q.top2];
}
int deq(){
      if(q.top2 == q.len-1){
            while(q.top1>0){
                  push2(pop1());
            }
      }
      return pop2();
}

void qempty(){
      if (q.top1==0 && q.top2==q.len-1)
            printf("true\n");
      else
            printf("false\n");
}

void qmax(){
      if(q.top1 > 0 && q.top2 < q.len -1){
            printf("%d\n", max(q.max[q.top1-1], q.max[q.top2+1]));
      } else if (q.top1 == 0 && q.top2 < q.len -1){
            printf("%d\n",q.max[q.top2+1]);
      } else if (q.top1 > 0 && q.top2 == q.len -1){
            printf("%d\n",q.max[q.top1-1]);
      }
}


int main() {
      qinit();
      int n;
      scanf("%ld", &n);
      char cmd[10];
      int t;
      for(int i = 0; i<n; i++){
            scanf("%s", &cmd);
            if(!strcmp(cmd,"ENQ")){
                  scanf("%d", &t);
                  enq(t);
            } else if(!strcmp(cmd,"DEQ")){
                  printf("%d\n", deq());
            } else if(!strcmp(cmd,"EMPTY")){
                  qempty();
            } else if(!strcmp(cmd,"MAX")){
                  qmax();
            }
      }
      free(q.data);
      free(q.max);
      return 0;
}
