#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int count[20];

int strcmpp ( const char * s1 , const char * s2 )
{
      if(strlen(s1) > strlen(s2)) return 1;
      return -1;

}


void csort(char *src, char *dest) {
      for(int i = 0; i < 70; i++)
            dest[i] = 0;
      char  b[20][30], sour[70];
      strncpy(sour, src, 70);
      for(int i = 0; i<20; i++)
            for(int j = 0; j< 30; j++)
                  b[i][j] = 0;
      //добавим пробел в начале
      for(int i = strlen(sour)-1; i >= 0; i--)
            sour[i+1] = sour[i];
      sour[0] = ' ';

      //загоним слова в массив
      int words = 0, t = 0;
      for(int i = 1; i < strlen(sour);i++, t = 0){
            if(sour[i] != ' ' && sour[i-1] == ' '){
                  while(sour[i] != ' ' && i < strlen(sour)){
                        b[words][t] = sour[i];
                        i++;
                        t++;
                  }
                  words++;
            }
      }

      int k[words];
      for(int i = 0; i < words; i++) k[i] = 0;

      for(int i = 0; i < words-1; i++)
            for(int j = i+1; j < words; j++){
                  if(strcmpp(b[i], b[j]) < 1)
                        k[j]++;
                  else
                        k[i]++;
            }


      for(int i = 0; i < words; i++)
            for(int j = 0; j < words; j++)
                  if(i == k[j]){
                        strncat(dest, b[j], 30);
                        strncat(dest, " ", 30);
                        count[i] = b[j][0];
                  }
            dest[strlen(dest)-1] = 0;
}


int main(){
      char src[70], dest[70];
      gets(src);
      csort(src, dest);
      printf("%s\n", dest);
        return 0;
}
