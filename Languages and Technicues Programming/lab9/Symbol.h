class Symbol{
private:
    char val;
    int num;
    char table[10];
public:
    int powerOfSet = 10;

    Symbol(char x);

    char getval();

    bool operator== (const Symbol &other) const;
    bool operator< (const Symbol &other) const;
    bool operator> (const Symbol &other) const;
    Symbol operator~ ();

};