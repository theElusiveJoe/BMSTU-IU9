#include <iostream>

using namespace std;


class Equation {
public:
    double a, b, c, d;

    Equation(double a, double b, double c) {
        if (a == 0) {
            cout << "error";
            exit(0);
        }
        this->a = a;
        this->b = b;
        this->c = c;
        this->d = b * b - 4 * a * c;
    }

    int getNumOfRoots() {
        if (d > 0)
            return 2;
        if (d == 0)
            return 1;
        return 0;
    }

    void removeRoot() {
        if (d > 0) {
            c = b * b / 4 / a;
            d = 0;
            return;
        } else if (d == 0) {
            c++;
            d = b * b - 4 * a * c;
            return;
        }
    }

    void addRoot() {
        if (d < 0) { // 0 решений
            c = b * b / 4 / a;
            d = 0;
            return;
        } else if (d == 0) {
            if (a > 0)
                c--;
            else
                c++;
            
            d = b * b - 4 * a * c;
            return;
        }
    }
};
