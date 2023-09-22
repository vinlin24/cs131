#include <iostream>
using namespace std;

template <typename T>
void callQuack(T const &obj)
{
    obj.quack();
}

class Duck
{
public:
    void quack() const { cout << "Quack!\n"; };
};

class DuckPerson
{
public:
    void quack() const { cout << "I say quack!\n"; };
};

class Goose
{
public:
    void honk() const { cout << "Honk!\n"; };
};

int main()
{
    Duck d;
    DuckPerson p;
    Goose g;
    callQuack(d); // Quack!
    callQuack(p); // I say quack!
    // Compiler error if not commented out:
    // error: 'const class Goose' has no member named 'quack'
    callQuack(g);
}
