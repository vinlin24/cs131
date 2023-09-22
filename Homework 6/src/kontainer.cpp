// kontainer.cpp

#include <iostream>

template <typename T>
class Kontainer
{
public:
    Kontainer() : size(0){};
    void add(T item);
    T getMin();

private:
    T elements[100];
    size_t size;
};

template <typename T>
void Kontainer<T>::add(T item)
{
    this->elements[this->size++] = item;
}

template <typename T>
T Kontainer<T>::getMin()
{
    T *min = nullptr;
    for (size_t i = 0; i < this->size; ++i)
    {
        T *current = &this->elements[i];
        if (min == nullptr || *current < *min)
            min = current;
    }
    return *min;
}

// Test code.
int main(void)
{
    Kontainer<int> k;
    int values[] = {6, 4, -17, 0, 3, 6, -11, 8, 24};
    for (int value : values)
        k.add(value);
    std::cout << k.getMin() << std::endl;
}
