#include <iostream>
using namespace std;

int binarySearch(int arr[], int low, int high, int x) {
    while (low <= high) {
        int mid = low + (high - low) / 2; // Calculate mid to prevent overflow
        
        if (arr[mid] == x) {
            return mid; // Element found
        }
        else if (arr[mid] > x) {
            high = mid - 1; // Search in the left half
        }
        else {
            low = mid + 1; // Search in the right half
        }
    }
    return -1; // Element not found
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int x = 3;
    int n = sizeof(arr) / sizeof(arr[0]); // Size of the array

    int result = binarySearch(arr, 0, n - 1, x); 

    if (result == -1) {
        cout << "Element not found" << endl;
    } else {
        cout << "Element found at index " << result << endl;
    }

    return 0;
}
