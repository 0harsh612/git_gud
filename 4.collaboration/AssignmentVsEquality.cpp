#include <iostream>
using namespace std;

int main() {
    int score = 75;

    // HINT: A single '=' assigns a value. What operator is used to COMPARE values?
    if (score = 100) {
        cout << "Incredible, you got a perfect score!" << endl;
    } else {
        cout << "Good effort, keep practicing." << endl;
    }

    return 0;
}