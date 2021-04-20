#include <iostream>
#include "FenwickTree.cpp"

using namespace std;

int main() {
    int vec[8];
    for (int i = 0; i<8; i++){
        vec[i] = i;
        cout << vec[i] << " ";
    }
    FenwickTree<int, 8> fen(&vec);

    for ( int i = 0; i<8; i++){
        cout << i << ":" << fen.query(i) << endl;
    }

    fen.change(0,1);

    for ( int i = 0; i<8; i++){
        cout << i << ":" << fen.query(1,i) << endl;
    }

    return 0;
}
