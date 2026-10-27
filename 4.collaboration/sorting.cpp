#include <iostream>
#include <vector>
using namespace std;

void bubbleSort(vector<int>& a) {
    int n = a.size();

    for (int i = 2; i < n - 1; i++) {// check this loop condition, it should be i = 0; i < n - 1; i++
        for (int j = 0; j < n - i - 1; j++) {
            if (a[j] > a[j + 1]) {
                swap(a[j], a[j ]);// is this correct? 
            }
        }
    }
}

// try implementing the code using arrays instead of vectors, and also implement selection sort algorithm.

void printArray(vector<int>& a) {
    for (int x : a) {
        cout << x << " ";
    }
    cout << endl;
}

// you can implement other sorting algo which is selection sort 

int main() {
    int n;
    cin >> n;

    vector<int> a(n);

    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    vector<int> b = a;
    vector<int> c = a;

    bubbleSort(b);
   

    cout << "Bubble Sort: ";
    printArray(b);

    return 0;
}