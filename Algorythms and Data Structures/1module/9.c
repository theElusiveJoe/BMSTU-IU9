#include <stdio.h>

long array[] = {
1,
2,
3,
4,
5, 6,7,8,9
};

void revarray(void*, unsigned long, unsigned long);

int main(int argc, char **argv){
      int i;
      revarray(array, 9, sizeof(long));

printf("\n");
for (i = 0; i < 9; i++) {
printf("%ld\n", array[i]);
}
return 0;
}

void revarray(void *base, unsigned long nel, unsigned long width){
      char temp;
      int i;
      char *start = (char*) base, *end = (char*)(base + (nel-1)*width);
      while(start < end){
            for(i = 0; i < width; ++i){
                  temp = start[i];
                  start[i] = end[i];
                  end[i] = temp;
            }
            start += width;
            end -= width;

      }
}
