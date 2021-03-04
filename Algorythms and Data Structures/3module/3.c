#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct queue{
      long count;
      long head;
      long tail;
      long* data;
      long cap;
} q;



void init(){
      q.data = (long*)malloc(4*sizeof(long));
      q.cap = 4;
      q.count = 0;
      q.head = 0;
      q.tail = 0;

}

void enq(long x){
      if(q.count == q.cap){
            long *buff = q.data;
            long buflen = q.cap;
            q.cap*=2;
            q.data = (long*)malloc(q.cap*sizeof(long));
            if(q.head < q.tail){
                  for(int i = 0; i < buflen; i++)
                        q.data[i] = buff[i];
            } else {
                  for(int i = 0; i < q.tail; i++)
                        q.data[i] = buff[i];
                  for(int i = q.head; i < buflen; i++)
                        q.data[i+buflen] = buff[i];
                  q.head += buflen;
            }
            free(buff);
      }
      q.data[q.tail] = x;
      q.tail++;
      if(q.tail == q.cap)
            q.tail = 0;
      q.count++;
}

long deq(){
      long x = q.data[q.head];
      q.head++;
      if(q.head == q.cap)
            q.head = 0;
      q.count--;
      return x;
}

void printq(){
      printf("\nq: ");
      for(int i = 0; i < q.cap; i++)
            printf("%ld ", q.data[i]);
      printf("\ntail = %ld\n", q.tail);
      printf("head = %ld\n\n", q.head);

}

int main(){
      long n;
      scanf("%ld", &n);
      char cmd[10];
      long t;
      init();
      for(int i = 0; i<n; i++){
      //while(strcmp(cmd,"Q")){
            scanf("%s", &cmd);
            if(!strcmp(cmd,"ENQ")){
                  scanf("%ld", &t);
                  enq(t);
                  //printq();
            }
            if(!strcmp(cmd,"DEQ")){
                  printf("%ld\n", deq());
                  //printq();
            }
            if(!strcmp(cmd,"EMPTY")){
                  if(q.count)
                        printf("false\n");
                  else
                        printf("true\n");
            }

      }
      free(q.data);

}
