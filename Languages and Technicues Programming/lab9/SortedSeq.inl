#include <iostream>

using namespace std;

template<class T>
SortedSeq<T>::SortedSeq() {}

template<class T>
SortedSeq<T>::SortedSeq(T x) {
    this->arr.push_back(x);
}

template<class T>
void SortedSeq<T>::print() {
    for (auto x:arr) {
        cout << x.getval() << " ";
    }
    cout << endl;
}

template<class T>
T SortedSeq<T>::getElem(int index) {
    return arr.at(index);
}

template<class T>
SortedSeq<T> &SortedSeq<T>::operator+=(SortedSeq<T> &other) {
    vector<T> newarr;

    for (int i = 0; i < this->arr.size(); i++) {
        for (int j = 0; j < other.arr.size(); j++) {
            if (this->arr[i] == ~(other.arr[j])) {
                break;
            }
            if ( j == other.arr.size()-1)
                newarr.push_back(this->arr[i]);
        }
    }
    for (int i = 0; i < other.arr.size(); i++) {
        for (int j = 0; j < this->arr.size(); j++) {
            if (other.arr[i] == ~(this->arr[j])) {
                break;
            }
            if ( j == this->arr.size()-1)
                newarr.push_back(other.arr[i]);
        }
    }

    this->arr = newarr;

    return *this;
}

template<class T>
SortedSeq<T>& SortedSeq<T>::operator~() {
    for(int i = 0; i < this->arr.size(); i++){
        this->arr[i] =~this->arr[i];
    }
    return *this;
}

template <class T>
bool SortedSeq<T>::operator<(const SortedSeq<T> &other) const{
    for(int i = 0; i < this->arr.size && i < other.arr.size(); i++){
        if (this->arr[i] < other.arr[i]){
            return false;
        } else if (this->arr[i] > other.arr[i]){
            return true;
        }
    }
    if(this->arr.size() > other.arr.size()){
        return false;
    }
    return true;
}

template<class T>
bool SortedSeq<T>::operator==(const SortedSeq<T> &other) const {
    for(int i = 0; i < this->arr.size && i < other.arr.size(); i++) {
        if (!(this->arr[i] == other.arr[i])) {
            return false;
        }
        if (this->arr.size != other.arr.size())
            return false;
        return true;
    }
}

template<class T>
bool SortedSeq<T>::operator!=(const SortedSeq<T> &other) const {
    return !(this==other);
}

template<class T>
bool SortedSeq<T>::operator>(const SortedSeq<T> &other) const {
    return !(this<other) && !(this==other);
}

template<class T>
bool SortedSeq<T>::operator<=(const SortedSeq<T> &other) const {
    return (this < other) || (this==other);
}

template<class T>
bool SortedSeq<T>::operator>=(const SortedSeq<T> &other) const {
    return (this > other) || (this==other);
}