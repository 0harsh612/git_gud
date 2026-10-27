#include <iostream>

class A {
private:
    double x;
    double y;

public:
    void accept(int a, int b) {
        x = a;
        y = b;
    }
    // add some more overloaded functions apni creativity dikhao
    

    void accept(double a, double b) {
        x = a;
        y = b;
    }

    void display() const {
        std::cout << "x = " << x << ;// display on different line
        std::cout << "y = " << y << '\n';
    }
};

int main() {
    A obj;

    obj.accept(2);// 2 parameters expected
    obj.display();

    obj.accept(2.5, 3.5);
    obj.display();

    return 0;
}
