#include <stdio.h>

#include <stdlib.h>

union Int32 {
      int x;
      unsigned char bytes[4];
};

typedef union Int32 num;

num* dsort1(num * a, int n, int d) {
      int i, j, k;
      int count[256];
      for (i = 0; i < 256; i++)
            count[i] = 0;

      for(i=0; i<n; i++) {
            count[a[i].bytes[d]]++;
      }

      i = 1;
      while (i < 256) {
            count[i] = count[i] + count[i - 1];
            i++;
      }

      j = n - 1;
      num* b = (num*)malloc((n+1) * sizeof(num));
      for (i = 0; i < n; i++) {
                b[i].x=a[i].x;
      }

      while (j >= 0) {
            k = a[j].bytes[d];
            i = count[k] - 1;
            count[k] = i;
            b[i].x = a[j].x;
            j--;
      }

      free(a);
      return b;
}

num* dsort2(num * a, int n, int d) {
      int i, j, k;
      int count[256];
      for (i = 0; i < 256; i++)
            count[i] = 0;

      for(i=0; i<n; i++) {
            count[a[i].bytes[d] & 128]++;
      }

      i = 254; // тут типа все наоборот
      while (i >= 0) {
            count[i] = count[i] + count[i + 1];
            i--;
      }

      j = n - 1;
      num* b = (num*)malloc((n+1) * sizeof(num));
      for (i = 0; i < n; i++) {
                b[i]=a[i];
      }

      while (j >= 0) {
            k = a[j].bytes[d];
            i = count[k & 128] - 1;
            count[k & 128] = i;
            b[i].x = a[j].x;
            j--;
      }

      free(a);
      return b;
}

int main() {
      int n;
      scanf("%d", & n);

      num* a = (num*)malloc((n+1) * sizeof(num));
      for (int i = 0; i < n; i++)
            scanf("%d", &a[i].x);

      for(int i = 0; i < 4; i++){
            a = dsort1(a, n, i);
      }

      a = dsort2(a, n, 3);

      for (int i = 0; i < n; i++)
      printf("%d\n", a[i]);

      free(a);

      return 0;
}
