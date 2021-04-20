#include "FenwickTree.h"

using namespace std;

template<typename T, int N> // для коструктора
T build(T *arr1, int l, int r, T *arr2) {
    int m;
    T res = 0;
    int bound = r > N ? N : r;
    while (l < bound) {
        m = (l + r) / 2;
        res += build<T, N>(arr1, l, m, arr2);
        l = m + 1;
    }
    if (r < N) {
        res += (*arr1)[r];
        (*arr2)[r] = res;
    }
    return res;
}

template<typename T, int N>
// конструктор
FenwickTree<T, N>::FenwickTree(T* arr) {
    this->arr = new T[N];
    int r = 1;
    while (r < N)
        r = r << 1;
    build<T, N>(&arr, 0, r - 1, &(this->arr));
}

template <int N>
FenwickTree<bool, N>::FenwickTree<bool, N>(bool* arr){

}

template<typename T, int N>
// запрос от начала последоваетльности
T FenwickTree<T, N>::query(int a) {
    T res = 0;
    while (a >= 0) {
        res += arr[a];
        a = (a & (a + 1)) - 1;
    }
    return res;
}

template<typename T, int N>
// запрос на отрезок
T FenwickTree<T, N>::query(int a, int b) {
    return query(b) - query(a - 1);
}

template<typename T, int N>
void FenwickTree<T, N>::change(int i, T newValue) {
    newValue -= query(i, i);
    while (i < N) {
        arr[i] += newValue;
        i = (i | (i + 1));
    }
}
