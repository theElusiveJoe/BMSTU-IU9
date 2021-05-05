#include <iostream>
#include "Equations.h"

using namespace std;

int main() {
    Equation a(3, 0, -10);
    Equation b(2, 0, 0);
    Equation c(1, 0, 9);
    //   Equation d(1, 0, -10);
    Equations s1;
    s1.add(a);
    // s1.add(d);
    s1.add(b);
    s1.add(c);
    for (int i = 0; i < s1.data.size() - 1; i++) {
        cout << s1.data[i].getNumOfRoots() << " ";
    }
    cout << "\n";
    Equations::EquationsIterator it = s1.begin();
    Equations::EquationsIterator ite = s1.end();
    for (; it != (++s1.end()); ++it) {
        cout << it.index << ": " << (*it).a << "*x^2+" << (*it).b << "*x+" << (*it).c << ' ' << endl;
        it.addRoot();
    }

    cout << endl;

    Equations::EquationsIterator it2 = s1.begin();
    for (; it2 != (++s1.end()); ++it2) {
        cout << it2.index << ": " << (*it2).a << "*x^2+" << (*it2).b << "*x+" << (*it2).c << ' ' << endl;
    }
    return 0;
}
