#include <vector>
#include <iostream>
#include "Equation.h"

using namespace std;

class Equations {

public:
    vector<Equation> data;

    Equations() {
        Equation end(1, 0, 0);
        (data).push_back(end);
    }

    void add(Equation e) {
        data.push_back(e);
        swap(data[data.size() - 2], data[data.size() - 1]);
    }

    Equation &operator[](const int index) {
        return data.at(index);
    }

    class EquationsIterator : public iterator<forward_iterator_tag, Equation> {
    private:
        vector<int> links;
        vector<Equation> *data;
        Equation *eq;
    public:
        int index;

        EquationsIterator(vector<Equation> *data, int index) {
            this->data = data;
            this->index = index;
            //cout << "CALLED CONSSTRUCTO\n";
            for (int i = 0; i < data->size() - 1; i++) {
                if ((*data)[i].getNumOfRoots() == 0) {
                    links.push_back(i);
                  //  cout << "pushed " << i << endl;
                }
            }
            for (int i = 0; i < (*data).size() - 1; i++) {
                if ((*data)[i].getNumOfRoots() == 1) {
                    links.push_back(i);
                 //   cout << "pushed " << i << endl;
                }
            }
            for (int i = 0; i < (*data).size() - 1; i++) {
                if ((*data)[i].getNumOfRoots() == 2) {
                    links.push_back(i);
                  //  cout << "pushed " << i << endl;
                }
            }
            links.push_back((*data).size() - 1);

            this->eq = &(*data)[(links)[index]];
        }

        EquationsIterator &operator=(const EquationsIterator &it) {
            eq = it.eq;
            return *this;
        }

        EquationsIterator &operator++() {
            index++;
            this->eq = &(*data)[(links)[index]];
            return *this;
        }

        Equation operator*() {
            return *eq;
        }

        bool operator==(const EquationsIterator &it) {
            if (this->eq == it.eq)
                return true;
            return false;
        }

        bool operator!=(const EquationsIterator &it) {
            return !(*this == it);
        }



        void addRoot() {
            (*eq).addRoot();
            (links).clear();
            for (int i = 0; i < (*data).size() - 1; i++) {
                if ((*data)[i].getNumOfRoots() == 0) {
                    links.push_back(i);
                }
            }
            for (int i = 0; i < (*data).size() - 1; i++) {
                if ((*data)[i].getNumOfRoots() == 1) {
                    links.push_back(i);
                }
            }
            for (int i = 0; i < (*data).size() - 1; i++) {
                if ((*data)[i].getNumOfRoots() == 2) {
                    links.push_back(i);
                }
            }
            links.push_back((*data).size() - 1);
        }

        void removeRoot() {
            (*eq).removeRoot();
            (links).clear();
            for (int i = 0; i < (*data).size() - 1; i++) {
                if ((*data)[i].getNumOfRoots() == 0) {
                    links.push_back(i);
                }
            }
            for (int i = 0; i < (*data).size() - 1; i++) {
                if ((*data)[i].getNumOfRoots() == 1) {
                    links.push_back(i);
                }
            }
            for (int i = 0; i < (*data).size() - 1; i++) {
                if ((*data)[i].getNumOfRoots() == 2) {
                    links.push_back(i);
                }
            }
            links.push_back((*data).size() - 1);
        }
    };

    EquationsIterator begin() {
      //  cout << "create begin: " << endl;
        return EquationsIterator(&data, 0);
    }

    EquationsIterator end() {
        return EquationsIterator(&data, data.size() - 2);
    }
};