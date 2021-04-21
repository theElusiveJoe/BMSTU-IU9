#include <iostream>
#include "FenwickTree.cpp"

using namespace std;

int main() {
    //для int
    int vec[10];
    for (int i = 0; i < 10; i++) {
        vec[i] = i;
        cout << vec[i] << " ";
    }
    cout << "- исходный массив" << endl;

    FenwickTree<int, 10> fen(vec);

    for (int i = 0; i < 10; i++) {
        cout << fen.query(i, i) << " ";
    }
    cout << " - получили" << endl;


    fen.change(1, 255);
    fen.change(0, 255);
    for (int i = 0; i < 10; i++) {
        cout << fen.query(i, i) << " ";
    }
    cout << " - изменили" << endl;

    cout << endl << "*****************************************\n";

    bool bec[10] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1};
    FenwickTree<bool, 10> fen2(bec);
    for (int i = 0; i < 10; i++) {
        cout << bec[i] << " ";
    }
    cout << "- исходный массив" << endl;
    for (int i = 0; i < 10; i++) {
        cout << fen2.query(i,i) << " ";
    }
    cout << " - получили" << endl;

    fen2.change(0, 0);
    fen2.change(5, 0);


    for (int i = 0; i < 10; i++) {
        cout<< fen2.query(i,i) << " ";
    }
    cout << endl;


    return 0;
}