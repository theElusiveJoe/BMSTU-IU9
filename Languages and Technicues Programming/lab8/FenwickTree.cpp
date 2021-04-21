#include "FenwickTree.h"
#include <iostream>

using namespace std;

//********обычный шаблон конструктора**********
template<typename T, int N> // для коструктора
T build2(T *arr1, int l, int r, T *arr2) {
    T res = 0;
    int m;
    int bound = r > N ? N : r;
    while (l < bound) {
        m = (l + r) / 2;
        res ^= build2<T, N>(arr1, l, m, arr2);
        l = m + 1;
    }
    if (r < N) {
        res ^= arr1[r];
        arr2[r] = res;
    }
    return res;
}

template<typename T, int N>
void build1(T* arr1, T* arr2){
    int r = 1;
    while (r < N)
        r = r << 1;
    build2<T, N>(arr1, 0, r - 1, arr2);
}

template<typename T, int N> // конструктор
FenwickTree<T, N>::FenwickTree(T* arr) {
    this->arr = new T[N];
    build1<T,N>(arr, this->arr);
}
//*******************************************

//********специальный шаблон конструктора**********
bool get_val(int index, char* arr){
    return bool((arr[index/8]>>index%8)%2);
}

void set_val(int index, bool newval, char* arr){
    int i1 = index/8, i2 = index%8;
    bool theNum = bool((arr[i1]>>i2)%2);
     //здесь theNum - значение эл-та дерева (а не последовательности)
    if (theNum == newval)
        return;
    char ch = 1;
    char sieve = ch<<i2;
    if (theNum){ // единицу надо поменять на ноль
       // cout << (int)arr[i1];
        arr[i1] -= sieve;
        //cout << " -> " << (int)arr[i1] << endl;
    } else { //ноль меняем на единицу
       // cout << (int)arr[i1];
        arr[i1] += sieve;
        //cout << " -> " << (int)arr[i1] << endl;
    }
}

template<int N>
bool buildbool2(bool *arr1, int l, int r, char *arr2){
    bool res = false;
    int m;
    int bound = r > N ? N : r;
    while (l < bound) {
        m = (l + r) / 2;
        res ^= buildbool2<N>(arr1, l, m, arr2);
        l = m + 1;
    }
    if (r < N) {
        res ^= arr1[r];
        //arr2[r] = res;
        set_val(r, res, arr2);
    }
    return res;
}

template<int N>
void buildbool1(bool* arr1, char* arr2){
    int r = 1;
    while (r < N)
        r = r << 1;
    buildbool2<N>(arr1, 0, r - 1, arr2);
}

template<int N>
FenwickTree<bool, N>::FenwickTree(bool *arr) {
    this->arr = new char[N/8+1];
    buildbool1<N>(arr, this->arr);
}
//*******************************************

template<typename T, int N> // деструктор
FenwickTree<T,N>::~FenwickTree() {
    delete arr;
}

template<int N> // деструктор
FenwickTree<bool, N>::~FenwickTree() {
    delete arr;
}

template<typename T, int N> // запрос от начала последоваетльности
T FenwickTree<T, N>::query(int i) {
    T res = 0;
    while (i >= 0) {
        res ^= arr[i];
        i = (i & (i + 1)) - 1;
    }
    return res;
}

template<typename T, int N>// запрос на отрезок
T FenwickTree<T, N>::query(int a, int b) {
    return query(b) ^ query(a - 1);
}

template<int N> // запрос от начала последоваетльности
bool FenwickTree<bool, N>::query(int i) {
    bool res = 0;
    while (i >= 0) {
        res = res ^ get_val(i, arr);
        i = (i & (i + 1)) - 1;
    }
    return res;
}

template<int N>// запрос на отрезок
bool FenwickTree<bool, N>::query(int a, int b) {
    return query(b) ^ query(a - 1);
}

template<typename T, int N> // изменение элемента последовательности
void FenwickTree<T, N>::change(int i, T newValue) {
    newValue ^= query(i, i);
    while (i < N) {
        arr[i] ^= newValue;
        i = (i | (i + 1));
    }
}

template<int N> // изменение элемента последовательности
void FenwickTree<bool, N>::change(int i, bool newValue) {
    if (newValue == query(i,i))
        return;

    while (i < N) {
        int i1 = i/8, i2 = i%8;
        bool theNum = bool((arr[i1]>>i2)%2);
        char ch = 1;
        char sieve = ch<<i2;
        if (theNum){ // единицу надо поменять на ноль
            //cout << (int)arr[i1];
            arr[i1] -= sieve;
            //cout << " -> " << (int)arr[i1] << endl;
        } else { //ноль меняем на единицу
            //cout << (int)arr[i1];
            arr[i1] += sieve;
            //cout << " -> " << (int)arr[i1] << endl;
        }

        i = (i | (i + 1));
    }
}