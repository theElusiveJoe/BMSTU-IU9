#include <vector>

using namespace std;

template<class T>
class SortedSeq {
private:
    vector<T> arr;
public:
    SortedSeq();

    SortedSeq(T x);

    void print();

    T getElem(int index);

    int getSize() {
        return arr.size();
    }

    SortedSeq<T> &operator+=(SortedSeq<T> &other);

    SortedSeq<T> &operator~();

    bool operator<(const SortedSeq<T> &other) const;

    bool operator>(const SortedSeq<T> &other) const;
    bool operator<=(const SortedSeq<T> &other) const;
    bool operator>=(const SortedSeq<T> &other) const;
    bool operator==(const SortedSeq<T> &other) const;
    bool operator!=(const SortedSeq<T> &other) const;


};
#include "SortedSeq.inl"