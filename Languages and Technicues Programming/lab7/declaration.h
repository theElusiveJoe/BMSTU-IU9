#include <iostream>

class Fraction{
public:
    int num = 0, deg = 0;

    Fraction(int a, int b);
    Fraction();

    Fraction operator+ (const Fraction &a);
    Fraction operator- (const Fraction &a);
    Fraction operator* (const Fraction &a);

    void print();
};

class Egyptian {
private:
    int* denoms;
    int len;

public:

    Egyptian(Fraction f, int len);
    Egyptian(const Egyptian &E);
    virtual ~Egyptian();

    int& operator[] (int index);
    Egyptian& operator= (const Egyptian &E1);

    int numOfFracs();
    Fraction toRational();
};
