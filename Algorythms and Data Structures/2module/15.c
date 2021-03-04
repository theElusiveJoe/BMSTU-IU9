#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *str;
char *str2;
int *t;
int n;


int min(int a, int b) {
      if (a < b) return a;
      return b;
}

int build2(int l, int r, int n){
	int m, res = 0;
	int bound = min(r, n);
	while (l < bound){
		m = (l + r) / 2;
		res ^= build2(l, m, n);
		l = m + 1;
	}
	if (r < n){
		res ^= 1 << (((int)str[r]) - 97);
		t[r] = res;
	}
	return res;
}

void build1(int n){
      int r = 1;
	while (r < n)
		r *= 2;
	build2(0, r - 1, n);
}

int query2(int a){
	int v = 0;
	while (a>=0){
		v ^= t[a];
		a = (a&(a + 1)) - 1;
	}
	return v;
}


void update2(int i, int res){
	while (i < n){
		t[i] ^= res;
		i = i | (i + 1);
	}
}

void update1(int a){
      int res = 0;
      int len = strlen(str2);
      res ^= 1 << (((int)str[a]) - 97);
      int b = a;
      for (int i = 0; i < len; i++){
            res = (1 << ((int)str2[i] - 97)) ^ (1 << (((int)str[a]) - 97));
            update2(a, res);
            str[a] = str2[i];
            a++;
      }
}

int main(int argc, char const *argv[]) {
      //строка
      str = (char*)malloc(1000001*sizeof(char));
      gets(str);
      //создаем дерево
      t = (int*)malloc(1000001*sizeof(int*));
      //строим дерево
      n = strlen(str);
      build1(n);
      //подготавливаем запросы
      int m = 0;
	scanf("%d", &m);
      char cmd[4];
      int a, b;
      str2 = (char*)malloc(1000001 * sizeof(char));
      //

      for (int j = 0; j < m; j++){
		scanf("%s", cmd);
		if (strcmp("HD",cmd) == 0){
                  scanf("%d %d", &a, &b);
                  int k;
                  k = query2(a-1)^query2(b);
                  if(k&(k-1))
                        printf("NO\n");
                  else
                        printf("YES\n");
            }
		else{
                  scanf("%d %s", &a, str2);
                  update1(a);
            }
      }



	free(t);
	free(str);
      free(str2);
	return 0;
}
