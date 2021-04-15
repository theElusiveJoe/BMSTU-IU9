#include <iostream>
#include "declaration.h"

using namespace std;

void foo(Egyptian E){
    Egyptian X = E;
    X.toRational();
    cout << X.numOfFracs();
}

int main() {
    //fraction f = {7, 15}, g = {7, 12};
    Fraction F(15,-1);
    F.print();
    Egyptian E(F, 2);
    Fraction G = E.toRational();
    G.print();
    foo(E);
    //Fraction a(4,5), b(75, 3);
   // Fraction c = b*a;
//    c.print();
//    c= b-a;
//    c.print();
//    c = a*b;
//    c.print();
//    Egyptian *E1 = new Egyptian(f, 3);
//    Egyptian *E2 = new Egyptian(g, 2);
////    E1.numOfFracs();
////   fraction g = E1.toRational();
////    cout << g.numenator <<"/"<< g.denomenator;
//    cout << (*E1)[0] << " " << (*E1)[1] << " " << (*E1)[2] << " - e1" <<endl;
//    cout << (*E2)[0] << " " << (*E2)[1] << " " << (*E2)[2] << " - e2" <<endl;
//    *E2 = *E1; // тут работает перегрузка оператора
//    delete E1;
//    cout << (*E2)[0] << " " << (*E2)[1] << " " << (*E2)[2] << " - e2" << endl;
//    Egyptian *E3 = E2; // а тут работает конструктор копий
//    cout << (*E3)[0] << " " << (*E3)[1] << " " << (*E3)[2] << " - e3" << endl;
//    delete E2;
    return 0;
}
