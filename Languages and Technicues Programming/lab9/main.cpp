#include "Symbol.h"
#include "SortedSeq.h"
#include <iostream>

using namespace std;

int main() {
//    Symbol A('a');
//    Symbol B('b') ;//= new Symbol('b');
//    cout << (A<B) << endl;
//    cout << (~A).getval() << endl;
//    Symbol neA = (~A);
//    cout << neA.getval();

    Symbol A('1');
    Symbol B('2');
    Symbol C('3');
    Symbol D(~A);
    SortedSeq<Symbol> s1(A);
    SortedSeq<Symbol> s2(B);
    SortedSeq<Symbol> s3(C);
    SortedSeq<Symbol> s4(D);
    s1.print();
    s1 += s2;
    s1.print();
    s1 += s3;
    s1.print();
    s1 += s4;
    s1.print();
    s1 = ~s1;
    s1.print();
    cout << endl;
    s2.print(); cout << " - s2\n";
    s3.print(); cout << " - s3\n";
    cout << (&s2 < &s3) << " - s2<s3\n";
    cout << (&s2 > &s3) << " - s2>s3\n";
    cout << (&s2 <= &s3) << " - s2<=s3\n";
    cout << (&s2 >= &s3) << " - s2>=s3\n";
    cout << (&s2 == &s3) << " - s2==s3\n";
    cout << (&s2 != &s3) << " - s2!=s3\n";
    return 0;
}
