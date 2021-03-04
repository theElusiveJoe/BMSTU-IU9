#include <stdio.h>
#include <stdlib.h>

struct Date{
      int Day, Month, Year;
};

typedef struct Date Date;


Date* dsort(Date *a, int d, int n)
{
        int len, i, j, k;
        if (d==1)
                len = 32;
        if (d==2)
                len = 13;
        if (d==3)
                len =61;

        int count[len];
        for(i=0; i<len; i++)
                count[i]=0;


        for(i=0; i<n; i++) {
                if (d==1)
                        k=a[i].Day;
                if (d==2)
                        k=a[i].Month;
                if (d==3)
                        k=a[i].Year-1970;
                count[k]++;
        }

        i = 1;
        while (i<len) {
                count[i] = count[i] + count[i - 1];
                i++;
        }

        j=n-1;
        Date* b = (Date*)malloc(n*sizeof(Date));

        while (j>=0) {
                if (d==1)
                        k=a[j].Day;
                if (d==2)
                        k=a[j].Month;
                if (d==3)
                        k=a[j].Year-1970;
                i=count[k]-1;
                count[k]=i;
                b[i] = a[j];
                j--;
        }

        free(a);
        return b;
}

int main(){
      int n;
      scanf("%d", &n);

      Date* a=(Date*)malloc(n*sizeof(Date));
      for(int i = 0; i < n; i++)
            scanf("%d %d %d", &a[i].Year, &a[i].Month, &a[i].Day);

      a=dsort(a, 1, n);
      a=dsort(a, 2, n);
      a=dsort(a, 3, n);

      for (int i = 0; i < n; i++)
            printf("%d %d %d\n", a[i].Year,a[i].Month, a[i].Day);

      free(a);

      return 0;
}
