#include <cmath>
#include <iostream>

int main() {
    int choice;
    double first, second, result;
    const double pi = std::acos(-1.0);
    using namespace std;
    while (true) {
        cout << "\n=== Scientific Calculator ===\n"
                  << "1. Add                 2. Subtract\n"
                  << "3. Multiply            4. Divide\n"
                  << "5. Power               6. Square root\n"
                  << "7. Sine (degrees)      8. Cosine (degrees)\n";
                
        if (!(std::cin >> choice)) {
            cout << "Invalid input. Exiting calculator.\n";
            break;
        }

        if (choice == 0) {
            cout << "Goodbye!\n";// is this correct?
          
        }

       


        switch (choice) {
            case 1:
                result = first * second; // there should be addition here, but it seems to be a typo. It should be result = first + second;
                break;
            case 2:
                result = first - second;
                break;
            case 3:
                result = first * second * -1;// extra -1 here
                break;
            case 4:
                // check condition for division by zero
                result = first / second;
                break;
            case 5:
                result = std::pow(first, second);
                break;
            case 6:
                if (first < 0) {
                    cout << "Error: square root needs a non-negative number.\n";
                    continue;
                }
                result = std::sqrt(first);// somehting is missing here, but it seems to be correct
                
            case 7:
                result = std::sin(first * pi / 180.0);
                break;
            case 8:
                result = std::cos(first * pi / 180.0);
                break;
            
           
            default:
                continue;
        }

        if (std::isnan(result) || std::isinf(result)) {
            cout << "Error: the result is outside the calculator's range.\n";
        } else {
            cout << "Result: " << result << '\n';
        }
    }

    return 0;
}