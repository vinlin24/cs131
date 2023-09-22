#include <iostream>
using namespace std;

class StringOrInt
{
};

// Boxed types for the sake of demonstration.
class String : public StringOrInt
{
public:
    String(string const &str) : str_(str) {}
    string str_;
};

class Int : public StringOrInt
{
public:
    Int(int num) : num_(num) {}
    int num_;
};

class BoundedHolder
{
private:
    static const int MAX = 10;
    StringOrInt *arr_[MAX];
    int count_;

public:
    BoundedHolder()
    {
        count_ = 0;
    }
    void add(StringOrInt *ptr)
    {
        if (count_ >= MAX)
            return;
        arr_[count_++] = ptr;
    }
    StringOrInt *get(int pos) const
    {
        if (pos >= count_)
            return nullptr;
        return arr_[pos];
    }
};

int main()
{
    BoundedHolder h;
    String s("hi");
    Int i(5);
    h.add(&s);
    h.add(&i);
    // get the values from the container
    string *ps = (string *)h.get(0);
    cout << *ps << endl; // prints: hi
    int *pi = (int *)h.get(1);
    cout << *pi << endl; // prints: 5
}
