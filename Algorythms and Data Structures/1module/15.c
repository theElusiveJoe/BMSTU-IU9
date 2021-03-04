#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int *argc, char **argv){
	if (argc != 4){
		printf("Usage: frame <height> <width> <text>");
		return 0;
	} else {
		int width = atoi(argv[2]), height = atoi(argv[1]), len, j;
		char *s;
		s = argv[3];
		len = strlen(s);


	if(width-2 < len || height < 3){
		printf("Error");
		return 0;
	}

	//printf("%s\n", s);

	for(j = 0; j < width; ++j) // upper frame
		printf("*");
		printf("\n");

	for(int i = 1; i < height - 1; ++i){
		printf("*"); // left f rame

		if(i == (height-1)/2){
			for(j = 0; j < (width - len - 2)/2; j++)
				printf(" ");
			printf("%s", s);
			for(j = (width - len)/2+len; j < width - 1; j++)
				printf(" ");
		} else {
			for(j = 0; j < width-2; ++j)
				printf(" ");
		}

		printf("*\n"); // right frame
	}

	for(j = 0; j < width; ++j) // lower frame
		printf("*");
	return 0;
}
}
