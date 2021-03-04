
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
/*
s - сама строка
n - количество слов
a[] - массив длинн слов, в нем n эл-тов
len - длинна строки s
*/

int split(char *s, char ***words){

      // найдем количество слов
      int n = 0, i = 0, flag = 0, len = strlen(s);
      for (; s[i] != '\0'; i++) {
            if (s[i] == ' ')
                  flag = 0;
             else {
                  if (flag == 0){
                      n++;
                      flag = 1;
                  }
              }
        }

      int *a = (int *)malloc(n*sizeof(int));
      for (i = 0; i < n; i++) {
            a[i] = 1;                 // это чтобы нули тоже поместились
      }

      // забьём массив длинами слов
      int j = -1;
      if(s[0] == ' '){
            for(i = 0; i < len; ++i){
                  if(s[i+1]!= ' ' && s[i] == ' ')
                        j++;
                  if(s[i]!= ' ')
                        ++a[j];
                  }
      } else {
            j = 0;
            for(i = 0; i < len; ++i){
                  if(s[i]!= ' ')
                        ++a[j];
                  if(s[i]== ' ' && s[i+1] != ' ')
                        j++;
            }
      }


      //создадим массив слов
      char** p = (char**)malloc(n*sizeof(char*));
      //и выделим место под сами слова
      for(i = 0; i < n; i++){
            p[i] = (char*)malloc(a[i]*sizeof(char));
      }



      // переместим слова из строки в массив
                  // i - буква в строке
                  // j - номер слова
                  // m - буква в слове
      int m;
      for(i = 0, j = 0; i < len; ++i){
            if(s[i]!= ' '){
                  for(m = 0; m < a[j]-1; ++m)
                        p[j][m] = s[i+m];
                  p[j][m] = (char)0;
                  i += m-1;
                  ++j;
            }

      }
      *words = p;

      free(a);
	return n;
}



#define INITIAL_SIZE 128

char *getstring()
{
	char *s;
	int flag, len = 0, size = INITIAL_SIZE;

	s = (char*)malloc(INITIAL_SIZE);
	if (s == NULL) return NULL;

	for (;;) {
		if (fgets(s+len, size-len, stdin) == NULL) {
			free(s);
			return NULL;
		}

		len += (int)strlen(s+len);
		if (s[len-1] == '\n') break;

		char *new_s = (char*)malloc(size *= 2);
		if (new_s == NULL) {
			free(s);
			return NULL;
		}

		memcpy(new_s, s, len);
		free(s);
		s = new_s;
	}

	s[len-1] = 0;
	return s;
}

void printword(char *s)
{
	printf("\"");
	for (;;) {
		char c = *s++;
		switch (c) {
		case 0:
			printf("\"\n");
			return;
		case '\a':
			printf("\\a");
			break;
		case '\b':
			printf("\\b");
			break;
		case '\f':
			printf("\\f");
			break;
		case '\n':
			printf("\\n");
			break;
		case '\r':
			printf("\\r");
			break;
		case '\t':
			printf("\\t");
			break;
		case '\v':
			printf("\\v");
			break;
		case '\\':
			printf("\\\\");
			break;
		case '\"':
			printf("\\\"");
			break;
		default:
			printf(c >= 0x20 && c <= 0x7E ? "%c" : "\\x%02x", c);
		}
	}
}

int main()
{
	char *s = getstring();
	if (s == NULL) return 1;

	char **words;
	int n = split(s, &words);
	free(s);

	for (int i = 0; i < n; i++) printword(words[i]);

	for (int i = 0; i < n; i++) free(words[i]);
	free(words);
	return 0;
}
