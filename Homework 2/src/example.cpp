// example.cc
// $ g++ -o example example.cpp
// $ ./example

#include <iostream>
#include <vector>
#include <queue>
using namespace std;

// Question 8a
size_t longestRun(vector<bool> const &vec)
{
    size_t count = 0;
    size_t max = 0;
    for (size_t i = 0; i < vec.size(); ++i)
    {
        if (vec[i])
        {
            if (++count > max)
                max = count;
        }
        else
            count = 0;
    }
    return max;
}

// Question 8c
class Tree
{
public:
    unsigned value;
    vector<Tree *> children;
    Tree(unsigned value, vector<Tree *> children)
    {
        this->value = value;
        this->children = children;
    }
};

unsigned maxTreeValue(Tree const *root)
{
    if (root == nullptr)
        return 0;

    unsigned max = 0;
    queue<Tree const *> nodes;
    nodes.push(root);

    while (!nodes.empty())
    {
        Tree const *current = nodes.front();
        nodes.pop();
        if (current->value > max)
            max = current->value;
        for (Tree const *child : current->children)
            nodes.push(child);
    }

    return max;
}

int main()
{
    vector<bool> test1 = {true, true, false, true, true, true, false};
    cout << longestRun(test1) << endl; // 3

    vector<bool> test2 = {true, false, true, true};
    cout << longestRun(test2) << endl; // 2

    /*
        4
       /|\
      3 6 1
       / \
      2   5
    */
    Tree node2(2, {});
    Tree node5(5, {});
    Tree node6(6, {&node2, &node5});
    Tree node3(3, {});
    Tree node1(1, {});
    Tree node4(4, {&node3, &node6, &node1});

    cout << maxTreeValue(&node4) << endl; // 6
}
