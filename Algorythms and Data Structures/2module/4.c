#include <stdlib.h>
#include <stdio.h>

int *array;

int compare(unsigned long i, unsigned long j)
{
        if (i <= j) {
                printf("COMPARE␣%d␣%d\n", i, j);
        } else {
                printf("COMPARE␣%d␣%d\n", j, i);
        }

        if (array[i] == array[j]) return 0;
        return array[i] < array[j] ? -1 : 1;
}

void swap(unsigned long i, unsigned long j)
{
        if (i <= j) {
                printf("SWAP␣%d␣%d\n", i, j);
        } else {
                printf("SWAP␣%d␣%d\n", j, i);
        }

        int t = array[i];
        array[i] = array[j];
        array[j] = t;
}

void shellsort(unsigned long,
        int (*)(unsigned long, unsigned long),
        void (*)(unsigned long, unsigned long));

int main(int argc, char **argv)
{
        int i, n;
        scanf("%d", &n);

        array = (int*)malloc(n * sizeof(int));
        for (i = 0; i < n; i++) scanf("%d", array+i);

        shellsort(n, compare, swap);
        for (i = 0; i < n; i++) printf("%d␣", array[i]);
        printf("\n");

        free(array);
        return 0;
}

void shellsort(unsigned long n,
        int (* compare)(unsigned long, unsigned long),
        void (* swap)(unsigned long, unsigned long))
{
      int i, j, m;
      int a[30];
      a[0] = a[1] = 1;
      for(i = 2; i < 31; i++){
            a[i] = a[i-1] + a[i-2];
            if(n < a[i]){
                  m = i-1;
                  break;
            }
      }

      for(unsigned long d = a[m]; m >=1 ; m--, d=a[m]){ // сам шаг
            for(i = 0; i+d < n; i++) //подшаги
                        if(compare(i, i+d) > 0){
                              swap(i, i+d);
                              for(j = i-d; j>=0; j-=d){
                                    if(compare(j, j+d) > 0)
                                          swap(j, j+d);
                                    else
                                          break;
                              }
                        }
      }
}
