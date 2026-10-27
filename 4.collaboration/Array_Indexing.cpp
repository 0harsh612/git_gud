#include <iostream>
using namespace std;

int main() {
    int numbers[5] = {10, 20, 30, 40, 50};
    int sum = 0;

    cout << "Calculating the sum of the array..." << endl;

    // HINT: Do arrays in C++ start at index 1 or 0? 
    // HINT: If the size is 5, what is the very last valid index?
    for (int i = 1; i <= 5; i++) {
        sum = sum + numbers[i];
    }

    cout << "The total sum is: " << sum << endl;
    cout << "Expected sum is: 150" << endl;

    return 0;
}