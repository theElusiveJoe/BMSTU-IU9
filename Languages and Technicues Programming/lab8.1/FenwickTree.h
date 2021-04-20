#include <vector>

using namespace std;

template<typename T, int N>
class FenwickTree{
private:
    vector<T> arr;

public:
    FenwickTree(T* arr);
//    ~FenwickTree();

    T query(int a, int b);
    T query(int a);
    void change(int i, T newValue);
};