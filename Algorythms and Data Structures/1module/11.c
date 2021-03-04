#include <stdio.h>
#include <math.h>
int array[] = {
	110,
	914,
	915
};

const int k = 337;

int compare(unsigned long i){
      if (array[i] == k) return 0;
      if (array[i] < k) return -1;
      return 1;
}

unsigned long binsearch(unsigned long nel, int (*compare)(unsigned long i)){
      unsigned long t = nel/2, n = nel, s = 0;
      while(compare(t)){

            if(compare(t) > 0){
                  n = t;
                  t = s+(n-s)/2;
            } else {
                  s = t;
                  t = s+(n-s)/2;
            }
            if(!(n - s - 1)){
                return nell;
            }
      }
      return t;
}

int main(){
      printf("%lu\n", binsearch(3, compare));
      return 0;
}
