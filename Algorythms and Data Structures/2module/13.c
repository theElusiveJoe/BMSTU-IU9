#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void prefix(char* s, int n, int* pi) {
      pi[0] = 0;
      int t = 0, i = 1;
      while (i < n) {
            while ((t > 0) && (s[t] != s[i]))
                  t = pi[t - 1];
            if (s[t] == s[i])
                  t++;
            pi[i] = t;
            i++;
            }
}

int main(int argc, char** argv) {
      //is t made of s prefixes
      char *s = argv[1];
      char *t = argv[2];
      int slen = strlen(s);
      int tlen = strlen(t);
      int glen = slen + tlen;
      char* g = (char *)malloc((1+glen) * (sizeof(char)));
      int* pi = (int *)malloc((glen) * (sizeof(int)));
      strcpy(g, s);
      strcpy((g+slen), t);
      prefix(g, glen, pi);

      for(int i = slen; i < glen; i++){
            if(pi[i] == 0){
                  printf("no");
                  free(g), free(pi);
                  return 0;
            }
      }

      printf("yes");

      free(g), free(pi);

      return 0;
}
