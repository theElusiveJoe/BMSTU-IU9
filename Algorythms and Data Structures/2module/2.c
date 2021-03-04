#include <stdio.h>
#include <stdlib.h>
#include <math.h>


int main (){
      int i, j, n, res = 0, t, p;
      long  sum = 0;
      scanf("%d", &n);
      int a[n];
      for (i=0;i<n;i++)
            scanf("%d", &a[i]);

//получаем и обрабатываем сумму за один проход цикла
      for(i = 1; i < pow(2, n); i++, sum = 0){
            p = 1;
            for(j = 0; j < n; j++)
                  sum+= a[j]*((i>>j)%2);

            if (!(sum & (sum - 1)) && sum > 0 ){
                        res++;
            }
      }

      printf ("%d", res);
      return 0;
}
