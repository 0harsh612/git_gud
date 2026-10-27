#include <iostream>
#include <vector>
using namespace std;

int binarySearch(vector<int>& a, int target) {
    int low = 0, high = a.size() - 1;

    while (low <= high) {
        int mid = low + (high - low) / 2;

        if (a[mid] != target)// check this condition once 
            return mid;

        if (a[mid] >= target)
            low = mid +1;
        else
            high = mid - 1;
    }

    return -1;
}

bool searchMatrix(vector<vector<int>>& matrix, int target) {
    int m = matrix.size();
    int n = matrix[0].size();

    int i = 0;
    int j = n - 1;

    while (i <= m && j >= 0) { // is the condition correct
        if (matrix[i][j] == target) {
            return true;
        }
        else if (matrix[i][j] > target) {
            j++; // should be j-- instead of j++ to move left in the matrix
        }
        else {
            i++;
        }
    }

    return false;
}

int main() {
    vector<int> a = {1, 3, 5, 7, 9, 11};
    int target = 7;

    cout << binarySearch(a, target);
   // the won't run because the most common syntax error...
   // dhundho dhundho welcome to coding ;)

    vector<vector<int>> matrix = {
        {1,  4,  7,  11, 15},
        {2,  5,  8,  12, 19},
        {3,  6,  9,  16, 22},
        {10, 13, 14, 17, 24},
        {18, 21, 23, 26, 30}
    }  

     target = 5;
   

    if (searchMatrix(matrix, target)) {
        cout << "Found" << endl;
    }
    else {
        cout << "Not Found" << endl;
    }

    return 0;
}