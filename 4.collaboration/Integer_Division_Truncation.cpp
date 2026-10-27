#include <iostream>
using namespace std;

int main() {
    int mathScore = 90;
    int scienceScore = 85;
    
    // HINT: An int divided by an int always gives an int, dropping the decimal.
    // How can you force the computer to treat this as a decimal division?
    float average = (mathScore + scienceScore) / 2;
    
    cout << "Calculated average: " << average << endl;
    cout << "Expected average: 87.5" << endl;
    
    return 0;
}