#include "declaration.h"
#include <iostream>

using namespace std;

int gcd(int a, int b) {
    while (true) {
        if (a == 0 || a == b) {
            return b;
        }
        if (b == 0) {
            return a;
        }
        if (a > b) {
            a %= b;
        } else {
            b %= a;
        }
    }
}
Egyptian::Egyptian(Fraction f, int len) {
    int nr = f.num;
    int dr = 1;
    while (f.deg < 1){
        dr*=10;
        f.deg++;
    }
    int x = gcd(nr, dr);
    nr/= x, dr/= x;
    cout << nr << "/" << dr;
    this->len = len;
    this->denoms = new int[len];
    int i = 0;
    while (true) {
        if (dr == 0 || nr == 0) {
            break;
        }
        if (dr % nr == 0) {
            this->denoms[i] = dr / nr;
            break;
        }
        int n = dr / nr + 1;
        this->denoms[i] = n;
        int a = nr * n - dr;
        int b = dr * n;
        nr = a;
        dr = b;
        i++;
    }
    cout << endl;
}
Egyptian::~Egyptian() {
    delete this->denoms;
}
Egyptian::Egyptian(const Egyptian &E) {
    this->len = E.len;
    this->denoms = new int[this->len];
    for (int i = 0; i < len; i++) {
        denoms[i] = E.denoms[i];
    }
    // copy(E.denoms, E.denoms+len, this->denoms);
}

int &Egyptian::operator[](int index) {
    return (this)->denoms[index];
}
Egyptian &Egyptian::operator= (const Egyptian &E1) {
    this->len = E1.len;
    this->denoms = new int[this->len];
    for (int i = 0; i < len; i++) {
        denoms[i] = E1.denoms[i];
    }
    return *this;
}

int Egyptian::numOfFracs() {
//    for (int i = 0; i < len; ++i) {
//        std::cout << denoms[i] << " ";
//    }
//    std::cout << std::endl;

    return len;
}
Fraction Egyptian::toRational() {
    int x = 0, y = 1;
    for (int i = 0; i < len; ++i) {
        y *= denoms[i];
    }
    for (int i = 0; i < len; ++i) {
        x += y / denoms[i];
    }
    int g = gcd(x, y);
    x /= g, y /= g;
    int i = 1, c = 0;
    while(y > i){
        i*=10;
        c++;
    }
    int y1 = i / y;
    while (y*y1 != i){
        y1 = i / y;
        i*=10;
        c++;
    }
    Fraction F(x*y1, -c);
    return F;
}



Fraction::Fraction(int a, int b) {
    num = a, deg = b;
}
Fraction::Fraction() {}
int abs(int x) {
    if (x < 0)
        return -x;
    return x;
}
int getOrder(int x) {
    int i = 1, c = 0;
    while (i < abs(x)) {
        i *= 10;
        c++;
    }
    return c - 1;
}
Fraction normalize(int num, int deg) {
    deg += getOrder(num);
    while (num%10 == 0)
        num/=10;
    Fraction f(num, deg);
    return f;
}
Fraction Fraction::operator+(const Fraction &a) {
    Fraction x = *this, y = a, z;
    x.deg-=getOrder(x.num);
    y.deg-=getOrder(y.num);
    while (x.deg > y.deg) {
        x.num *= 10;
        x.deg--;
    }
    while (x.deg < y.deg) {
        y.num *= 10;
        y.deg--;
    }
    z.num = x.num + y.num;
    z.deg = x.deg;
    return normalize(x.num + y.num, x.deg);
}
Fraction Fraction::operator-(const Fraction &a) {
    Fraction x = *this, y = a;
    x.deg-=getOrder(x.num);
   y.deg-=getOrder(y.num);
    if (x.deg > y.deg) {
        while (x.deg > y.deg) {
            x.num *= 10;
            x.deg--;
        }
    } else {
        while (x.deg < y.deg) {
            y.num *= 10;
            y.deg--;
        }
    }
    return normalize(x.num - y.num, x.deg);
}
Fraction Fraction::operator*(const Fraction &a) {
    Fraction x = *this, y = a;
    x.deg-=getOrder(x.num);
    y.deg-=getOrder(y.num);
    return normalize(x.num*y.num, x.deg+y.deg);
}

void Fraction::print() {
    cout << "(" << this->num << "*10^" << this->deg << ")\n";
}