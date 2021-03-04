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
      // t > s
      char *t = argv[1];
      char *s = argv[2];
      int slen = strlen(s);
      int tlen = strlen(t);
      int pi[slen];
      prefix(s, slen, pi);
      int q, k;
      q = k = 0;
      while(k < tlen){
            while(q > 0 && s[q] != t[k])
                  q = pi[q-1];
            if(s[q] == t[k])
                  q++;
            if(q == slen){
                  printf("%d ", k-slen + 1);
                  //return 0;
                  k = k - slen + 2;
                  q = 0;
            } else {
                  k++;
            }
      }

      return 0;
}
