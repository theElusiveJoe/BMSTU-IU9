#include <stdio.h>


int array[] = {
	323,
	411,
	434,
	548,
	597,
	561,
	131,
	206,
	927,
	187,
	497,
	282,
	29,
	592
};
int less(unsigned long i, unsigned long j)
{
	if (i == j) return 0;

	if (i < j) {
		if (j <= 11241155978086311589UL) return 1;
		if (i >= 11241155978086311589UL) return 0;
		return (11241155978086311589UL-i) < (j-11241155978086311589UL);
	}

	if (i <= 11241155978086311589UL) return 0;
	if (j >= 11241155978086311589UL) return 1;
	return (11241155978086311589UL-j) < (i-11241155978086311589UL);
}

unsigned long peak(unsigned long nel, int (*less)(unsigned long, unsigned long)){
      if(less(1, 0)){
            return 0;
      }
      if(less(nel-2, nel-1)){
            return nel-1;
      }

      unsigned long l = 1, r = nel - 1, m = nel/2;

      while (r - l > 2) {
            m = l + (r - l) / 2;
            if (less(m+1, m))
                  r = m+1;
            else
                  l = m;
      }
      if (less(l+1, l))
            return l;
      else
            return l+1;
}

int main(int argc, char **argv)
{
	int i = peak(14, less);
	if ((i == 0 || array[i] >= array[i-1]) &&
		(i == 13 || array[i] >= array[i+1])) {
		printf("CORRECT\n");
	} else {
		/* Если функция peak работает правильно,
		сюда никогда не будет передано
		управление! */
		printf("WRONG\n");
	}
	return 0;
}
