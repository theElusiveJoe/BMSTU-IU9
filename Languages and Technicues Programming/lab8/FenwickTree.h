#include <vector>

using namespace std;

template<class T, typename N>
class FenwickTree{
private:
    vector<T> arr;
    N len;

public:
    FenwickTree(vector<T> arr, N n);

    T getXOR(N a, N b);
    T getXOR(N a);
    void change(N i, T newValue);
};