#include <iostream>

class my_shared_ptr
{
private:
    int *ptr = nullptr;
    int *refCount = nullptr; // a)
public:
    // b) constructor
    my_shared_ptr(int *ptr)
    {
        this->ptr = ptr;
        this->refCount = new int(1);
    }
    // c) copy constructor
    my_shared_ptr(const my_shared_ptr &other)
    {
        this->ptr = other.ptr;
        this->refCount = other.refCount;
        *this->refCount++;
    }
    // d) destructor
    ~my_shared_ptr()
    {
        *this->refCount--;
        if (*this->refCount == 0)
            delete this->ptr;
    }
    // e) copy assignment
    my_shared_ptr &operator=(const my_shared_ptr &obj)
    {
        // Prevent aliasing.
        if (this == &obj)
            return *this;

        // Modify current shared_ptr, cleaning up if necessary.
        *this->refCount--;
        if (*this->refCount == 0)
            delete this->ptr;

        // Copy over data from obj.
        this->ptr = obj.ptr;
        this->refCount = obj.refCount;
        *this->refCount++;

        return *this;
    }
};

int main()
{
    auto ptr1 = new int[100];
    auto ptr2 = new int[200];
    my_shared_ptr m(ptr1); // should create a new shared_ptr for ptr1
    my_shared_ptr n(ptr2); // should create a new shared_ptr for ptr2
    // ptr2 should be deleted, and there should be 2 shared_ptr pointing to ptr1
    n = m;
}
