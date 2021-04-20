#include <iostream>
#include "FenwickTree.cpp"

using namespace std;

int main() {
    vector<int> vec(20);
    for ( int i = 0; i<16; i++){
        vec.push_back(i);
    }
    FenwickTree fen(vec, 16);

    for ( int i = 0; i<16; i++){
        cout << fen.getXOR(i-1,1) << endl;
    }

    return 0;
}
