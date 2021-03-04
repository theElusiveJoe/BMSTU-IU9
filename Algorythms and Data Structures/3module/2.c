#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

struct stck{
      long top;
      long* data;
} stack;

void push(long a){
      stack.data[stack.top] = a;
      stack.top++;
}

long pop(){
      stack.top--;
      return stack.data[stack.top];
}

int main(){
      long n;
      scanf("%ld", &n);
      char cmd[10];
      long t, tt;
      stack.data = (long*)malloc(n*sizeof(long));
      stack.top=0;
      for(int i = 0; i<n; i++){
            scanf("%s", &cmd);
            if(!strcmp(cmd,"CONST")){
                  scanf("%ld", &t);
                  push(t);
            }
            if(!strcmp(cmd,"ADD")){
                  push(pop() + pop());
            }
            if(!strcmp(cmd,"SUB")){
                  push(pop() - pop());
            }
            if(!strcmp(cmd,"MUL")){
                  push(pop() * pop());
            }
            if(!strcmp(cmd,"DIV")){
                  push(pop() / pop());
            }
            if(!strcmp(cmd,"MAX")){
                  t = pop();
                  tt = pop();
                  if(t > tt)
                        push(t);
                  else
                        push (tt);
            }
            if(!strcmp(cmd,"MIN")){
                  t = pop();
                  tt = pop();
                  if(t < tt)
                        push(t);
                  else
                        push (tt);
            }
            if(!strcmp(cmd,"NEG")){
                  push(-pop());
            }
            if(!strcmp(cmd,"DUP")){
                  t = pop();
                  push(t);
                  push(t);
            }
            if(!strcmp(cmd,"SWAP")){
                  t = pop();
                  tt = pop();
                  push(t);
                  push(tt);
            }

      }
      printf("%ld", pop());
      free(stack.data);


}
