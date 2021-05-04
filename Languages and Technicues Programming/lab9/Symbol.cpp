#include "Symbol.h"

Symbol::Symbol(char x){
//    char table2[] = {'1','2','3','4','5','6','7','8','9','0',
//                       '-','=','q','w','e','r','t','y','u','i',
//                       'o','p','[',']','a','s','d','f','g','h',
//                       'j','k','l',';','z','x','c','v','b','n',
//                       'm',',','.','/','!','@','#','$','%','^',
//                       '&','*','(',')','_','+','Q','W','E','R',
//                       'T','Y','U','I','O','P','{','}','A','S',
//                       'D','F','G','H','J','K','L',':','"','Z',
//                       'X','C','V','B','N','M','<','>','?','|','`','~'};
    char table2[] = {'1','2','3','4','5','6','7','8','9','0'};
    for (int i = 0; i < 10; i++){
        table[i] = table2[i];
    }
    this->val = x;
    for (this->num = 0; num < 10; num++){
        if (x == table[num]){
            break;
        }
    }
}

char Symbol::getval() {
    return this->val;
}

bool Symbol::operator== (const Symbol &other) const{
    return this->val == other.val;
}
bool Symbol::operator> (const Symbol &other) const{
    return this->val > other.val;
}
bool Symbol::operator< (const Symbol &other) const{
    return this->val < other.val;
}

char abs(char x){
    if (x < 0)
        return -x;
    return x;
}

Symbol Symbol::operator~(){
    char ch = table[9-num];
    Symbol x(ch);
    return x;
}