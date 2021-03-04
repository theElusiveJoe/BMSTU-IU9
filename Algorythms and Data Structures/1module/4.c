#include <stdio.h>

int main(){
	unsigned long s1 = 0, s2 = 0, n, s0;
	char t = 0;
	
	scanf("%c", &t);
	while(t != 0x20){
		if(t <= 'Z') // uppercase 
			n = t - 0x41;
		else n = t - 0x47;
		s0 = ((s1 >> n)|1) << n;
		s1 |= s0;
		scanf("%c", &t);
	}
	
	scanf("%c", &t);
	while(t != '\n'){
		if(t <= 'Z') // uppercase 
			n = t - 0x41;
		else n = t - 0x47;
		s0 = ((s2 >> n)|1) << n;
		s2 |= s0;
		scanf("%c", &t);
	}
	
	s1 = s1&s2;
	for(int i = 0; i < 26; ++i){
		if(s1%2)
			printf("%c", (i+0x41));
		s1/=2;
	}
	
	for(int i = 26; i < 52; ++i){
		if(s1%2)
			printf("%c", (i+0x47));
		s1/=2;
	}

	return 0;
}

