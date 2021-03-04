#include <stdio.h>

int array[] = {
      -1,
	-1703931461,
	-625969021,
	-6420879
};

int compare(void *a, void *b)
{
	int va = *(int*)a;
	int vb = *(int*)b;
	if (va == vb) return 0;
	return va < vb ? -1 : 1;
}

int maxarray(void*, unsigned long, unsigned long,
	int (*)(void *a, void *b));

int main(int argc, char **argv)
{
	printf("%d\n", maxarray(array, 3, sizeof(int), compare));
	return 0;
}

int maxarray(void *base, unsigned long nel, unsigned long width,
      int (*compare)(void *a,void *b)){
            char *maxi = base, *now = base;
            for(int i = 0; i < nel; ++i){
                  if(compare(maxi, now) < 0)
                        maxi = now;
                  now += width;
            }
      return (maxi - (char *)base)/width;
}
