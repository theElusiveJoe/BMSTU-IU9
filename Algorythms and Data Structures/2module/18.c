#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(int argc, char** argv) {
      int n;
      scanf("%d", &n);
      float *t = (float*)malloc(n*sizeof(float));
      float a, b;
      for(int i = 0; i < n; i++) {
            scanf("%f/%f ", &a, &b);
            float f=a/b;
            if(a != 0){;
                  t[i]=log(f);
            } else
                  t[i] = 200;
      }

      float maxsum = 0, sum = 0;
      int r = 0, l = 0, start = n-1, i = n-1;
      while (i >= 0) {
            if(t[i] == 200){
                  i--;
                  sum = 0;
                 start = i;
                 printf("Zero! %d \n", i);
                 continue;

            }
            sum += t[i];
            if (sum >= maxsum) {
                      maxsum=sum;
                      r=start;
                      l=i;
                      printf("upgtate maxsum %d %d\n", l ,r);
            }
            i--;
            if (sum < 0) {
                  sum = 0;
                  start = i;
            }
      }

      printf("%d %d\n", l, r);

      free(t);
      return 0;
}
