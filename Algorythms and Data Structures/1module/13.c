#include <stdio.h>
#include <string.h>

int strdiff(char *a, char *b){
      int j, k;
      for(int i = 0; i < 11; ++i){
            if(a[i]==0 && b[i] == 0)
                  return -1;
            //if()
            //printf("%d - i\n", i);
            if(a[i] != b[i]){
                  for(j = 1, k = 0; k < 8; j*=2, ++k){
                        //printf("%d %d %d\n", a[i], b[i], j);
                        if((a[i]^b[i])&j)
                              return 8*i+k;
                  }
            }
            //printf("\n");
      }
      return -1;
}

int main(int argc, char **argv)
{
        char s1[1000], s2[1000];
        gets(s1);
        gets(s2);
        printf("%d\n", strdiff(s1, s2));

        return 0;
}
