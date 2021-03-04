#include <stdio.h>
#include <string.h>

/*int overlap(char* s1, char* s2){
      int l1 = 0, max = 0, flag,i, j;
      for(; s1[l1] != 0; l1++);
      for(int k = 0; k < (strlen(a[i][k])); k++){ //это длинна наложения
            flag = 1;
            for(int l = 0; l < k; l++){ // а тут считаем, какие конкретно буквы сравнивать
                  if(a[i][strlen(a[i][k])-k+l] !=a[j][l])
                        flag = 0;
            }
            if (flag) max = k;
      }

      return max;
}
*/

#define min(a,b) \
   ({ __typeof__ (a) _a = (a); \
       __typeof__ (b) _b = (b); \
     _a < _b ? _a : _b; })

int main(){
      int n = 0, len = 0, i = 0, j = 0, max = 0;
      scanf("%d", &n);
      char a[10][30];
      int c[10];
      gets(a[0]);
      for (i = 0; i < n; i++) {
            gets(a[i]);
            c[i] = strlen(a[i]);
      }

      int b[10][10], flag;
      for(i = 0; i < n; i++){ //левое словво
            for(j = 0; j < n; j++){ // правое слово
                  if (i == j) b[i][i] = 0;
                  else {
                        for(int k = 0; k < min(c[i], c[j]); k++){ //это длинна наложения
                              flag = 1;
                              for(int l = 0; l < k; l++){ // а тут считаем, какие конкретно буквы сравнивать
                                    if(a[i][c[i]-k+l] != a[j][l])
                                          flag = 0;
                              }
                              if (flag) max = k;
                        }
                        b[i][j] = max;
                  }
            }
      }

      for(i = 0; i < n; i++)
            len+=strlen(a[i]);

      int l, m;
      for(int k = 0; k < n-1; k++){
            max = 0;
            for(i = 0; i < n; i++)
                  for(j = 0; j < n; j++)
                        if(b[i][j] > max){
                              max = b[i][j];
                              l = i;
                              m = j;
                        }
            len-=max;
            for(i = 0; i < n; i++){
                  b[i][m] = 0;
                  b[l][i] = 0;
            }
      }

      printf("%d\n", len);

      return 0;
}
