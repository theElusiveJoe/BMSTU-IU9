template<typename T, int N>
class FenwickTree{
private:
    T* arr;
public:
    FenwickTree(T* arr);
    ~FenwickTree();

    T query(int a, int b);
    T query(int i);
    void change(int i, T newValue);
};

template<int N>
class FenwickTree<bool, N>{
private:
    char* arr;
public:
    FenwickTree(bool* arr);
    ~FenwickTree();

    bool query(int a, int b);
    bool query(int i);
    void change(int i, bool newValue);
};
