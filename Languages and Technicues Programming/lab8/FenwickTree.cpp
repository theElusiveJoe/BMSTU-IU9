#include "FenwickTree.h"

template<class T, typename N>
FenwickTree<T, N>::FenwickTree(vector<T> arr, N n){
   // this->arr = new vector<T>;
    this->arr = arr;
    this->len = n;

    for (N i = 1; i < n; i++)
        this->arr [i] =  this->arr[i-1] ^ this->arr[i];

    for (N i = n-1; i > 0; i--) {
        int lower_i = (i & (i+1)) - 1;
        if (lower_i >= 0) this->arr[i] ^= this->arr[lower_i];
    }
}

template<class T, typename N>
T FenwickTree<T, N>::getXOR(N a){
    T result = 0;
    for (; a >= 0; a = (a & (a+1)) - 1)
        result ^= arr[a];
    return result;
}

template<class T, typename N>
T FenwickTree<T, N>::getXOR(N a, N b) {
    return getXOR(b)^getXOR(a-1);
}

template<class T, typename N>
void FenwickTree<T,N>::change(N i, T newValue) {
    T oldValue = getXOR(i, i);
    for (; i < len; i = (i | (i+1))){
        arr[i] ^= oldValue;
        arr[i] ^= newValue;
    }
}

